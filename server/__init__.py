import os
import time

from flask import Flask, request
from flask import make_response, jsonify

from server.utils import utils
from server.validators import validator
from server.views import user
from server.database import init_mysql

app = Flask(__name__)
init_mysql(app)
# app.config.from_object('config')

app.register_blueprint(user.mod)



@app.route("/file", methods=['POST'])
def register():
    if validator.validate_reg(request.form['username'], request.form['password']):
        uploadedFile = request.files['file']
        print(uploadedFile.filename)
        if validator.validate_file(uploadedFile.filename):
            APP_ROOT = os.path.dirname(os.path.abspath(__file__))
            UPLOAD_FOLDER = os.path.join(APP_ROOT, 'uploads/')
            uploadedFile.save(
                UPLOAD_FOLDER + str(int(time.time())) + "." + utils.getFileExt(uploadedFile.filename))
            make_response()
            return "success"
        else:
            "error"
    else:
        "error"


@app.errorhandler(404)
def page_not_found(error):
    return error_response(error)


@app.errorhandler(401)
def unauthorized(error):
    return error_response(error)


@app.errorhandler(403)
def forbidden(error):
    return error_response(error)


@app.errorhandler(500)
def internal_server_error(error):
    app.logger.exception(error)
    return error_response(error)


@app.errorhandler(400)
def bad_request(error):
    return error_response(error)


@app.errorhandler(405)
def wrong_method(error):
    return jsonify({'status': 'error', 'message': 'Wrong HTTP method used'}), 405


def error_response(error):
    response = make_response()
    response = jsonify({'status': error.code, 'message': error.description})
    response.status_code = error.code
    return response
