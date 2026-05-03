class Solution:
    def findLucky(self, arr: List[int]) -> int:
        count = Counter(arr)
        ans = -1
        
        for num in count:
            if count[num] == num:
                ans = max(ans, num)
                
        return ans