from main import BaseRecord, User, InventoryManager, Bin, Part, Log

def test_create_user():
    me = InventoryManager()
    me.create_user("dundas.levins20@ycdsbk12.ca", 1112387)
    assert len(User.all_users) == 1

    me.create_user("bart.garthoplis@ycdsb.ca", 2224241)
    assert len(User.all_users) == 2

def test_find_bin_by_location():
    me = InventoryManager()
    a = Bin("A3", 12345)
    b = Bin("B7", 41325)

    assert me.find_bin_by_location("A3") == a
    assert me.find_bin_by_location("B7") == b


def test_find_user_by_student_num():
    me = InventoryManager()
    bill = User("bill.nye20@ycdsbk12.ca", 123456789)
    shaquiffa = User("shaquiffa.daniel@ycdsbk12.ca", 987654321)

    assert me.find_user_by_student_num(123456789) == bill
    assert me.find_user_by_student_num(987654321) == shaquiffa

def test_find_part_by_barcode():
    me = InventoryManager()
    a = Part("motor", 1, "1j343g", 12345)
    b = Part("sensor", 4, "4h935y", 51234)

    assert me.find_part_by_barcode("1j343g") == a
    assert me.find_part_by_barcode("4h935y") == b

def test_add_part():
    me = InventoryManager()
    a = Bin("A3", 12345)
    b = Bin("B7", 41325)
    me.add_part("motherboard", 1, "123l4jk", "A3")
    me.add_part("ssd", 1, "a21l3kj4", "B7")

    for part in me.parts:
        if part.name == "motherboard":
            assert part.bin_id == 0
        elif part.name == "ssd":
            assert part.bin_id == 1
