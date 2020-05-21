from src.magic_list.magic_list import MagicList
from src.magic_list.person import Person

class TestMagicList:

    def test_magic_list_without_class_type(self):
        magic_list = MagicList()
        magic_list[0] = "test"
        assert magic_list[0] == "test"
        print(magic_list[0])

    def test_magic_list_with_class_type(self):
        magic_list = MagicList(Person)
        magic_list[0].age = 10
        assert magic_list[0].age == 10
        print(magic_list[0])