from flask import Flask
from src.models import db, ma
from config.settings import DATABASE_URI, environment, front_end_url
from src.routes.routes import bp as routes_bp
from flask_cors import CORS
from src.utils.constants import ENVIRONMENT

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

origins_map = {
    ENVIRONMENT.LOCAL.value: ['*'],
    ENVIRONMENT.PRODUCTION.value: [front_end_url]
}

allowed_origin = origins_map.get(environment, origins_map[ENVIRONMENT.PRODUCTION.value])

CORS(app, origins=allowed_origin,
     supports_credentials=True,
     allow_headers=["Content-Type", "Authorization", "Accept"],
     methods=["GET"])

db.init_app(app)
ma.init_app(app)

app.register_blueprint(routes_bp)

if __name__ == "__main__":
    app.run(debug=True)