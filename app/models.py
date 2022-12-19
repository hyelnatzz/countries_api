from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate



db = SQLAlchemy()

"""
setup_db(app)
    binds a flask application and a SQLAlchemy service
"""
def setup_db(app, path):
    app.config['SQLALCHEMY_DATABASE_URI'] = path
    db.app = app
    db.init_app(app)
    db.create_all()
    migrate = Migrate(app, db)

class Continent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    total_population = db.Column(db.Integer)
    countries = db.relationship('Country', backref='continent', lazy='dynamic')
     

    def save(self):
        db.session.add(self)
        db.session.commit()

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'countries': len(self.countries.all())
        }

    def __repr__(self):
        return f'<Continent: {self.name}>'


class Country(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    continent_id = db.Column(db.Integer, db.ForeignKey('continent.id'))
    name = db.Column(db.String(20), unique=True, nullable=False)
    population = db.Column(db.Integer)
    currency = db.Column(db.String(5))
    cca = db.Column(db.String)
    official_lang = db.Column(db.String)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'continent': self.continent.name,
            'population': self.population,
            'cca3': self.cca,
            'currency': self.currency,
            'official language': self.official_lang
        }

    def __repr__(self):
        return f'<Country: {self.name}>'




