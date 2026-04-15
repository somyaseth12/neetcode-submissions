class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
     
        left = 0
        right = len(arr) - 1
        
        while right - left + 1 > k:
            if abs(arr[left] - x) > abs(arr[right] - x):
                left += 1   # remove left (farther)
            else:
                right -= 1  # remove right (farther)
        
        return arr[left:right+1]