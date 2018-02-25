from sqlalchemy import MetaData

import unittest

from src.flaskr import app

class BaseTest(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.app = app.test_client()
