from tracer.datastore import url
from tracer.datastore.tpoints import fetch_total_url_points
from tracer.validations import is_valid_url, validate_and_return_file_extension
from tracer.actions import fetch_url_og_details, upload_image
from tracer.utils import generate_image_url_from_id

def add_url(url_target, user_id):
    if not is_valid_url(url_target):
        return None
    url_og = fetch_url_og_details(url_target)
    return (url.add_url(url_target, user_id, url_og), url_og)

def get_all_urls(user_id):
    try:
        return url.get_all_urls(user_id)
    except Exception as e:
        print(e)
        return None

def get_url(user_id, url_id):
    return url.get_specific_url(user_id, url_id)

def get_hits(urlid):
    return fetch_total_url_points(urlid)

def update_og_details(user_id, url_id, title, description, image, d_url):
    url.update_og_data(user_id, url_id, {
        "title": title,
        "description": description,
        "image": image,
        "url": d_url
    })

def get_image_url_from_image(image_file):
    image_id = upload_image(image_file, validate_and_return_file_extension(image_file.filename))
    return generate_image_url_from_id(image_id)

def delete_url_from_user(uuid, url_id):
    return url.delete_url(uuid, url_id)