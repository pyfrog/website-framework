""" Database model Categories class """

from flask_mongoengine import MongoEngine
from flask_mongoengine.wtf import model_form
from base import BaseDocument

db = MongoEngine()

class Categories(BaseDocument):
  name = db.StringField(max_length=50, required=True)
  code = db.StringField(max_length=10, required=True)
  description = db.StringField(max_length=500, required=True)
  image = db.URLField()

  def to_cutsom_json(self):
    """Return data in JSON format"""
    json_data = {
      "image":self.image,
      "name":self.name,
      "code":self.code,
      "description":self.description
    }
    return json_data

class SubCategories(BaseDocument):
  name = db.StringField(max_length=50, required=True)
  code = db.StringField(max_length=10, required=True)
  parent = db.ReferenceField(Categories)
  description = db.StringField(max_length=500, required=True)
  image = db.URLField()

  def to_cutsom_json(self):
    """Return data in JSON format"""
    json_data = {
      "image":self.image,
      "name":self.name,
      "code":self.code,
      "parent_code":self.parent.code,
      "description":self.description
    }
    return json_data

category_fied_args = {
  'name': {
    'textarea': False
    },
  'description': {'textarea': True}
}
CategoryForm = model_form(Categories, field_args=category_fied_args)
SubCategoryForm = model_form(SubCategories, field_args={'description': {'textarea': True}})