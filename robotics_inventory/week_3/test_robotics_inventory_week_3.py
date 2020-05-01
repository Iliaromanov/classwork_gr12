from main import BaseRecord, Bin, InventoryManager, User

def test_find_bin_by_location():
    me = InventoryManager()
    a = Bin("here", "adfsf", 5)
    b = Bin("there", "df", 2)
    c = Bin("not here", "boad", 54)

    assert me.find_bin_by_location("here") == a
    assert me.find_bin_by_location("there") == b

def test_find_user_by_student_num():
    me = InventoryManager()
    bill = User("bill.nye20@ycdsbk12.ca", 123456789)
    bartholamule = User("bart@yandex.ru", "N/A")
    shaquiffa = User("shaquiffa.daniel@ycdsbk12.ca", 987654321)

    assert me.find_user_by_student_num(123456789) == bill
    assert me.find_user_by_student_num(987654321) == shaquiffa
