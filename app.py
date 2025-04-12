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

allowed_origins = origins_map.get(environment, origins_map[ENVIRONMENT.PRODUCTION.value])

print(f"Environment: {environment}")
print(f"Front-end URL: {front_end_url}")
print(f"Allowed origins: {allowed_origins}")

CORS(app,
     resources={r"/*": {
         "origins": allowed_origins,
         "supports_credentials": True,
         "allow_headers": ["Content-Type", "Authorization", "Accept"],
         "methods": ["GET", "OPTIONS"],
         "expose_headers": ["Content-Type"],
         "vary_header": True
     }})

db.init_app(app)
ma.init_app(app)

app.register_blueprint(routes_bp)

if __name__ == "__main__":
    app.run(debug=True)