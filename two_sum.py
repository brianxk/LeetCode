import math

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # nums = list(enumerate(nums))  # O(n)
        nums_copy = list(nums)
        nums.sort() # = sorted(nums, key=lambda x: x[1])  # O(n * log n)
        
        i = len(nums) - 1
        j = 0
        
        # Rule out numbers that are too large
        i = self.find_target_index(nums, 0, len(nums), target, nums[j])

        while i > j:
            while (nums[i] + nums[j]) <= target:
                if nums[i] + nums[j] == target:
                    first = nums_copy.index(nums[i])
                    second = nums_copy.index(nums[j])
                    
                    if first == second:
                        second = nums_copy.index(nums[j], first + 1)
                    
                    return [first, second]
                    
                j += 1
                
            i -= 1
       
    
    def find_target_index(self, nums: List[int], begin: int, end:int , target: int, pair: int) -> int:
        midpoint = math.floor((begin + end) / 2)
        if midpoint <= begin:
            return midpoint
        
        if nums[midpoint] + pair > target:
            return self.find_target_index(nums, begin, midpoint, target, pair)
        elif nums[midpoint] + pair < target:
            return self.find_target_index(nums, midpoint, end, target, pair)
        elif nums[midpoint] + pair == target:
            return midpoint
        