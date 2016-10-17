def validateReg(request):
    if request.form['email'] and request.form['password'] and request.form['name']:
        return
    else:
        return "Bad Request"

def validateFile(fileName):
    if fileName.rfind(".") == -1:
        return False
    elif fileName.endswith("pdf") or fileName.endswith("png") or fileName.endswith("jpg"):
        return True
    else:
        return False