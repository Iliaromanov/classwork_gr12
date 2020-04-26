
class Bin:
    """Bin for robot parts

    Attributes:
        id(int): id number
        location(str): the location
        part_id(str): the id of the part
        qty_in_bin(int): the amount of that part in the bin
    """
    def __init__(self, id: int, location: str, part_id: str, qty_in_bin: int):
        """Creates a Bin object

        Args:
            id(int): id number
            location(str): the location
            part_id(str): the id of the part
            qty_in_bin(int): the amount of that part in the bin
        """
        self._id = id
        self.location = location
        self._part_id = part_id
        self._qty_in_bin = qty_in_bin

        def get_id(self):
            return self._id

        def set_id(self, new_id):
            assert new_id is int
            self._id = new_id

        def get_part_id(self):
            return self._part_id

        def set_part_id(self, new_part_id):
            assert new_part_id is int
            self._part_id = new_part_id

        def get_qty_in_bin(self):
            return self._qty_in_bin

        def set_qty_in_bin(self, new_value):
            assert new_value is int
            assert new_value >= 0
            self._qty_in_bin = new_value
       

class Part:
    """Robot parts class

    Attributes:
        id: int
        name: str
        quantity: int
        bin_id: int
    """

    def __init__(self, id: int, name: str, quantity: int, bin_id: int):
        self._id = id
        self.name = name
        self._quantity = quantity
        self._bin_id = bin_id

        def get_id(self):
            return self._id

        def set_id(self, new_id):
            assert new_id is int
            self._id = new_id

        def get_quantity(self):
            return self._quantity

        def set_quantity(self, new_amount):
            if new_amount < 0:
                raise ValueError("Quantity must be above 0")
            self._quantity = new_amount
