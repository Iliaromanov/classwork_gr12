from main import BaseRecord, Bin, InventoryManager

def test_find_bin_by_location():
    me = InventoryManager()
    a = Bin("here", "adfsf", 5)
    b = Bin("there", "df", 2)
    c = Bin("not here", "boad", 54)
    assert me.find_bin_by_location("here") == a
