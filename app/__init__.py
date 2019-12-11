import os
import importlib

from flask import Flask

ENV = os.environ.get('FLASK_ENV')

if ENV is None:
    ENV = 'development'

config = importlib.import_module(f'config.{ENV}')

# create and configure the app
app = Flask(__name__, instance_relative_config=True)

conf = config.get(app)
app.config.from_mapping(
    SECRET_KEY=conf['key'],
    DATABASE=conf['db']
)

# ensure the instance folder exists
try:
    os.makedirs(app.instance_path)
except OSError:
    pass

from app.routes import index
app.register_blueprint(index.bp)
app.add_url_rule('/', endpoint='index') 