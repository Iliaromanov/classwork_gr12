from typing import List
import math


# a) Easiest First
class Target:
    def __init__(self, difficulty: int):
        self.difficulty = difficulty
    
    def __repr__(self):
        return f"Target({self.difficulty})"

targets = [
    Target(10),
    Target(100),
    Target(25),
    Target(50)
]


def bubble_sort(targets: List[Target]) -> List[Target]:
    for i in range(len(targets) - 1):
      for j in range(len(targets) - 1 - i):
          a = targets[j].difficulty
          b = targets[j + 1].difficulty

          if a > b:
              targets[j], targets[j+1] = targets[j+1], targets[j]

    return targets

print(bubble_sort(targets))


# b) Closest First

enemy_locations = [
    [0, 3],
    [0, 2],
    [0, 4],
    [0, 1]
]

def bubble_sort_distance(locations):
    for i in range(len(locations) - 1):
        for j in range(len(locations) - 1 - i):
            a = math.sqrt(locations[j][0]**2 + locations[j][1]**2)
            b = math.sqrt(locations[j+1][0]**2 + locations[j+1][1]**2)

            if a > b:
                locations[j], locations[j + 1] = locations[j + 1], locations[j]
    return locations

print(bubble_sort_distance(enemy_locations))
