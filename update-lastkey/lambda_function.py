import json
import boto3
import os

dynamodb = boto3.resource('dynamodb')
TABLE_NAME = os.getenv('TABLE_NAME')

def lambda_handler(event, context):
    pkey = event['pkey']
    skey = event['skey']
    lastkey = event['lastkey']
    
    table = dynamodb.Table(TABLE_NAME)
    response = table.update_item(
        Key={
            'pkey': pkey,
            'skey': skey
        },
        UpdateExpression="set lastkey=:l",
        ExpressionAttributeValues={
            ':l': lastkey
        },
        ReturnValues="UPDATED_NEW"
    )
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
