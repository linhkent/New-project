import mongoengine

# mongodb://<dbuser>:<dbpassword>@ds133865.mlab.com:33865/c4e25-hw-web2

host = "ds133865.mlab.com"
port = 33865
db_name = "c4e25-hw-web2"
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