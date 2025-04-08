from src.models import db
from src.models.character_model import Character

class CharacterRepository:
    
    def get_all_characters(self, name, page):
        try:
            per_page = 20
            query = Character.query
            
            if name:
                query = query.filter(Character.name.ilike(f"%{name}%"))
                
            pagination = query.paginate(page=page, per_page=per_page, error_out=False)
            characters = pagination.items
            
            return {
                "items": characters,
                "total": pagination.total,
                "pages": pagination.pages,
                "page": pagination.page,
                "per_page": per_page
            }
        except Exception:
            db.session.rollback()
            raise 

    def get_character(self, id):
        try: 
            character = db.session.get(Character, id)
            return character
        except Exception:
            db.session.rollback()
            raise