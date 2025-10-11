#
# @lc app=leetcode id=844 lang=python3
#
# [844] Backspace String Compare
#

# @lc code=start
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack = []
        for i in s:
            if i != "#":
                stack.append(i)
            elif stack:
                stack.pop()
        final_S = "".join(stack)
        stack1=[]
        for i in t:
            if i != "#":
                stack1.append(i)
            elif stack1:
                stack1.pop()
        final_t = "".join(stack1)

        return final_S == final_t



        

# @lc code=end
