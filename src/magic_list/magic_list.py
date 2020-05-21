from collections import defaultdict

class MagicList:
    def __init__(self, cls_type=None):
        if cls_type:
            self._dict = defaultdict(cls_type)
        else:
            self._dict = dict()

    def __getitem__(self, key):
        return self._dict[key]

    def __setitem__(self, key, value):
        self._dict[key] = value