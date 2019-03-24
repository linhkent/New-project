from mongoengine import Document, StringField # co nhieu kieu import kieu du lieu vd IntField FloadtField hay FileField

class Food(Document):
    title = StringField()
    link = StringField()