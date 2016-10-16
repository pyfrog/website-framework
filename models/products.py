""" Database model Products class """

from flask_mongoengine import MongoEngine
from flask_mongoengine.wtf import model_form
from base import BaseDocument

from categories import *

db = MongoEngine()

class Products(BaseDocument):
  name = db.StringField()
  code = db.IntField()
  category = db.ReferenceField(Categories)
  short_description = db.StringField()
  description = db.StringField()
  image = db.URLField()
  thumbnail = db.URLField()

  def to_cutsom_json(self):
    """Return data in JSON format"""
    json_data = {
      "image":self.image,
      "name":self.name,
      "code":self.code,
      "short_description":self.short_description,
      "description":self.description
    }
    return json_data

CategoryForm = model_form(
    Categories, 
    field_args={
      'description': {'textarea': True}, 
      'short_description': {'textarea': True}
    })