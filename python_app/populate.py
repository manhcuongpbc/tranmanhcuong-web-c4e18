from models.service import Service
import mlab
from faker import Faker
from random import randint, choice

mlab.connect()

fake = Faker()

# print(fake.name())
for i in range(50):
    print(i+1)
    new_service = Service(
        name=fake.name(),
        yob = randint(1990,2000),
        gender = randint(0,1),
        height = randint(155,190),
        phone= fake.phone_number(),
        address= fake.address(),
        status= choice([True, False]),
        description = 'Học giỏi, ngoan hiền',
        measurements = [90,80,90],
        image = 'D:\C4E18\WebModule\python_app\static\image\hand.jpg'
    )

    new_service.save()
