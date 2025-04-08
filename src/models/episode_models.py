from src.models import db

class Episode(db.Model):
    __tablename__ = 'episodes'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    air_date = db.Column(db.String(30))
    episode = db.Column(db.String(20), unique=True, nullable=False)

    characters = db.relationship('Character', secondary='character_episode', back_populates='episodes')