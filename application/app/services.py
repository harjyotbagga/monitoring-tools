from faker import Faker
from models import User

fake = Faker()


def generateFakeUser():
    name = fake.name()
    age = fake.random_int(min=18, max=80)
    address = fake.address()
    latitude = fake.latitude()
    longitude = fake.longitude()
    phone_number = fake.phone_number()
    email = fake.email()
    country = fake.country()
    return User(
        name,
        age,
        address,
        latitude,
        longitude,
        phone_number,
        email,
        country)
