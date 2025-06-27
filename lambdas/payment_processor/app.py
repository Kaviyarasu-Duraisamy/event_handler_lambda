import json
import os
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['TABLE_NAME'])

def lambda_handler(event, context):
    for record in event['detail']:
        table.put_item(Item={
            'paymentId': record['paymentId'],
            'amount': record['amount'],
            'payer': record['payer']
        })
    return {"status": "success"}
