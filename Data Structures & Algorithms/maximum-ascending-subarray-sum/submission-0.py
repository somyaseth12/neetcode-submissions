class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        maxS = cS = nums[0]
        

        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                cS += nums[i]
            else:
                cS = nums[i]
            maxS = max(maxS,cS)
        return maxS
        

       