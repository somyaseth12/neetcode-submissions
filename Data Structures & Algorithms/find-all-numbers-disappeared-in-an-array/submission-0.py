class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for num in nums:
            index = abs(num) - 1   # convert value to index
            
            if nums[index] > 0:
                nums[index] = -nums[index]   # mark as visited
        
        # Positive index means number is missing
        result = []
        for i in range(len(nums)):
            if nums[i] > 0:
                result.append(i + 1)
        
        return result