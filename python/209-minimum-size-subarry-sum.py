class Solution:
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        start = 0
        sum_tmp = 0
        min_size = float('inf')
        for i in range(len(nums)):
            sum_tmp += nums[i]
            while sum_tmp >= s:
                min_size = min(min_size, i - start + 1)
                sum_tmp -= nums[start]
                start += 1

        return min_size if min_size != float('inf') else 0