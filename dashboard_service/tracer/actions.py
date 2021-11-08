import requests 
from bs4 import BeautifulSoup
from tracer.properties import get_email_client, get_s3_instance
from traceback import print_exc
from tracer.utils import get_uuid

SENDER = "Tracer <auth@trcr.tk>"
SUBJECT = "Here's Your Magic Link, {}"
BODY_TEXT = (
                "Here is your Magic Link.\r\n"
                "Click the link below, and you will be Authenticated in no time!\n\n"
                "{}"
            )
CHARSET = "UTF-8"
CONFIGURATION_SET = "ConfigSet"

client = get_email_client()

s3 = get_s3_instance()

def upload_image(file_reference, file_extension):
    unqid = "im-" + get_uuid()
    filename = unqid + "." + file_extension
    s3.put_object(
        Key=filename,
        Body=file_reference,
        ACL='public-read'
    )
    return filename

def send_token_mail(recipient_name, recipient_email, token, referer):
    auth_url = f"{referer}/verify/{token}"
    try:
        client.send_email(
            Destination={
                'ToAddresses': [
                    recipient_email,
                ],
            },
            Message={
                'Body': {
                    'Text': {
                        'Charset': CHARSET,
                        'Data': BODY_TEXT.format(auth_url),
                    }
                },
                'Subject': {
                    'Charset': CHARSET,
                    'Data': SUBJECT.format(recipient_name),
                },
            },
            Source=SENDER
        )
        return True
    except Exception as e:
        print(e)
        return False

def fetch_url_og_details(url):
    try:
        reqs = requests.get(url)
        soup = BeautifulSoup(reqs.text, 'html.parser') 
        og_contents = dict()
        temp_title = None
        for title in soup.find_all('title'): 
            temp_title = title.get_text()
            break
        temp_img = None
        for link in soup.find_all('link'):
            if link.get('rel') in ["icon", "shortcut icon"]:
                temp_img = link.get('href')
    
        for meta in soup.find_all('meta'):
            if meta.get("property") and meta.get("property")[:3] == "og:":
                field = meta.get("property")[3:]
                if field == "title":
                    og_contents['title'] = meta.get("content")
                
                elif field == "site_name":
                    og_contents['site_name'] = meta.get("content")
                
                elif field == "url":
                    og_contents['url'] = meta.get("content")
                
                elif field == "image":
                    og_contents['image'] = meta.get("content")

                elif field == "description":
                    og_contents['description'] = meta.get("content")
        
        if not og_contents.get("og:title"):
            og_contents['title'] = temp_title
        
        if not og_contents.get("og:site_name"):
            og_contents['site_name'] = "Tracer"

        if not og_contents.get("og:url"):
            og_contents['url'] = url
        
        if not og_contents.get("og:image") and temp_img:
            og_contents['image'] = temp_img
        
        return og_contents
    except:
        print_exc()
        return None