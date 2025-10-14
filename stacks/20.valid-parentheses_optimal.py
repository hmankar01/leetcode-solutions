#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashmap = {')':'(',
                   '}':'{',
                   ']':'['
                   }
        for i in s:
            if i in hashmap:#checks closing paranthesis only
                if stack and stack[-1] == hashmap[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        if not stack:
            return True
        else: 
            return False
#time complexity: O(n) 
# space complexity: O(n) because hashmap is taking O(1) as the variables are constant

# @lc code=end

