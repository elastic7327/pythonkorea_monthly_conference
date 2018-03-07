import json
import pytest

from src.tests.base import BaseTest
from src.models.user import User
from src.database import ENGINE, session

class TestFlaskrViews(BaseTest):

    def test_hello_world_via_client(self):

        # 토큰없이 시도를 할때에는 401 에러는 받습니다.
        res = self.app.get(
                "/",
                content_type="application/x-www-form-urlencoded")
        assert res.status_code == 401

        # Fake User을 만들어서, 해당 유저의 토큰을 발급받습니다.
        u = self.mixer.blend(User)
        data = json.dumps({"username": u.username, "password": u.password})
        res = self.app.post(
                    "/auth",
                    data=data,
                    content_type="application/json"
                )

        # 정상적인경우 status 200을 받습니다.
        assert res.status_code == 200
        assert 'access_token' in str(res.data)


        # 이제 헤더에 토큰을 추가해서 다시 시도합니다.
        token = json.loads(res.data)["access_token"]
        res = self.app.get(
                "/",
                headers={'Authorization': 'JWT ' + token})
        assert res.status_code == 200


        # 성공!











    @pytest.mark.skip(reason="skip it for a moment")
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

