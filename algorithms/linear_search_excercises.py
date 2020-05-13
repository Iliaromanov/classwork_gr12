from typing import List

# 1. Search a list of ints for a particular integer. Return the index location, -1 if not found.

def find_num(nums: List[int], target: int) -> int:
    for i, num in enumerate(nums):
        if num == target:
            return i
    return -1


# 2. Search a list of ints for the last occurance of a particular integer. -1 if not found.

def find_last_num(nums: List[int], target: int) -> int:
    max_i = -1
    i = 0

    while i < len(nums):
        if nums[i] == target:
            if i > max_i:
                max_i = i
        i += 1
    return max_i
