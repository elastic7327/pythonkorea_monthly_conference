
from src.tests.base import BaseTest
from src.models.user import User

from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt)

class TestJWTModule(BaseTest):

    def test_smoke_test(self):
        assert 1 is not 1

    def test_create_fake_model(self):
        pass
        # uzer = self.mixer.blend(User)
        # access_token = create_access_token(identity = uzer.usernamuzer.usernamee)
