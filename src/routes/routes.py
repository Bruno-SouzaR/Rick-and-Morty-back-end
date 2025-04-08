from flask import Blueprint, request
from src.controllers.character_controller import CharacterController

character_bp = Blueprint('character_bp', __name__)
character_controller = CharacterController()

@character_bp.route('/', methods=['GET'])
def get_characters():
    filters = request.args.to_dict()
    return character_controller.get_all_characters(filters)

@character_bp.route('/<int:id>', methods=['GET'])
def get_character(id):
    return character_controller.get_character(id)



bp = Blueprint('routes', __name__)

bp.register_blueprint(character_bp, url_prefix='/character')