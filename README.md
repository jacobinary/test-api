# Test API

## Installation

Run `pip install -e .`.

## Development

Under `config/env`, create a `development.py` file with the following contents, replacing any keys with appropriate values.

[example.py](config/env/example.py):
```py
import os

def init(app):
  return {
    'secret': {
      'key': 'I-AM-NOT-A-KEY',
      'db': os.path.join(app.instance_path, 'test-app.sqlite')
    },
    'map': {
      'key': 'I-AM-NOT-A-KEY'
    }
  }
```