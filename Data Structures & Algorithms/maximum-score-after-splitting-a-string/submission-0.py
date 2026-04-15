class Solution:
    def maxScore(self, s: str) -> int:
        ms=0
        for i in range(1,len(s)):
            left = s[:i]
            right = s[i:]

            zeros = left.count('0')
            ones = right.count('1')

            ms = max(ms,zeros+ones)
        return ms