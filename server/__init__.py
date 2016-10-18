import os
import time

from flask import url_for, redirect, request, render_template, make_response, abort, jsonify

from server.views import user
from server.utils import file_utils
from server.views.validators import validator
from .database import app, cursor

app.register_blueprint(user.mod)

@app.route('/', defaults={'name': 'Saurabh'})
@app.route('/<name>')
def hello_world(name):
    return render_template('Hello.html', name=name)

@app.route("/file", methods=['POST'])
def register():
    if validator.validateReg(request.form['username'], request.form['password']):
        uploadedFile = request.files['file']
        print(uploadedFile.filename)
        if validator.validateFile(uploadedFile.filename):
            APP_ROOT = os.path.dirname(os.path.abspath(__file__))
            UPLOAD_FOLDER = os.path.join(APP_ROOT, 'uploads/')
            uploadedFile.save(UPLOAD_FOLDER + str(int(time.time())) + "." + file_utils.getFileExt(uploadedFile.filename))
            make_response()
            return "success"
        else:
            "error"
    else:
        "error"

@app.errorhandler(404)
def pageNotFound(error):
    return error_response(error)


@app.errorhandler(401)
def pageNotFound(error):
    return error_response(error)

@app.errorhandler(403)
def pageNotFound(error):
    return error_response(error)


@app.errorhandler(500)
def pageNotFound(error):
    return error_response(error)

@app.errorhandler(400)
def pageNotFound(error):
    return error_response(error)


@app.route('/abort')
def killed():
    abort(401)

@app.route('/redirect')
def redir():
    return redirect(url_for('killed'))


def error_response(error):
    response = make_response()
    response = jsonify({'status': error.code, 'message': error.description})
    response.status_code = error.code
    return response