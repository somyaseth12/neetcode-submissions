class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
      max_right = -1   # last element will become -1
    
    # traverse from right to left
      for i in range(len(arr) - 1, -1, -1):
          current = arr[i]      # store current value
          arr[i] = max_right   # replace with max on right
          
          # update max_right
          if current > max_right:
              max_right = current
      
      return arr
        
      