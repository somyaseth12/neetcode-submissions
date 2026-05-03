class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:

        n = len(grid)
        total = n * n
        
        freq = [0] * (total + 1)
        repeated = 0
        missing = 0
        
        # Count frequency of each number
        for row in grid:
            for num in row:
                freq[num] += 1
        
        # Find repeated and missing numbers
        for i in range(1, total + 1):
            if freq[i] == 2:
                repeated = i
            elif freq[i] == 0:
                missing = i
        
        return [repeated, missing]