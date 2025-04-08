from src.services.character_service import CharacterService
from src.utils.api_response import ApiReponse
from werkzeug.exceptions import NotFound

class CharacterController:

    def __init__(self):
        self.character_service = CharacterService()

    def get_all_characters(self, filters):
        try:
            data = self.character_service.get_all_characters(filters)
            return ApiReponse.response(success=True, data=data, message= "Personagens recuperados com sucesso", status_code=200)
        except Exception as e:
            return ApiReponse.response(success=False,data=None, message="Erro ao buscar personagens", status_code=500)

    def get_character(self, id):
        try:
            data = self.character_service.get_character(id)   
            return ApiReponse.response(success=True, data=data, message="Personagem encontrado com sucesso", status_code=200)
        except NotFound:
            return ApiReponse.response(success=False, data=None, message="Personagem não encontrado", status_code=404)
        except Exception:
            return ApiReponse.response(success=False, data=None, message="Erro ao buscar personagem", status_code=500)