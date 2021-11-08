from boto3.dynamodb.conditions import Key, Attr

from tracer.properties import get_db_instance

from time import time

db = get_db_instance()
table = db.Table('URLs')

def add_url(url_target, user_id, url_title, url_id):
    url_obj = {
        'urlid'     : url_id,
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
    if url_title:
        url_obj['url_title'] = url_title
    try:
        table.put_item(Item = url_obj)
        return url_obj['urlid']
    except Exception as e:
        print(e)
        return None

id = add_url(
'https://chat.whatsapp.com/KDh4UceuxxC0GUbCDwMSey',
'1717016f-0247-4634-b01a-44f12b54d4a8',
'Everything Required to Crack GATE 2022 | Gate Material, Resources, Videos, PYQs, Question Banks | 100% Free',
'gatecse'
)
