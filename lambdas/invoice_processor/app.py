import json
import os
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['TABLE_NAME'])

def lambda_handler(event, context):
    for record in event['detail']:
        table.put_item(Item={
            'invoiceId': record['invoiceId'],
            'amount': record['amount'],
            'customer': record['customer']
        })
    return {"status": "success"}
