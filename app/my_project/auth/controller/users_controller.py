from flask import Blueprint, request, jsonify
from ..services.users_service import UsersService

def create_users_controller(mysql):
    users_controller = Blueprint('user', __name__)
    service = UsersService(mysql)

    @users_controller.route('/users', methods=['GET'])
    def get_users():
        """
        Get a list of users
        ---
        responses:
          200:
            description: list of all users
            examples:
              application/json: [{"id": 1, "name": "Maria"}]
        """
        users = service.get_users()
        return jsonify(users)
    
    # @users_controller.route('/users', methods=['POST'])
    # def create_users():
    #     data = request.json
    #     if not data or 'access_id' not in data or 'username' not in data or 'email' not in data:
    #         return jsonify({"error": "Invalid data"}), 400

    #     try:
    #         service.add_users(data)
    #         return jsonify({"message": "User created"}), 201
    #     except Exception as e:
    #         return jsonify({"error": str(e)}), 500
        
    @users_controller.route('/users/<int:user_id>', methods=['PUT'])
    def update_users(user_id):
        """
        Update user information
        ---
        parameters:
          - name: user_id
            in: path
            type: integer
            required: true
            description: The ID of the user to update
          - name: body
            in: body
            required: true
            schema:
              type: object
              properties:
                username:
                  type: string
                email:
                  type: string
        responses:
          200:
            description: User updated successfully
            examples:
              application/json: {"message": "User updated"}
          400:
            description: Invalid input data
          500:
            description: Internal server error
        """
        data = request.json
        if not data or 'username' not in data or 'email' not in data:
            return jsonify({"error": "Invalid data"}), 400
        try:
            service.modify_users(user_id, data)
            return jsonify({"message": "User updated"})
        except Exception as e:
            return jsonify({"error": str(e)}), 500
        
    @users_controller.route('/users/<int:user_id>', methods=['DELETE'])
    def delete_users(user_id):
        """
        Delete a user by ID
        ---
        parameters:
          - name: user_id
            in: path
            type: integer
            required: true
            description: The ID of the user to delete
        responses:
          200:
            description: User deleted successfully
            examples:
              application/json: {"message": "User deleted"}
          500:
            description: Internal server error
        """
        try:
            service.remove_users(user_id)
            return jsonify({"message": "User deleted"})
        except Exception as e:
            return jsonify({"error": str(e)}), 500
        
    @users_controller.route('/users/<int:user_id>/threshold', methods=['GET'])
    def get_users_with_threshold(user_id):
        try:
            user_with_threshold = service.get_users_with_threshold(user_id)
            return jsonify(user_with_threshold)
        except Exception as e:
            return jsonify({"error": str(e)}), 500
        
    @users_controller.route('/users', methods=['POST'])
    def create_user():
        data = request.json
        if not data or 'user_id' not in data or 'access_id' not in data or 'username' not in data or 'email' not in data:
            return jsonify({"error": "Invalid data"}), 400

        try:
            service.add_user(data)
            return jsonify({"message": "User created"}), 201
        except Exception as e:
            return jsonify({"error": str(e)}), 500
        
    @users_controller.route('/users/batch', methods=['POST'])
    def insert_noname_users_batch():
        try:
            service.insert_noname_users_batch()
            return jsonify({"message": "Batch users inserted successfully"}), 201
        except Exception as e:
            return jsonify({"error": str(e)}), 500
        

    return users_controller

