

from mixer.backend.sqlalchemy import Mixer

from sqlalchemy import MetaData
from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

import unittest

from src.flaskr import app

from src.models import user

from src.models.user import Base

ENGINE = create_engine('sqlite:///:memory:')

class BaseTest(unittest.TestCase):

    def setUp(self):
        app.testing = True

        self.app = app.test_client()

        Base.metadata.create_all(ENGINE)

        SESSION = sessionmaker(bind=ENGINE)

        self.mixer = Mixer(session=SESSION(), commit=True)

        # role = mixer.blend(user.User)

        # dal.db_init('sqlite:///:memory:')

    def tearDown(self):
        ENGINE = create_engine('sqlite:///:memory:')
        Base.metadata.drop_all(ENGINE)
