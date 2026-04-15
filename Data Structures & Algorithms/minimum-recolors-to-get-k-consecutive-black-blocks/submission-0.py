class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        # count whites in first window
        white_count = 0
        for i in range(k):
            if blocks[i] == 'W':
                white_count += 1
        
        min_ops = white_count
        
        # sliding window
        for i in range(k, len(blocks)):
            # remove left element
            if blocks[i - k] == 'W':
                white_count -= 1
            
            # add right element
            if blocks[i] == 'W':
                white_count += 1
            
            min_ops = min(min_ops, white_count)
        
        return min_ops