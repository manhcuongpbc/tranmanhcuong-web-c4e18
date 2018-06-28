from models.customer import Customer
import mlab
from faker import Faker
from random import randint, choice

mlab.connect()

fake = Faker()

for i in range(50):
    print(i+1)
    new_Customer = Customer(
        name = fake.name(),
        gender = randint(0,1),
        phone = fake.phone_number(),
        address = fake.address(),
    )

    new_Customer.save()
