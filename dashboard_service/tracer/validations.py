import re
from tracer import utils
from functools import wraps
from flask import request, jsonify
from tracer.properties import get_site_secret_key

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'token' in request.headers:
            obj = utils.get_object_from_token(request.headers['token'], get_site_secret_key())
            if obj and obj.get('UUID'):
                return f(obj['UUID'])
        return jsonify({ "STATUS" : "FAIL" })
    return decorated_function

def email(user_email) :
    try :
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        if(re.search(regex, user_email)) :
            return True
        else :
            return False
    except Exception as e :
        print(e)
        return False

def password(user_password) :
    try :
        regex = '^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[a-zA-Z]).{8,}$'
        if(re.search(regex, user_password)) :
            return True
        else :
            return False
    except Exception as e :
        print(e)
        return False

def is_valid_url(redirect_url):
    if(redirect_url.startswith('https://trcr.tk') or redirect_url.startswith('http://trcr.tk') or redirect_url.startswith('http://tracer.syscape.live') or redirect_url.startswith('https://tracer.syscape.live')):
        return False
    try :
        regex = re.compile(
            r'^https?://'  # http:// or https://
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?|'  # domain...
            r'localhost|'  # localhost...
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
            r'(?::\d+)?'  # optional port
            r'(?:/?|[/?]\S+)$', re.IGNORECASE)
        # print(redirect_url is not None and regex.search(redirect_url))
        if(re.search(regex, redirect_url)):
            return True
        else :
            return False
    except Exception as e :
        print(e)
        return False

def validate_and_return_file_extension(filename):
    if '.' in filename:
        extension = filename.rsplit('.', 1)[1].lower()
        if extension in ALLOWED_EXTENSIONS:
            return extension
    return None