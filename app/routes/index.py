from flask import Blueprint, request, jsonify
import json

bp = Blueprint('index', __name__)

@bp.route('/', methods=['GET', 'POST'])
def index():
    return jsonify({
      'ip': request.remote_addr,
      'method': request.method,
      'path': request.path,
      'post_params': request.json if request.is_json else request.form,
      'get_params': request.args
    })