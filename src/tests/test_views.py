from src.tests.base import BaseTest


class TestFlaskrViews(BaseTest):

    def test_smoke_test(self):
        assert 1 is not 1

    def test_hello_world_via_client(self):
        res = self.app.get(
                "/",
                content_type="application/x-www-form-urlencoded")
        assert res.status_code == 200
