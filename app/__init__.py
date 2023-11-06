from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager

from app.config import Settings

app = Flask(__name__)
app.config.from_object(Settings)

db = SQLAlchemy(app)
ma = Marshmallow(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)

# Endpoint
@app.route('/')
def index():
    return jsonify(message='Hola, bienvenido a la efi de DevOps')

from app.views import users

app.register_blueprint(users.bp, url_prefix='/users')








