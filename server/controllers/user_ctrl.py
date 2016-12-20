from server.models.user import User



def create_user(request):
    response = {}
    if 'first_name' not in request or request['first_name'] is '':
        response['status'] = 400
        response['message'] = "first_name is required"
        return response

    if 'last_name' not in request or request['last_name'] is '':
        response['status'] = 400
        response['message'] = "last_name is required"
        return response

    if 'email' not in request or request['email'] is '':
        response['status'] = 400
        response['message'] = "email is required"
        return response

    if 'mobile' not in request or request['mobile'] is '':
        response['status'] = 400
        response['message'] = "mobile is required"
        return response

    if 'gender' not in request or request['gender'] is '':
        response['status'] = 400
        response['message'] = "gender is required"
        return response

    if 'device_type' not in request or request['device_type'] is '':
        response['status'] = 400
        response['message'] = "device is required"
        return response

    if 'social_id' not in request or request['social_id'] is '':
        if 'password' not in request or request['password'] is '':
            response['status'] = 400
            response['message'] = "password is required"
            return response

    return User.create_user(request)
