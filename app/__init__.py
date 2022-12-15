import os
from flask import Flask, jsonify
from dotenv import load_dotenv

from app.main import main_bp
from app.continent.continent import continent_bp
from app.country.country import country_bp
from app.models import setup_db
from app.error_handlers import setup_error_handlers

load_dotenv()  # take environment variables from .env

def create_app():
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_mapping(
        SECRET_KEY=os.environ.get('SECRET_KEY'),
        FLASK_ENV='development',
        SQLALCHEMY_TRACK_MODIFICATIONS=False
        )

    db_path = 'sqlite:///data.db'

    # db.app = app
    # db.init_app(app)


    app.register_blueprint(main_bp)
    app.register_blueprint(continent_bp)
    app.register_blueprint(country_bp)


    with app.app_context():
        setup_db(app, db_path)
        setup_error_handlers(app)

    return app

    

