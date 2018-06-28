from models.service import Service
import mlab

mlab.connect()

# all_service = Service.objects()
# first_service = all_service[0]

# print(first_service.name)

id_to_find = "5b2ba8f9250f4217644467cc"
# service = Service.objects.get(id=id_to_find)

service = Service.objects.with_id(id_to_find)

if service is not None:
    # service.delete()
    print(service.yob)
    service.update(set__yob=1893)
    service.reload()
    print(service.yob)
else:
    print("service not found")
# print(service.to_mongo())
