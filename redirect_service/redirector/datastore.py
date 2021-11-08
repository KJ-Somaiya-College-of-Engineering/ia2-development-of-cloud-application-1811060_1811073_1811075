from decimal import Decimal

import boto3

from boto3.dynamodb.conditions import Key

db = boto3.resource('dynamodb')
table_urls = db.Table('URLs')
table_tpoints = db.Table('TPOINTs')
table_snets = db.Table('SNETs')

def get_redirect_url(urlid):
    data = None
    data = table_urls.query(KeyConditionExpression=Key('urlid').eq(urlid))
    if data and data['Items'] and len(data['Items']) > 0:
        if data['Items'][0].get('url_og'):
            return (data['Items'][0]['url_target'], data['Items'][0]['url_og'], "O")
        elif data['Items'][0].get('url_title'):
            return (data['Items'][0]['url_target'], data['Items'][0]['url_title'], "T")
        else :
            return (data['Items'][0]['url_target'],)

def put_submitted_data(data):
    table_tpoints.put_item(Item=data)

def get_snet_val(snet):
    data = None
    data = table_snets.query(KeyConditionExpression=Key('ipaddress').eq(snet))
    if data and data['Items'] and len(data['Items']) > 0:
        return data['Items'][0]

def put_snet_val(snet_data):
    table_snets.put_item(Item=snet_data)

def increment_respective_counts(urlid, brand, os, ram):
    update_query = f'set hits = hits + :inc, clicks.OS.{os} = clicks.OS.{os} + :inc, clicks.Brands.{brand} = clicks.Brands.{brand} + :inc, clicks.RAMs.{ram} = clicks.RAMs.{ram} + :inc'
    try:
        table_urls.update_item(
            Key={
                'urlid': urlid
            },
            UpdateExpression=update_query,
            ExpressionAttributeValues={
                ':inc' : Decimal(1)
            },
            ReturnValues='NONE'
        )
    except Exception as e:
        print(e)
        print("QUERY::>>", update_query)