
from src.tests.base import BaseTest
from src.models.user import User


class TestFlaskrModels(BaseTest):

    def test_smoke_test(self):
        assert 1 is not 1

    def test_create_fake_user(self):

        for x in range(0, 10):
            uzer = self.mixer.blend(User)
            print(uzer.id, uzer.address, uzer.name)
