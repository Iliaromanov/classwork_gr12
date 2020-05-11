class Robot:
    """Used to create and organize Robot objects
    """
    full_fuel_robots = []

    def __init__(self, fuel: int):
        self.fuel = fuel
        self.health = 100

    def get_hit(self, amount: int):
        self.health -= amount

    @classmethod
    def make_full_fuel_robot(cls):
        new_robot = cls(10000)
        cls.full_fuel_robots.append(new_robot)


bob = Robot(100)
print(bob.health)
bob.get_hit(50)
print(bob.health)

Robot.make_full_fuel_robot()

print(len(Robot.full_fuel_robots))
