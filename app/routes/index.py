from flask import Blueprint, request, render_template, url_for
from app import config

bp = Blueprint('index', __name__)

@bp.route('/', methods=['GET', 'POST'])
def index():
  return render_template('index.html',
    config = {
      'key': config['map']['key']
    },
    info = {
      'ip': request.remote_addr,
      'method': request.method,
      'path': request.path,
      'post_params': request.json if request.is_json else request.form,
      'get_params': request.args
    }
  )