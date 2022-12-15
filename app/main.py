from flask import Blueprint, jsonify, abort
from app.models import Continent, Country
from sqlalchemy.exc import SQLAlchemyError

main_bp = Blueprint('main_bp', __name__, url_prefix='/')

@main_bp.get('/')
@main_bp.get('/api/')
@main_bp.get('/api/v1/')
def index():
    try:
        populate_db()
        return jsonify({
                'message': 'Welcome to the countries api.\nTo get country details visit /api/v1/countries/<name>\nTo get continent details visit /api/v1/continents/<name>.',
        }), 200
    except SQLAlchemyError:
        abort(500, description='Something went wrong, try again')



#---------------------------------- DB UTILITY ----------------------------#
def populate_db():
    '''Populates db if empty'''
    c = Continent.query.all()
    if c != []:
        return
    
    from app.sample import continent, countries
    europe = Continent(**continent)
    europe.save()

    for country in countries:
        new_country = Country()
        new_country.name = country.name
        new_country.cca = country.cca
        new_country.currency = country.currency
        new_country.population = country.population
        new_country.official_lang = country.official_lang
        new_country.continent = europe
        new_country.save()
    return