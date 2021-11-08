from flask import Blueprint, request, jsonify

from tracer.interfaces import tpoints

from tracer.validations import login_required

app = Blueprint('tpoints', __name__)

@app.route('/tpoints/locations')
@login_required
def get_locations(uuid):
    urlid = request.args.get('urlid')
    if not urlid:
        return jsonify({ "STATUS" : "FAIL" })
    data = tpoints.get_location_data(urlid)
    if data:
        return jsonify({ "STATUS" : "OK", "DATA" : data })
    return jsonify({ "STATUS" : "FAIL" })

@app.route('/tpoints')
@login_required
def get_data(uuid):
    urlid = request.args.get('urlid')
    if not urlid:
        return jsonify({ "STATUS" : "FAIL" })
    last_evaluated_key = request.args.get('lek')
    data = tpoints.get_tpoints(urlid, last_evaluated_key)
    if data:
        return jsonify({ "STATUS" : "OK", "DATA" : data[0], "LEK": data[1] })
    return jsonify({ "STATUS" : "FAIL" })