from src.models import db


class CharacterEpisode(db.Model):
    __tablename__ = 'character_episode'
    
    character_id = db.Column(db.Integer, db.ForeignKey('characters.id'), primary_key=True)
    episode_id = db.Column(db.Integer, db.ForeignKey('episodes.id'), primary_key=True)