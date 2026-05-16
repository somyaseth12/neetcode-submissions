class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        freq = Counter(arr)   # count frequency of each string
        
        for word in arr:      # keep original order
            if freq[word] == 1:
                k -= 1
                if k == 0:
                    return word
        
        return ""