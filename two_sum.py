class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        nums = list(enumerate(nums))  # O(n)
        nums = sorted(nums, key=lambda x: x[1])  # O(n * log n)
        
        i = len(nums) - 1
        j = 0
        
        # Rule out numbers that are too large
        while (nums[i][1] + nums[j][1]) > target:
            i -= 1

        while i >= 0:
            while (nums[i][1] + nums[j][1]) <= target:
                if nums[i][1] + nums[j][1] == target:
                    return [nums[i][0], nums[j][0]]
                    
                j += 1
                
            i -= 1
            