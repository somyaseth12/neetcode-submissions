from collections import Counter

class Solution:
    def maxDifference(self, s: str) -> int:
        freq = Counter(s)   # count frequency of each character
        
        max_odd = 0         # maximum odd frequency
        min_even = float('inf')  # minimum even frequency
        
        for count in freq.values():
            if count % 2 == 1:   # odd frequency
                max_odd = max(max_odd, count)
            else:                # even frequency
                min_even = min(min_even, count)
        
        return max_odd - min_even