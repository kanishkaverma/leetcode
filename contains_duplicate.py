class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        set1 = set()
        for i in range(len(nums)):
            if nums[i] in set1:
                return True
            set1.add(nums[i])
        print(set1)
        return False

# Alternate sol
# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         return len(set(nums)) < len(nums)