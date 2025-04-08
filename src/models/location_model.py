from src.models import db, ma

class Location(db.Model):
    __tablename__ = 'locations'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    type = db.Column(db.String(50))
    dimension = db.Column(db.String(50))

    character_origin = db.relationship('Character', foreign_keys='Character.origin_id', uselist=True, lazy=True, back_populates='origin')
    character_location = db.relationship('Character', foreign_keys='Character.location_id', uselist=True, lazy=True, back_populates='location')

class LocationOutput(ma.Schema):
    id = ma.Integer()
    name = ma.String()
    type = ma.String()
    dimension = ma.String()
    residents_count = ma.Method('count_residents')

    def count_residents(self, obj):
        return len(obj.character_location)