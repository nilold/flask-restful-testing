from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.user import UserModel


class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!")
    parser.add_argument('password',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!")

    def post(self):
        data = self.parser.parse_args()
        if UserModel.find_by_username(data['username']):
            return {'message': f"An user with username '{data['username']}' already exists."}, 400

        user = UserModel(**data)

        try:
            user.save_to_db()
        except:
            return {"message": "An error occurred inserting the user."}, 500

        return user.json(), 201

    # def put(self, username):
    #     data = self.parser.parse_args()
    #
    #     user = UserModel.find_by_name(username)
    #
    #     if user is None:
    #         user = UserModel(**data)
    #     else:
    #         user.password = data["password"]
    #
    #     user.save_to_db()
    #
    #     return user.json(), 200


class UserLogin(Resource):
    @jwt_required()
    def get(self, username):
        user = UserModel.find_by_username(username)
        if user:
            return user.json()

        return {"msg": "User not found"}, 404
