class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        remains = {}
        for index, value in enumerate(nums):
            tmp = target - value
            if tmp in remains:
                return [remains[tmp], index]
            else:
                remains[value] = index
