from src.models import db, ma
from marshmallow import fields

class Character(db.Model):
    __tablename__ = 'characters'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    status = db.Column(db.String(50))
    species = db.Column(db.String(50))
    type = db.Column(db.String(50), nullable=True)
    gender = db.Column(db.String(30))
    image = db.Column(db.String(120))

    origin_id = db.Column(db.Integer, db.ForeignKey('locations.id'),nullable=True)
    location_id = db.Column(db.Integer, db.ForeignKey('locations.id'),nullable=True)

    origin = db.relationship('Location', foreign_keys=[origin_id], uselist=False, lazy=True, back_populates='character_origin')
    location = db.relationship('Location', foreign_keys=[location_id], uselist=False, lazy=True, back_populates='character_location')
    episodes = db.relationship('Episode', secondary='character_episode', back_populates='characters')

    def __repr__(self):
        return f"<Character {self.name}>" 

class CharactersOutput(ma.Schema):
    id = ma.Integer()
    name = ma.String()
    status = ma.String()
    species = ma.String()
    image = ma.String()
    
characters_output = CharactersOutput(many=True) 

class CharacterOutput(CharactersOutput):
    gender = ma.String()
    origin = ma.Nested('LocationOutput', allow_none=True)
    location = ma.Nested('LocationOutput', allow_none=True)
    latest_air_date = ma.Function(lambda obj: obj.episodes[-1].air_date if obj.episodes else None)
    
character_output = CharacterOutput()