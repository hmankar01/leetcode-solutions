#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#

# @lc code=start
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        counter = {}
        for i in nums:
            if i in counter:
                return True
            else:
                counter[i] = 1 
        return False
# @lc code=end

