from mongoengine import *
# 1. Design Database
class Customer(Document):
    name = StringField()
    gender = IntField()
    phone = StringField()
    address = StringField()
    email = StringField()
    job = StringField()
    company = StringField()
