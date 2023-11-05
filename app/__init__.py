from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate

from app.config import Settings

app = Flask(__name__)
app.config.from_object(Settings)

db = SQLAlchemy(app)
ma = Marshmallow(app)
migrate = Migrate(app, db)

# Endpoint
@app.route('/')
def index():
    return jsonify(message='Hola, bienvenido a la efi de DevOps')









