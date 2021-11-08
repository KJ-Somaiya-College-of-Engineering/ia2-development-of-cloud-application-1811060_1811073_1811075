from traceback import print_exc

from flask import Blueprint, request, jsonify

from tracer.validations import login_required
from tracer.interfaces import url

app = Blueprint('url', __name__)

@app.route('/url', methods=['GET', 'POST', 'DELETE'])
@login_required
def url_func(uuid):
    if request.method == 'POST':
        data = request.get_json()
        redirect_url = data.get('redirect')
        res = url.add_url(redirect_url, uuid)
        if res:
            if not res[1]:
                return jsonify({ "STATUS" : "OK", "ID" : res[0] })
            return jsonify({ "STATUS" : "OK", "ID" : res[0], "OG_DETAILS" : res[1]})
        else :
            return jsonify({ "STATUS" : "FAIL","ERROR":"Unable to add URL" })
    
    elif request.method == 'GET':
        res = url.get_all_urls(uuid)
        if len(res) >= 0:
            return jsonify({ "STATUS" : "OK", "DATA" : res })
        else :
            return jsonify({ "STATUS" : "FAIL","ERROR":"Unable to fetch URLs" })
    
    elif request.method == 'DELETE':
        try:
            urlid = request.args['urlid']
            res = url.delete_url_from_user(uuid, urlid)
            if res:
                return jsonify({"STATUS": "OK"})
            else:
                return jsonify({"STATUS": "FAIL"})
        except:
            print_exc()
            return jsonify({"STATUS": "FAIL"})


@app.route('/url/details')
@login_required
def specific_url(uuid):
    urlid = request.args.get('id')
    if not urlid:
        return jsonify({ "STATUS" : "FAIL" })
    details = url.get_url(uuid, urlid)
    if details:
        # details['hits'] = url.get_hits(urlid)
        return jsonify({ "STATUS" : "OK", "DATA" : details })
    return jsonify({ "STATUS" : "FAIL" })

@app.route('/url/update/ogdata', methods=['POST'])
@login_required
def update_og(uuid):
    try:
        urlid = request.args['urlid']
        data = request.get_json()
        title = data.get('title')
        description = data.get('description')
        image = data.get('image')
        d_url = data.get('durl')
        url.update_og_details(uuid, urlid, title, description, image, d_url)
        return jsonify({"STATUS": "OK"})
    except:
        print_exc()
        return jsonify({"STATUS": "FAIL"})

@app.route('/image/upload', methods=['POST'])
@login_required
def upload_image(_):
    try:
        image_file_ref = request.files['cover']
        image_url = url.get_image_url_from_image(image_file_ref)
        return jsonify({"STATUS": "OK", "IMAGE_URL": image_url})
    except:
        print_exc()
        return jsonify({"STATUS": "FAIL"})
