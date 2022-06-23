class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        nums = list(enumerate(nums))  # O(n)
        nums = sorted(nums, key=lambda x: x[1])  # O(n * log n)
        nums.reverse()  # O(n)
        
        i = 0
        j = len(nums) - 1
        
        solution = []
        
        # Rule out numbers that are too large
        while (nums[i][1] + nums[j][1]) > target:
            i += 1

        while not solution:
            while (nums[i][1] + nums[j][1]) <= target:
                if nums[i][1] + nums[j][1] == target:
                    solution += [nums[i][0], nums[j][0]]
                    break
                    
                j -= 1
                
            i += 1
                
        return solution
        