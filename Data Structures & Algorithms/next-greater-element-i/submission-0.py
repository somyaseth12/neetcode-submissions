class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        nge_map = {}

        # Step 1: Build mapping for nums2
        for num in nums2:
            while stack and num > stack[-1]:
                nge_map[stack.pop()] = num
            stack.append(num)

        # Remaining elements → no next greater
        while stack:
            nge_map[stack.pop()] = -1

        # Step 2: Answer for nums1
        result = []
        for num in nums1:
            result.append(nge_map[num])

        return result