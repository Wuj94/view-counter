from pprint import pprint
import boto3


def read_counter(url, timestamp, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")

    table = dynamodb.Table('Views')
    response = table.get_item(
        Key={
            'timestamp': timestamp,
            'url': url
        },
        ProjectionExpression='hitcounter'
    )
    return response


def lambda_handler(event, context):
    return read_counter(**event)


if __name__ == '__main__':
    json1 = {"url": "google.com", "timestamp": 101010}
    read_response = lambda_handler(json1, None)
    print("Read counter for {} succeeded:".format(json1['url']))
    pprint(read_response)
