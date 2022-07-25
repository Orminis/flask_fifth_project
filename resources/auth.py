from flask import request
from flask_restful import Resource

from managers.complainer import ComplainerManager
from models.user import ComplainerModel


class RegisterResource(Resource):
    # TODO: validation of data
    def post(self):
        data = request.get_json()
        token = ComplainerManager.register(data)
        return {"token": token}, 201


class LoginResource(Resource):
    def post(self):
        data = request.get_json()
        user = ComplainerModel(**data)
        return user
