from flask import Blueprint, request, jsonify
from services.corridors_service import CorridorsService

def create_corridors_controller(mysql):
    corridors_controller = Blueprint('corridors', __name__)
    service = CorridorsService(mysql)

    @corridors_controller.route('/corridors', methods=['GET'])
    def get_corridors():
        corridors = service.get_corridors()
        return jsonify([corridor.to_dict() for corridor in corridors])

    @corridors_controller.route('/corridors', methods=['POST'])
    def create_corridors():
        data = request.json
        if not data or 'corridor_id' not in data or 'object_id' not in data or 'name' not in data:
            return jsonify({"error": "Invalid data"}), 400

        try:
            service.add_corridors(data)
            return jsonify({"message": "Corridors created"}), 201
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @corridors_controller.route('/corridors/<int:corridor_id>', methods=['PUT'])
    def update_corridors(corridor_id):
        data = request.json
        if not data or 'object_id' not in data or 'name' not in data:
            return jsonify({"error": "Invalid data"}), 400

        try:
            service.modify_corridors(corridor_id, data)
            return jsonify({"message": "Corridors updated"})
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @corridors_controller.route('/corridors/<int:corridor_id>', methods=['DELETE'])
    def delete_corridors(corridor_id):
        try:
            service.remove_corridors(corridor_id)
            return jsonify({"message": "Corridors deleted"})
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    return corridors_controller
