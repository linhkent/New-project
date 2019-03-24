import mongoengine

# mongodb://<dbuser>:<dbpassword>@ds113855.mlab.com:13855/c4e25-web

host = "ds113855.mlab.com"
port = 13855
db_name = "c4e25-web"
user_name = "admin"
password = "admin1"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())