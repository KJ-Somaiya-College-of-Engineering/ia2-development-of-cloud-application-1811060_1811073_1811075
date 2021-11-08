from tracer.properties import get_db_instance

from boto3.dynamodb.conditions import Attr

db = get_db_instance()
table = db.Table('TPOINTs')

def get_all_locations(urlid):
    data = table.scan(
        ProjectionExpression='latitude, longitude',
        FilterExpression=Attr('urlid').eq(urlid)
    )
    return_data = []
    if data :
        return_data.extend(data.get('Items'))
    lk=None
    while 'LastEvaluatedKey' in data:
        lk = data['LastEvaluatedKey']
        data = table.scan(
            ProjectionExpression='latitude, longitude',
            FilterExpression=Attr('urlid').eq(urlid),
            ExclusiveStartKey=lk
        )
        if data :
            return_data.extend(data.get('Items'))
    return return_data

def get_collected_data(urlid, last_evaluated_key=None):
    data = None
    if last_evaluated_key:
        data = table.scan(
            FilterExpression=Attr('urlid').eq(urlid),
            ExclusiveStartKey={ 'dataid': last_evaluated_key }
        )
    else:
        data = table.scan(
            FilterExpression=Attr('urlid').eq(urlid),
        )
    if data:
        if data.get('LastEvaluatedKey'):
            return (data.get('Items'), data.get('LastEvaluatedKey').get('dataid'))
        else :
            return (data.get('Items'), None)

def fetch_total_url_points(urlid):
    data = table.scan(
        FilterExpression=Attr('urlid').eq(urlid),
        Select='COUNT'
    )
    if data:
        return data.get('Count')