import boto3


class DynamoDbSetup:
    dynamodb = None

    @classmethod
    def create_table(cls):
        if not DynamoDbSetup.dynamodb:
            DynamoDbSetup.dynamodb = boto3.client('dynamodb', endpoint_url="http://localhost:8000")
        DynamoDbSetup.dynamodb.create_table(
            AttributeDefinitions=[{
                'AttributeName': 'url',
                'AttributeType': 'S'
            }, {
                'AttributeName': 'timestamp',
                'AttributeType': 'N'
            }],
            KeySchema=[{
                'AttributeName': 'timestamp',
                'KeyType': 'HASH'
            }, {
                'AttributeName': 'url',
                'KeyType': 'RANGE'
            }],
            TableName='Views',
            ProvisionedThroughput={
                'ReadCapacityUnits': 10,
                'WriteCapacityUnits': 10
            })

    @classmethod
    def delete_table(cls):
        if not DynamoDbSetup.dynamodb:
            DynamoDbSetup.dynamodb = boto3.client('dynamodb', endpoint_url="http://localhost:8000")
        DynamoDbSetup.dynamodb.delete_table(TableName='Views')

    @classmethod
    def delete_item(cls, url, timestamp):
        if not DynamoDbSetup.dynamodb:
            DynamoDbSetup.dynamodb = boto3.client('dynamodb', endpoint_url="http://localhost:8000")
        DynamoDbSetup.dynamodb.delete_item(
            TableName='Views',
            Key={
                'timestamp': {'N': str(timestamp)},
                'url': {'S': url}
            }
        )


if __name__ == '__main__':
    DynamoDbSetup.delete_item(url="google.com", timestamp=101010)
