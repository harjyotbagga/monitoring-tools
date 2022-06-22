from pymongo import UpdateOne, InsertOne, UpdateMany
from database import DATABASE_NAME
from database import get_mongo_client
import logging
import os
import sys

LOGGING_URL = os.getenv("LOGGING_URL", "http://localhost:9880/")
HTTP_LOGGING = os.getenv("HTTP_LOGGING", False)

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

class ApplicationLogger():
    def __init__(self, logger_name, logging_endpoint, logging_level=logging.INFO):
        self.logger_name = logger_name
        self.logging_level = logging_level
        self.logger = logging.getLogger(logger_name)
        self.logger.setLevel(logging_level)
        
        if HTTP_LOGGING == "True" or HTTP_LOGGING == True:
            http_handler = logging.handlers.HTTPHandler(
                LOGGING_URL,
                logging_endpoint,
                method='POST',
            )
            self.logger.addHandler(http_handler)
        else:
            stream_handler = logging.StreamHandler(sys.stdout)
            self.logger.addHandler(stream_handler)

    def debug(self, message):
        self.logger.debug(message)
    def info(self, message):
        self.logger.info(message)
    def warning(self, message):
        self.logger.warning(message)
    def error(self, message):
        self.logger.error(message)

    def __repr__(self) -> str:
        return f"ApplicationLogger: {self.logger_name}"
    def __str__(self) -> str:
        return f"ApplicationLogger({self.logger_name}, {self.logging_level})"