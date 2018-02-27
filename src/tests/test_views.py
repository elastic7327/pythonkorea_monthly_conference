import json
import pytest

from src.tests.base import BaseTest
from src.models.user import User

from src.database import ENGINE, session

class TestFlaskrViews(BaseTest):

    @pytest.mark.skip(reason="skip it for a moment")
    def test_hello_world_via_client(self):
        res = self.app.get(
                "/",
                content_type="application/x-www-form-urlencoded")
        assert res.status_code == 200

    def test_hello_projected_via_client(self):
        res = self.app.get(
                "/protected",
                content_type="application/x-www-form-urlencoded")
        assert res.status_code == 401


    def test_auth_endpoint_with_valid_request(self):

        u = self.mixer.blend(User)

        data = json.dumps({"username": u.username, "password": u.password})

        res = self.app.post(
                    "/auth",
                    data=data,
                    content_type="application/json"
                )

        assert res.status_code == 200

        assert 'access_token' in str(res.data)

        token = json.loads(res.data)["access_token"]

        print(token)

        res = self.app.get('/protected', headers={'Authorization': 'JWT ' + token})

        assert res.status_code == 200

