from pprint import pprint
import boto3


def increase_counter(user_id, url, verb, timestamp, increment, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")

    table = dynamodb.Table('Views')

    response = table.update_item(
        Key={
            'timestamp': timestamp,
            'url': url
        },
        UpdateExpression="SET user_id=:user_id, verb=:verb ADD hitcounter :increment",
        ExpressionAttributeValues={
            ':user_id': user_id,
            ':increment': increment,
            ':verb': verb
        },
        ReturnValues="UPDATED_NEW"
    )
    return response


def lambda_handler(event, context):
    return increase_counter(**event, increment=1)


if __name__ == '__main__':
    json1 = {"user_id": 1, "url": "google.com", "verb": "GET", "timestamp": 101010}
    update_response = lambda_handler(json1, None)
    print("Update counter for {} succeeded:".format(json1['url']))
    pprint(update_response)
