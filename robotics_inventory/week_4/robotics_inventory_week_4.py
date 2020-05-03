
import os
import datetime


class BaseRecord:
    def __inint__(self, id: int):
        self.created_at = datetime.datetime.now
        self.updated_at = datetime.datetime.now()
        self.id = id


class User:
    all_users = []

    def __init__(self, email: str, student_num: int):
        self.email = email
        self.student_num = student_num
        User.all_users.append(self)


class Part(BaseRecord):
    all_parts = []

    def __init__(self, name: str, quantity: int, barcode: str, bin_id: int):
        id = len(Part.all_parts)
        super().__init__(id)
        self.name = name
        self.quantity = quantity
        self._barcode = barcode
        self.bin_id = bin_id
        Part.all_parts.append(self)

    def get_barcode(self):
        return self._barcode

    def set_barcode(self, new_barcode: str):
        assert new_barcode is str
        self.barcode = new_barcode
        self.updated_at = datetime.datetime.now()


class Bin(BaseRecord):
    all_bins = []

    def __init__(self, location: str, part_id: int):
        id = len(Bin.all_bins)
        super().__init__(id)
        self._location = location
        self.part_id = part_id
        Bin.all_bins.append(self)

    def get_location(self):
        return self._location

    def set_location(self, new_location: str):
        assert new_location is str
        assert len(new_location) <= 2
        self._location = new_location
        self.updated_at == datetime.datetime.now()
        

class Log(BaseRecord):
    all_logs = []

    def __init__(self, user_id, part_id, quantity):
        self.user_id = user_id
        self.part_id = part_id
        self.quantity = quantity
        Log.all_logs.append(self)


class InventoryManager:
    def __init__(self):
        self.users = User.all_users
        self.parts = Part.all_parts
        self.bins = Bin.all_bins
        self.logs = Log.all_logs

    def create_user(self, email: str, student_num: int) -> None:
        User(email, student_num)

    def find_bin_by_location(self, location: str) -> Bin:
        for bin in self.bins:
            if bin.location == location:
                return bin

    def find_user_by_student_num(self, num: int) -> User:
        for user in self.users:
            if user.student_num == num:
                return user

    def add_part(name, quantity, bin_location) -> None:
        bin_id = self.find_bin_by_location(bin_location).id
        Part(name, quantity, bin_id)


if __name__ == "__main__":
    os.system("pytest")
#    os.system("mypy main.py --disallow-untyped-defs")
    os.system("pycodestyle main.py --ignore=E501,W")
