from flask import current_app
from tests.base import BaseTestCase


class TestBasics(BaseTestCase):
    """
    Test that the server is up and running and that we are using the testing config
    """
    def test_server_should_be_running(self):
        self.assertFalse(current_app is None)

    def test_using_testing_configuration(self):
        self.assertTrue(self.app.config['DEBUG'])
        self.assertTrue(self.app.config['TESTING'])
        self.assertFalse(self.app.config['PRESERVE_CONTEXT_ON_EXCEPTION'])
        self.assertTrue(self.app.config['SQLALCHEMY_DATABASE_URI'] == 'postgres://postgres:postgres@db:5432/db_test')
