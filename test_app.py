import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from app.models import setup_db


class TriviaTestCase(unittest.TestCase):
    """This class represents the country api test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.app.secret_key = os.environ.get('SECRET_KEY')
        self.database_path = 'sqlite:///data.db'

        # binds the app to the current context
        with self.app.app_context():
            setup_db(self.app, self.database_path)
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
    
    def tearDown(self):
        """Executed after each test"""
        pass


    def test_get_country(self):
        res = self.client().get("/api/v1/countries/latvia")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue('Latvia' in data["data"])


    def test_get_all_countries(self):
        res = self.client().get("/api/v1/countries/")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(len(data['data']), 4)


    def test_404_for_countries(self):
        res = self.client().get("/api/v1/countries/nigeria")

        self.assertEqual(res.status_code, 404)


    def test_get_continent(self):
        res = self.client().get("/api/v1/continents/europe")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue('Europe' in data["data"])


    def test_get_all_continent(self):
        res = self.client().get("/api/v1/continents/")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(len(data['data']), 1)


    def test_404_for_continent(self):
        res = self.client().get("/api/v1/continents/nigeria")

        self.assertEqual(res.status_code, 404)


    def test_404_general(self):
        res = self.client().get("/api/hgjogjdagbk")

        self.assertEqual(res.status_code, 404)




# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()