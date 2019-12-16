import os

def init(app):
  return {
    'app': {
      'key': 'I-AM-NOT-A-KEY',
      'db': os.path.join(app.instance_path, 'test-app.sqlite')
    },
    'map': {
      'key': 'I-AM-NOT-A-KEY'
    }
  }