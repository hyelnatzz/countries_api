# Flask-RESTful API project template

This project is a simple API that provides information about the continents and the countries in the world.
It uses the flask factory method and the Blueprints design.

There are two models implemented: Continent and Country, with sample data provided about Europe and four countries within it. The database management system is SQLlite.

Main libraries used:
1. Flask-Migrate - for handling all database migrations.
2. Flask-SQLAlchemy - adds support for SQLAlchemy ORM.

Project structure:
```
.
├── README.md
├── app
│   ├── __init__.py
│   ├── continent
│   │   ├── __init__.py
│   │   └── continent.py
│   ├── country
│   │   ├── __init__.py
│   │   └── country.py
│   ├── error_handlers.py
│   ├── main.py
│   ├── models.py
│   └── sample.py
├── instance
│   └── data.db  
├── requirements.txt
├── test_app.py
└── wsgi.py
```

* app - holds all endpoints, error handlers and data models.
* instance - holds the sqlite db.
* test_app.py - contains the app test cases.
* wsgi.py - contains gunicorn server setup requirement (for deployment on render.com)

## Running 

1. Clone repository.
2. pip install requirements.txt
3. Start server by running 'flask run --reload':
4. Populate database by visiting http://127.0.0.1:5000/


## Usage
### Countries endpoint
GET all countries http://127.0.0.1:5000/api/v1/countries

RESPONSE
```json
{
    "data": [
        {
            "details": {
                "cca3": "NOR",
                "continent": "Europe",
                "currency": "Norwegian krone",
                "id": 1,
                "name": "Norway",
                "official language": "Norwegian",
                "population": 5425270
            },
            "name": "Norway"
        },
        {
            "details": {
                "cca3": "MDA",
                "continent": "Europe",
                "currency": "Moldovan leu",
                "id": 2,
                "name": "Moldova",
                "official language": "Romanian",
                "population": 2603813
            },
            "name": "Moldova"
        },
        {
            "details": {
                "cca3": "LVA",
                "continent": "Europe",
                "currency": "Euro",
                "id": 3,
                "name": "Latvia",
                "official language": "Latvian",
                "population": 1842226
            },
            "name": "Latvia"
        },
        {
            "details": {
                "cca3": "EST",
                "continent": "Europe",
                "currency": "Euro",
                "id": 4,
                "name": "Estonia",
                "official language": "Estonian",
                "population": 1331796
            },
            "name": "Estonia"
        }
    ]
}
```
GET one country http://127.0.0.1:5000/api/v1/countries/latvia

RESPONSE
```json
{
    "data": {
        "details": {
            "cca3": "LVA",
            "continent": "Europe",
            "currency": "Euro",
            "id": 3,
            "name": "Latvia",
            "official language": "Latvian",
            "population": 1842226
        },
        "name": "Latvia"
    }
}
```
GET all continents http://127.0.0.1:5000/api/v1/continents/

RESPONSE
```json
{
    "data": [
        {
            "details": {
                "countries": 4,
                "id": 1,
                "name": "Europe"
            },
            "name": "Europe"
        }
    ]
}
```
GET one continent http://127.0.0.1:5000/api/v1/continents/europe

RESPONSE
```json
{
    "data": {
        "details": {
            "countries": 4,
            "id": 1,
            "name": "Europe"
        },
        "name": "Europe"
    }
}
```
