from mongoengine import *
# 1. Design Database
class Service(Document):
    name = StringField()
    yob = IntField()
    gender = IntField()
    height = IntField()
    phone = StringField()
    address = StringField()
    status = BooleanField()
    description = StringField()
    measurements = ListField()
    image = ImageField()
    
# new_service = Service(
#     name = "Le van luyen",
#     yob = 1992,
#     gender = 0,
#     height = 165,
#     phone = '01453456789',
#     address = 'Gaigon',
#     status = True
# )

# new_service.save()