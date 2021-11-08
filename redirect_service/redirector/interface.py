import traceback
from time import time

from uuid import uuid4

from redirector import datastore, tools, fetcher

def get_redirect_url(urlid):
    try:
        return datastore.get_redirect_url(urlid)
    except Exception as e:
        print(e)
        return None

def push_data_to_store(data):
    try:
        data['dataid'] = str(uuid4())
        super_ip = tools.supernetter(data['ipaddress'])
        snet_values = datastore.get_snet_val(super_ip)
        if snet_values:
            data['latitude'] = snet_values['latitude']
            data['longitude'] = snet_values['longitude']
            data['pincode'] = snet_values['zip']
            data['city'] = snet_values['city']
        else:
            details = fetcher.fetch_details_for_ip(super_ip)
            if details:
                datastore.put_snet_val(details)
                data['latitude'] = str(details['latitude'])
                data['longitude'] = str(details['longitude'])
                data['pincode'] = str(details['zip'])
                data['city'] = str(details['city'])
        data_new = tools.transform_tpoint(data)
        data_new["availableRamKey"] = tools.get_ram_gbs(data.get('availableRam'))
        datastore.increment_respective_counts(data['urlid'], data_new['brand'], data_new['os'], data_new['availableRamKey'])
        data_new["time"] = str(int(time()))
        datastore.put_submitted_data(data_new)
    except Exception as e:
        traceback.print_exc()