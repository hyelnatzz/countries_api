from flask import Blueprint, jsonify, request, abort
from app.models import Country


country_bp = Blueprint('country_bp', __name__, url_prefix='/api/v1/countries')

@country_bp.get('/')
def countries_home():
    try:
        countries = [{country.name: country.to_dict()} for country in Country.query.all()]
        if countries == []:
            abort(404, description='No country added yet.')
        return jsonify({
            'data': countries,
        }), 200
    except Exception:
        abort(500)


@country_bp.get('/<name>')
def get_continent(name):
    country = Country.query.filter_by(name=name.capitalize()).first()
    try:
        return jsonify({
            'data': {country.name: country.to_dict()}
        }), 200
    except AttributeError:
        abort(404, description=f"'{name}' not found. Check the spelling")
    except Exception:
        abort(500)
