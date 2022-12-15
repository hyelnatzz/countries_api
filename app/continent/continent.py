from flask import Blueprint, jsonify, abort
from app.models import Continent

continent_bp = Blueprint('continent_bp', __name__, url_prefix='/api/v1/continents')

@continent_bp.get('/')
def continents_home():
    continents = [{continent.name: continent.to_dict()} for continent in Continent.query.all()]
    try:
        if continents == []:
                abort(404, description='No continent added yet.')
        return jsonify({
            'data': continents
        }), 200
    except Exception:
        abort(500)


@continent_bp.get('/<name>')
def get_continent(name):
    continent = Continent.query.filter_by(name=name.capitalize()).first()
    try:
        return jsonify({
            'data': {continent.name: continent.to_dict()}
        })
    except AttributeError:
        abort(404, description=f"'{name}' not found. Check the spelling")
    except Exception:
        abort(500)
