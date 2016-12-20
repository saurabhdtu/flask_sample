def validate_reg(request):
    if request.form['email'] and request.form['password'] and request.form['name']:
        return
    else:
        return "Bad Request"


def validate_file(filename):
    if filename.rfind(".") == -1:
        return False
    elif filename.endswith("pdf") or filename.endswith("png") or filename.endswith("jpg"):
        return True
    else:
        return False
