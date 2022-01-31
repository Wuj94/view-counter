import os
import unittest
import counter_lambda
import reader_lambda
from setup import DynamoDbSetup


class Test(unittest.TestCase):
    write_json = {"user_id": 1, "url": "google.com", "verb": "GET", "timestamp": 101010}
    read_json = {"url": "google.com", "timestamp": 101010}

    @classmethod
    def setUpClass(cls) -> None:
        os.system("docker run -p 8000:8000 amazon/dynamodb-local &")
        DynamoDbSetup.create_table()

    @classmethod
    def tearDownClass(cls) -> None:
        DynamoDbSetup.delete_table()
        os.system("docker stop $(docker ps | grep dynamodb-local | cut -d " " -f 1)")

    def test_increase_counter(self):
        def teardown_test_items():
            DynamoDbSetup.delete_item(self.write_json['url'], self.write_json['timestamp'])
        hitcounter = counter_lambda.increase_counter(**self.write_json, increment=1)['Attributes']['hitcounter']
        self.assertTrue(1 == hitcounter)
        teardown_test_items()

    def test_read_counter(self):
        hitcounter = counter_lambda.increase_counter(**self.write_json, increment=1)['Attributes']['hitcounter']
        self.assertTrue(1 == hitcounter)

        readcounter = reader_lambda.read_counter(**self.read_json)
        self.assertTrue(readcounter['Item']['hitcounter'] == 1)


if __name__ == '__main__':
    unittest.main()
