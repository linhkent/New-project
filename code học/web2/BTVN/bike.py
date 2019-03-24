from mongoengine import Document, StringField, IntField

class Bike(Document):
    model = StringField()
    daily_fee = IntField()
    image = StringField()
    year = IntField()