from server.database import db_connect, db_disconnect


class User:
    __TABLE_NAME = "users"
    __TRACKED_FIELDS = {"first_name", "last_name", ""}

    def __init__(self, uid):
        for field in self.__TRACKED_FIELDS:
            setattr(self, field, None)

    @staticmethod
    def create_user(request):
        conn = db_connect()
        cursor = conn.cursor()
        cursor.execute("SELECT email from users WHERE email = %s OR mobile = %s",
                       [request['email'], request['mobile']])
        if cursor.rowcount > 0:
            return {'status': 400, 'message': 'User Already Exists'}
        else:
            if 'social_id' not in request:
                cursor.execute(
                    "insert into users (first_name, last_name, email, mobile, gender, password, device_type)"
                    " values (%s, %s, %s, %s, %s, %s, %s)",
                    [request['first_name'], request['last_name'], request['email'],
                     request['mobile'], request['gender'], request['password'], request['device_type']])
                cursor.execute('SELECT LAST_INSERT_ID()')
            else:
                cursor.execute(
                    "insert into users (first_name, last_name, email, mobile, gender, social_id, device_type)"
                    " values (%s, %s, %s, %s, %s, %s, %s)",
                    [request['first_name'], request['last_name'], request['email'],
                     request['mobile'], request['gender'], request['social_id'],
                     request['device_type']])
                cursor.execute('SELECT LAST_INSERT_ID()')
            db_disconnect(cursor)
            data = {'message': "User Created Successfully",
                    'data': {'id': cursor.fetchone()[0], 'first_name': request['first_name']}
                    }
            conn.commit()
            return {'status': 200, 'message': data}
