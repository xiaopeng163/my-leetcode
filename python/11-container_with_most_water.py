class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        _max = 0
        i = 0
        j = len(height) - 1
        while i < j:
            _max = max(_max, (j - i) * min(height[i], height[j]))
            if height[i] < height[j]:
                i += 1
            else:
                j -=1
        return _max