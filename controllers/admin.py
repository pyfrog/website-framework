from flask import Blueprint, flash, redirect, render_template, \
     request, url_for
from flask_httpauth import HTTPDigestAuth

from models.categories import *
from models.products import *

admin = Blueprint('admin', __name__, 
  template_folder='./templates',
  static_folder='./static')

users = {
  "admin": "pass",
  "local": "secret"
}

auth = HTTPDigestAuth()

@auth.get_password
def get_pw(username):
  if username in users:
    return users.get(username)
  return None

@admin.route('/', methods=['GET'])
@auth.login_required
def index():
  return render_template('admin/index.html')

@admin.route('/homepage')
@auth.login_required
def homepage():
  return render_template('admin/homepage.html')

@admin.route('/categories', methods=['GET'])
@auth.login_required
def categories():
  return

@admin.route('/category/add', methods=['GET', 'POST'])
@auth.login_required
def category_add():
  form = CategoryForm(request.form)
  if request.method == 'POST':
    Categories(
      name = form.name.data,
      code = form.code.data,
      description = form.description.data,
      image = form.image.data
    ).save()
    flash(u'New Category Added', 'success')
  return render_template('admin/add_category.html', form=form)

@admin.route('/subcategory/add', methods=['GET', 'POST'])
@auth.login_required
def subcategory_add():
  form = SubCategoryForm(request.form)
  if request.method == 'POST':
    SubCategories(
      name = form.name.data,
      code = form.code.data,
      description = form.description.data,
      image = form.image.data
    ).save()
    flash(u'New Sub-Category Added', 'success')
  return render_template('admin/add_sub_category.html', form=form)

@admin.route('/products', methods=['GET'])
@auth.login_required
def products():
  return

@admin.route('/product/add', methods=['GET', 'POST'])
@auth.login_required
def product_add():
  form = ProductForm(request.form)
  if request.method == 'POST':
    Categories(
      name = form.name.data,
      code = form.code.data,
      category = form.category.data,
      short_description = form.short_description.data,
      description = form.description.data,
      image = form.image.data,
      thumbnail = form.thumbnail.data
    ).save()
    flash(u'New Product Added', 'success')
  return render_template('admin/add_product.html', form=form)