import os

def get(app):
  return {
    'key': 'dev',
    'db': os.path.join(app.instance_path, 'test-app.sqlite')
  }