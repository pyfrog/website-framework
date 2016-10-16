import os
from flask import Flask
from flask_mongoengine import MongoEngine
from flask_bootstrap import Bootstrap

from controllers.main import main
from controllers.admin import admin


app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])

db = MongoEngine(app)

Bootstrap(app)

app.register_blueprint(main, url_prefix='/')
app.register_blueprint(admin, url_prefix='/admin')


if __name__ == '__main__':
  app.run()