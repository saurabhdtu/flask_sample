from flask import Blueprint, request, jsonify, render_template, abort

from .validators.validator import validateReg
from ..database import cursor, connection

mod = Blueprint('user', __name__, url_prefix='/user')


@mod.route('/login', methods=['POST'])
def login():
    return jsonify({'message': 'User Created Successfully',
                    'status': 200})



@mod.route('/register', methods=['POST'])
def register():
    message = validateReg(request)
    if message is None:
        return processReg(request)
    else:
        abort(400, message)


def processReg(request):
    cursor.execute("SELECT email from user")
    cursor.execute("SELECT email from user WHERE email = %s", request.form['email'])
    if cursor.rowcount > 0:
        abort(403, 'User Already Exists')
    else:
        cursor.execute("insert into user (name, email, password) values (%s, %s, %s)", [request.form['name'], request.form['email'], request.form['password']])
        connection.commit()
        return jsonify({"status": 200, "message": "User Created Successfully"})
