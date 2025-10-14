#
# @lc app=leetcode id=71 lang=python3
#
# [71] Simplify Path
#

# @lc code=start
class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        slashless = path.split("/")
        for i in slashless:
            if i == "..":
                if stack:
                    stack.pop()
            elif i == "." or i == "": #. --> ignore and emplty "" is created by multiple slashes
                continue
            else: 
                stack.append(i)
        return "/"+"/".join(stack)   
#time complexity: O(n)
#space complexity: O(n)
# @lc code=end

