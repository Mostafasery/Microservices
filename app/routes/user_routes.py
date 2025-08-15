from flask import Blueprint, jsonify
from app.services.user_service import UserService

user_blueprint = Blueprint('user_blueprint', __name__)
user_service = UserService()

@user_blueprint.route('/users', methods=['GET'])
def get_users():
    users = user_service.get_users()
    return jsonify(users), 200

@user_blueprint.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = user_service.get_user_by_id(user_id)
    if user:
        return jsonify(user), 200
    else:
        return jsonify({"message": "User not found"}), 404
