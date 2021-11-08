from tracer.datastore import users
from tracer import validations

def check_if_uuid_exists(uuid):
    return users.check_uuid_exists(uuid)

def create_new_user(name, email):
    if not validations.email(email):
        return None
    return users.add_user(name, email)

def get_user_details(email):
    return users.get_user(email)