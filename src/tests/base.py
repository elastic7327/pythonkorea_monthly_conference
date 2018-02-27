

from mixer.backend.sqlalchemy import Mixer

from sqlalchemy import MetaData
from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

import unittest

from src.flaskr import app

from src.models import user

from src.models.user import Base

# ENGINE = create_engine('sqlite:///:memory:')

ENGINE = create_engine("mysql://root:MyNewPass@localhost/local_test")

class BaseTest(unittest.TestCase):

    def setUp(self):
        Base.metadata.create_all(ENGINE)
        app.testing = True
        app.debug = True

        self.app = app.test_client()

        self.SESSION = sessionmaker(bind=ENGINE)
        self.mixer = Mixer(session=self.SESSION(), commit=True)

        # role = mixer.blend(user.User)

        # dal.db_init('sqlite:///:memory:')

    def tearDown(self):
        pass
        # self.SESSION.close_all()
        # Base.metadata.drop_all(ENGINE)
