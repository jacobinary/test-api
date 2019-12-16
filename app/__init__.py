import os
import config

from flask import Flask

# create and configure the app
app = Flask(__name__, instance_relative_config=True)

config = config.load(app)

app.config.from_mapping(
    SECRET_KEY=config['app']['key'],
    DATABASE=config['app']['db']
)

# ensure the instance folder exists
try:
    os.makedirs(app.instance_path)
except OSError:
    pass

from app.routes import index
app.register_blueprint(index.bp)
app.add_url_rule('/', endpoint='index') 