class User():
    def __init__(self, name, age, address, latitude, longitude, phone_number, email, country):
        self.name = name
        self.age = age
        self.address = address
        self.coordinates = [latitude, longitude]
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


    def __repr__(self) -> str:
        return "User(name, age, address, latitude, longitude, phone_number, email, country)"
    def __str__(self) -> str:
        return f"USER: {self.name}"