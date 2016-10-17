import os
import time

from flask import url_for, redirect, request, render_template, make_response, abort, jsonify

from server.views import user
from server.views.validators import validator
from .database import app, cursor

app.register_blueprint(user.mod)

@app.route('/')
def hello_world():
    return render_template('Hello.html')


@app.route("/hello/<path>")
def myfunc(path):
    return path + "value"


@app.route("/hello/<path>/<userId>")
def myCustomFunc(path, userId):
    return path + "   " + userId + "  value"


@app.route("/admin")
def login():
    return "you are admin"


@app.route("/user/<username>")
def user(username):
    return username


@app.route("/access/<type>")
def handleLogin(type):
    if type.lower() == "admin":
        return redirect(url_for('login'))
    else:
        return redirect(url_for('user', username=type))


@app.route("/file", methods=['POST'])
def register():
    if validator.validateReg(request.form['username'], request.form['password']):
        uploadedFile = request.files['file']
        print(uploadedFile.filename)
        if validator.validateFile(uploadedFile.filename):
            APP_ROOT = os.path.dirname(os.path.abspath(__file__))
            UPLOAD_FOLDER = os.path.join(APP_ROOT, 'uploads/')
            uploadedFile.save(UPLOAD_FOLDER + str(int(time.time())) + "." + server.utils.file_utils.getFileExt(uploadedFile.filename))
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


@app.route('/users')
def users():
    return getUsers()


def getUsers():
    cursor.execute("select name,email from user")
    data = cursor.fetchall()
    response = {}
    list = []
    for s in data:
        aDict = {}
        aDict['name'] = s[0]
        aDict['email'] = s[1]
        list.append(aDict)
    return jsonify(data=list)


def error_response(error):
    response = make_response()
    response = jsonify({'status': error.code, 'message': error.description})
    response.status_code = error.code
    return response