from pymongo import UpdateOne, InsertOne, UpdateMany
from database import DATABASE_NAME
from database import get_mongo_client

class User():
    def __init__(self, name, age, address, latitude, longitude, phone_number, email, country):
        self.name = name
        self.age = int(age)
        self.address = address.replace("\n", " ")
        self.coordinates = [float(latitude), float(longitude)]
        self.phone_number = phone_number
        self.email = email
        self.country = country
    def getName(self):
        return self.name
    def getAge(self):
        return self.age
    def getAddress(self):
        return self.address
    def getCoordinates(self):
        return self.coordinates
    def getPhoneNumber(self):
        return self.phone_number
    def getEmail(self):
        return self.email
    def getCountry(self):
        return self.country

    def addUserToDatabase(self):
        try:
            db_instance = get_mongo_client()[DATABASE_NAME]
            user_info_collection = db_instance["UserInfo"]
            user_info = {
                "name": self.name,
                "age": self.age,
                "address": self.address,
                "coordinates": {
                    "latitude": self.coordinates[0],
                    "longitude": self.coordinates[1]
                },
                "phone_number": self.phone_number,
                "email": self.email,
                "country": self.country
            }
            
            res = user_info_collection.update_one({
                "name": self.name,
                "email": self.email,
                "phone_number": self.phone_number
            }, {"$setOnInsert": user_info}, upsert=True)
            return "User Upserted Succesfully"
        except Exception as e:
            raise e

    def __repr__(self) -> str:
        return "User(name, age, address, latitude, longitude, phone_number, email, country)"
    def __str__(self) -> str:
        return f"USER: {self.name}"
