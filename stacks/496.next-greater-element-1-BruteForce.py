'''

Next Greater Element I
Category	Difficulty	Likes	Dislikes
algorithms	Easy (75.13%)	9305	1019

The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.
You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.
For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater element of nums2[j] in nums2. If there is no next greater element, then the answer for this query is -1.
Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.

Example 1:
Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
Output: [-1,3,-1]
Explanation: The next greater element for each value of nums1 is as follows:
- 4 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
- 1 is underlined in nums2 = [1,3,4,2]. The next greater element is 3.
- 2 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.

Example 2:
Input: nums1 = [2,4], nums2 = [1,2,3,4]
Output: [3,-1]
Explanation: The next greater element for each value of nums1 is as follows:
- 2 is underlined in nums2 = [1,2,3,4]. The next greater element is 3.
- 4 is underlined in nums2 = [1,2,3,4]. There is no next greater element, so the answer is -1.

'''
#
# @lc app=leetcode id=496 lang=python3
#
# [496] Next Greater Element I
#

# @lc code=start
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        
        for num1 in nums1:
            found = False
            start_idx = nums2.index(num1)

            for j in range(start_idx + 1, len(nums2)):
                if nums2[j] > num1:
                    ans.append(nums2[j])
                    found = True
                    break
            if not found:
                ans.append(-1)
                
        return ans
            
# @lc code=end

# Brute Force Solution
#
# Time Complexity: O(m * n)
# - The outer loop iterates through each element of nums1 (m elements).
# - The inner loop, in the worst case, iterates through the entire nums2 array (n elements).
#
# Space Complexity: O(1)
# - We are not using any extra data structures that scale with the input size.
# - The 'ans' array is for the output and is not considered 'extra' space.