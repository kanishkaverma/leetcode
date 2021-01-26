class Solution(object): 
    def twoSum(self, nums, target): 
        dict = { }
        for i, x in enumerate(nums): 
            target_num = target - x 
            if target_num in dict: 
                return [dict[target_num], i]
            dict[x]= i
        return []