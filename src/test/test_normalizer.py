from src.api.normalizer import Normalizer

class TestNormalizer:
    def test_normalize(self):
        normalizer = Normalizer()
        data = [
            {
                "name": "device",
                "strVal": "iPhone",
                "metadata": "not interesting"
            },
            {
                "name": "isAuthorized",
                "boolVal": "false",
                "lastSeen": "not interesting"
            }
        ]
        result = normalizer.normalize(data)
        assert result == {
            "device": "iPhone",
            "isAuthorized": "false"
        }
