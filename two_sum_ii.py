from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        low, high = 0, len(numbers)-1

        mid = (low + high)//2
        while low < high:
            if (numbers[mid] > target):
                high = mid - 1

            elif (numbers[mid] < target):
                low = mid + 1

            elif (numbers[low] + numbers[mid] == target):
                return [low, mid]
