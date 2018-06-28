import mongoengine

# mongodb://manhcuong:159357456258CCC@ds163610.mlab.com:63610/muadong-c4e

host = "ds163610.mlab.com"
port = 63610
db_name = "muadong-c4e"
user_name = "manhcuong"
password = "159357456258CCC"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())