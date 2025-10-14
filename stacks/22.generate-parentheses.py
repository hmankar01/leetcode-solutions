#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(current_string,open_count,close_count):
            #base case for recursive approach
            if len(current_string) == 2*n:
                res.append(current_string)
                return
            
            if open_count<n:#condition 1
                backtrack(current_string + "(",open_count+1,close_count)

            if close_count<open_count:#condition 2
                backtrack(current_string+')',open_count,close_count+1)
            
        backtrack("",0,0) # will start from empty string and keep adding opening and closing paranthesis
        return res



# @lc code=end

