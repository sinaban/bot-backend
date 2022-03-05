import sqlite3
from flask_restful import Resource, reqparse
from models.user import UserModel
from flask_jwt import jwt_required


class UserRegister(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('username',
        type=str,
        required=True,
        help="This field cannot be blank."
    )
    parser.add_argument('password',
        type=str,
        required=True,
        help="This field cannot be blank."
    )

    def post(self):
        data = UserRegister.parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return {"message": "A user with that username already exists"}, 400

        user = UserModel(**data)
        user.save_to_db()

        return {"message": "User created successfully."}, 201

class ReturnUser(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
        type=str,
        required=True,
        help="This field cannot be blank."
    )
    parser.add_argument('password',
        type=str,
        required=True,
        help="This field cannot be blank."
    ) 

    # @jwt_required()
    def post(self):
                """
        check username and pass
        ---
        tags:
        - exchange data
        parameters:
          - in: path
            name: username
            type: string
            required: true
          - in: path
            name: passwword
            type: string
            required: true
        responses:
          200:

                  

        """
        data = ReturnUser.parser.parse_args()

        if  UserModel.find_by_username(data['username']):
            return {"username": data['username']}, 200

        return {"user": "User not found"}, 400   
