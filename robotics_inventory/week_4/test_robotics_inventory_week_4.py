
from main import BaseRecord, User, InventoryManager, Bin

def test_create_user():
    me = InventoryManager()
    me.create_user("dundas.levins20@ycdsbk12.ca", 1112387)
    assert len(User.all_users) == 1

    me.create_user("bart.garthoplis@ycdsb.ca", 2224241)
    assert len(User.all_users) == 2

def test_find_bin_by_location():
    pass
