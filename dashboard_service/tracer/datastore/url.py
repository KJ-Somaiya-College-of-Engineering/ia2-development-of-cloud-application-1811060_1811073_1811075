from tracer.properties import get_db_instance
from tracer.utils import generate_id, jsonify_clicks

from boto3.dynamodb.conditions import Key, Attr

from time import time

db = get_db_instance()
table = db.Table('URLs')

def add_url(url_target, user_id, url_og):
    url_obj = {
        'urlid'     : generate_id(5),
        'url_target': url_target,
        'created_ts': int(time()),
        'user_id'   : user_id,
        'hits'      : 0,
        'clicks'    : {
            'OS'    : {
                'Linux'     : 0,
                'Windows'   : 0,
                'MacOSX'    : 0,
                'Android'   : 0,
                'iOS'       : 0,
                'OtherOS'     : 0,
            },
            'Brands' : {
                'Vivo'      : 0,
                'Xiaomi'    : 0,
                'Asus'      : 0,
                'Nokia'     : 0,
                'Apple'     : 0,
                'Motorola'  : 0,
                'Samsung'   : 0,
                'OtherBrand'     : 0
            },
            'RAMs' : {
                'TwoGB'     : 0,
                'FourGB'    : 0,
                'SixGB'     : 0,
                'EightGB'   : 0,
                'OtherRAM'  : 0
            }
        }
    }
    if url_og:
        url_obj['url_og'] = url_og
    try:
        table.put_item(Item = url_obj)
        return url_obj['urlid']
    except Exception as e:
        print(e)
        return None

def get_all_urls(uuid):
    data = table.scan(FilterExpression=Attr('user_id').eq(uuid))
    if data:
        return_list = []
        for item in data['Items']:
            title = item.get('url_title')
            url_obj = {
                    "_id": str(item['urlid']),
                    "redirect_url": str(item['url_target']),
                    "created_ts": int(item['created_ts']),
                    "clicks" : jsonify_clicks(item.get('clicks')),
                    "hits" : int(item['hits']),
                    "url_og": item.get("url_og")
                }
            if item.get("url_og") and item.get("url_og").get("title"):
                url_obj['title'] = item.get("url_og").get("title")
            elif title:
                url_obj['title'] = title
            
            return_list.append(url_obj)
        return return_list

def get_specific_url(uuid, urlid):
    data = table.scan(FilterExpression=Attr('user_id').eq(uuid) & Key('urlid').eq(urlid))
    if data and data.get('Items'):
        if(len(data['Items']) > 0):
            item = data['Items'][0]
            title = item.get('url_title')
            url_obj = {
                    "_id": str(item['urlid']),
                    "redirect_url": str(item['url_target']),
                    "created_ts": int(item['created_ts']),
                    "clicks" : jsonify_clicks(item.get('clicks')),
                    "hits" : int(item['hits']),
                    "url_og": item.get("url_og")
                }
            if item.get("url_og") and item.get("url_og").get("title"):
                url_obj['title'] = item.get("url_og").get("title")
            elif title:
                url_obj['title'] = title
            return url_obj
                
        else :
            return None

def update_og_data(uuid, urlid, og_new):
    data = table.scan(FilterExpression=Attr('user_id').eq(uuid) & Key('urlid').eq(urlid), ProjectionExpression='urlid')
    if not data:
        return
    if data['Count'] != 1:
        return
    update_query = 'set url_og = :newog'
    try:
        table.update_item(
            Key={
                'urlid': urlid
            },
            UpdateExpression=update_query,
            ExpressionAttributeValues={
                ':newog' : og_new
            },
            ReturnValues='NONE'
        )
    except Exception as e:
        print(e)

def delete_url(uuid, urlid):
    try:
        table.delete_item(
            Key={
                'urlid' : urlid
            },
            ConditionExpression=Attr('user_id').eq(uuid)
        )
        return True
    except Exception as e:
        print(e)