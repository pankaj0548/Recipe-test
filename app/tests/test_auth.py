import unittest
from app import create_app
from app.db.models import User
from app.modules.my_sql import db
from flask import Flask

app = create_app()

class AuthTestCase(unittest.TestCase):
    
    def setUp(self):
        self.app = app.test_client()

    def test_register(self):
        response = self.app.post('/signup', data={'name':'Test User','email': 'test_user', 'password': '1234','conf_pass':'1234'}, follow_redirects=True)
        self.assertIn(b'Login', response.data) 

    def test_login(self):
        self.app.post('/register', data={'name':'Test User','email': 'test_user', 'password': '1234','conf_pass':'1234'}, follow_redirects=True)
        response = self.app.post('/login', data={'email': 'test_user', 'password': '1234'}, follow_redirects=True)
        self.assertIn(b'Recipe', response.data)

    def test_logout(self):
        self.app.post('/register', data={'name':'Test User','email': 'test_user', 'password': '1234','conf_pass':'1234'}, follow_redirects=True)
        self.app.post('/login', data={'email': 'test_user', 'password': '1234'}, follow_redirects=True)
        response = self.app.get('/logout', follow_redirects=True)
        self.assertIn(b'Login', response.data)

if __name__ == '__main__':
    unittest.main()
