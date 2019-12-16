import os
import importlib

ENV = os.environ.get('FLASK_ENV')

if ENV is None:
    ENV = 'development'

def load(app):
  config = importlib.import_module(f'config.env.{ENV}')

  return config.init(app)
