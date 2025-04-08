from src.repositories.character_repository import CharacterRepository
from src.models.character_model import character_output, characters_output
from werkzeug.exceptions import NotFound

class CharacterService:

    def __init__(self):
        self.character_repository = CharacterRepository()
        
    def get_all_characters(self, filters):

        name = filters.get('name', None)
        page = int(filters.get('page', 1))
                        
        result = self.character_repository.get_all_characters(name, page)
        
        data = characters_output.dump(result["items"])

        return data, {
            "meta": {
                "page": result["page"],
                "total": result["total"],
                "pages": result["pages"],
                "per_page":result["per_page"]
            }
        }   
  
    def get_character(self, id):

        character = self.character_repository.get_character(id)

        if not character:
            raise NotFound
        
        data = character_output.dump(character)

        return data