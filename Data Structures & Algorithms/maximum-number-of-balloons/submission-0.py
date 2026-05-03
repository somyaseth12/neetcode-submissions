class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count = Counter(text)
        
        return min(
            count['b'],
            count['a'],
            count['l'] // 2,   # 'l' appears 2 times
            count['o'] // 2,   # 'o' appears 2 times
            count['n']
        )
