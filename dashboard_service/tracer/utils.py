import jwt
import string
import random
import datetime
import uuid

from tracer.properties import get_aws_region, get_bucked_name

def generate_id(length = 4):
    char = string.ascii_uppercase + string.ascii_lowercase + string.digits
    return ''.join(random.choice(char) for _ in range(length))

def get_object_from_token(token, key):
    try:
        return jwt.decode(token, key, algorithms=['HS256'])
    except jwt.DecodeError as e:
        print(e)
        return None

def get_uuid():
    return str(uuid.uuid4())

def get_token_from_object(obj, key, time=None):
    try:
        if time:
            obj['exp'] = datetime.datetime.utcnow() + datetime.timedelta(seconds=time)
            return jwt.encode(obj,key)
        return jwt.encode(obj, key)
    except Exception as e:
        print(e)
        return None

def jsonify_clicks(clicks):
    jsonified = {
            'OS'    : {
                'Linux'     : int(clicks['OS']['Linux']),
                'Windows'   : int(clicks['OS']['Windows']),
                'MacOSX'    : int(clicks['OS']['MacOSX']),
                'Android'   : int(clicks['OS']['Android']),
                'iOS'       : int(clicks['OS']['iOS']),
                'Other'     : int(clicks['OS']['OtherOS'])
            },
            'Brands' : {
                'Vivo'      : int(clicks['Brands']['Vivo']),
                'Xiaomi'    : int(clicks['Brands']['Xiaomi']),
                'Asus'      : int(clicks['Brands']['Asus']),
                'Nokia'     : int(clicks['Brands']['Nokia']),
                'Apple'     : int(clicks['Brands']['Apple']),
                'Motorola'  : int(clicks['Brands']['Motorola']),
                'Samsung'   : int(clicks['Brands']['Samsung']),
                'Other'     : int(clicks['Brands']['OtherBrand'])
            },
            'RAMs' : {
                'TwoGB'     : int(clicks['RAMs']['TwoGB']),
                'FourGB'    : int(clicks['RAMs']['FourGB']),
                'SixGB'     : int(clicks['RAMs']['SixGB']),
                'EightGB'   : int(clicks['RAMs']['EightGB']),
                'Other'     : int(clicks['RAMs']['OtherRAM'])
            }
        }
    return jsonified

def generate_image_url_from_id(image_id):
    image_template = "https://{}.s3.{}.amazonaws.com/{}"
    image_url = image_template.format(get_bucked_name(), get_aws_region(), image_id)
    return image_url