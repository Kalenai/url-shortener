from flask_testing import TestCase
from app import create_app, db


class BaseTestCase(TestCase):
    def create_app(self):
        self.app = create_app('app.config.TestingConfig')
        return self.app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
