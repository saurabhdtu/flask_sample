from flask import Blueprint, request, jsonify, abort
from server.controllers import user_ctrl

mod = Blueprint('user', __name__, url_prefix='/user')


@mod.route('/login', methods=['POST'])
def login():
    return jsonify({'message': 'User Created Successfully',
                    'status': 200})


@mod.route('/register', methods=['POST'])
def register():
    data = user_ctrl.create_user(request.form)
    if data['status'] is not 200:
        abort(data['status'], data['message'])
    else:
        return jsonify(data['message'])
