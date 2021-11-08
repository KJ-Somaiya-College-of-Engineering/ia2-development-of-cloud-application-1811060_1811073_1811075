from tracer.datastore import tpoints

def get_location_data(urlid):
    try:
        return tpoints.get_all_locations(urlid)
    except Exception as e:
        print(e)

def get_tpoints(urlid, last_evaluated_key=None):
    try:
        return tpoints.get_collected_data(urlid, last_evaluated_key)
    except Exception as e:
        print(e)