from flask import Blueprint, jsonify, request, make_response

from tracer import utils, actions
from tracer.properties import get_site_secret_key
from tracer.interfaces import auth

app = Blueprint('auth', __name__)

@app.route('/auth/verify')
def verify():
    token = request.args.get('token')
    data = utils.get_object_from_token(token, get_site_secret_key())
    if data:
        status = auth.check_if_uuid_exists(data['UUID'])
        if status:
            return jsonify({'STATUS':'OK', 'DATA': data})
        else :
            return jsonify({ 'STATUS': 'FAIL', 'MSG' : 'OLDTOKEN'})
    else:
        return jsonify({ 'STATUS': 'FAIL'})

@app.route('/authenticate', methods=['POST'])
def authenticate():
    referer = request.headers.get('Origin')
    data = request.get_json()
    email = data.get('email')
    user_details = auth.get_user_details(email)
    if not user_details:
        return jsonify({ 'STATUS': 'FAIL' })
    user_obj = {
        'NAME': user_details['name'],
        'UUID': user_details['uuid'],
        'EMAIL': user_details['email']
    }
    token = utils.get_token_from_object(user_obj, get_site_secret_key())
    check = actions.send_token_mail(user_obj['NAME'], user_obj['EMAIL'], token, referer)
    if check:
        return jsonify({ 'STATUS': 'OK', 'MSG': 'Check Your Email for Auth Link'})
    return jsonify({ 'STATUS': 'FAIL' })

@app.route('/auth/new', methods=['POST'])
def new():
    referer = request.headers.get('Origin')
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    uuid = auth.create_new_user(name, email)
    token = utils.get_token_from_object({ 'NAME': name, 'EMAIL': email, 'UUID': uuid }, get_site_secret_key())
    check = None
    if uuid:
        check = actions.send_token_mail(name, email, token, referer)
    if check:
        return jsonify({ 'STATUS': 'OK' })
    return jsonify({ 'STATUS': 'FAIL' })