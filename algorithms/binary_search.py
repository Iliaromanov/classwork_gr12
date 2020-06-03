
from typing import List

def binary_search(nums: List[int], target: int) -> int:
    nums.sort()

    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        result = nums[mid]

        print(mid)

        if result == target:
            return mid
        elif result > target:
            right = mid
        elif result < target:
            left = mid
