class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # nums = list(enumerate(nums))  # O(n)
        nums_copy = list(nums)
        nums.sort() # = sorted(nums, key=lambda x: x[1])  # O(n * log n)
        
        i = len(nums) - 1
        j = 0
        
        # Rule out numbers that are too large
        while (nums[i] + nums[j]) > target:
            i -= 1

        while i >= 0:
            while (nums[i] + nums[j]) <= target:
                if nums[i] + nums[j] == target:
                    first = nums_copy.index(nums[i])
                    second = nums_copy.index(nums[j])
                    
                    if first == second:
                        second = nums_copy.index(nums[j], first + 1)
                    
                    return [first, second]
                    
                j += 1
                
            i -= 1
            