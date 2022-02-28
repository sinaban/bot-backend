from werkzeug.security import safe_str_cmp
from models.user import UserModel


def authenticate(username, password):
    """
        Register to the Bot
        return Acces token
        ---
        parameters:
          - in: path
            name: username
            type: string
            required: true
          - in: path
            name: password
            type: string
            required: true
        responses:
          200:
            description: A single user item
            schema:
              id: User
              properties:
                username:
                  type: string
                  description: The name of the user
                  default: Steven Wilson
    """
    user = UserModel.find_by_username(username)
    if user and safe_str_cmp(user.password, password):
        return user 


def identity(payload):
    user_id = payload['identity']
    return UserModel.find_by_id(user_id) , 200 , { 'Access-Control-Allow-Origin': "http://localhost:8080", \
      'Access-Control-Allow-Methods' : 'PUT,GET,POST' }
