from tracer.properties import get_db_instance
from tracer.utils import get_uuid

from boto3.dynamodb.conditions import Key, Attr

import time

db = get_db_instance()
table = db.Table('USERs')

def add_user(name, email):
    user = {
        'uuid': get_uuid(),
        'email': email,
        'name': name,
        'date_joined': int(time.time())
    }
    try:
        data = table.scan(
            FilterExpression=Attr('email').eq(email),
            Select='COUNT'
        )
        if data['Count'] == 0:
            table.put_item(Item = user)
            return user['uuid']
    except Exception as e:
        print(e)
        return None

def get_user(email=None, uuid=None):
    data = None
    if(email):
        data = table.scan(FilterExpression=Attr('email').eq(email))
    if(uuid):
        data = table.query(KeyConditionExpression=Key('uuid').eq(uuid))
    if data and data.get('Items'):
        return data['Items'][0]

def check_uuid_exists(uuid):
    data = table.query(KeyConditionExpression=Key('uuid').eq(uuid))
    return data['Count'] == 1