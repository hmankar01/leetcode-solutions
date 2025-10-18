#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
            return False
        hashmap = {}
        for i in s:
            if i not in hashmap:
                hashmap[i] = 1
            else:
                hashmap[i] +=1

        for i in t:
            if i in hashmap:
                hashmap[i] -= 1
            elif i not in hashmap:
                return False
            
        for i in hashmap:
            if hashmap[i] > 0:
                return False
        return True

    

            
    

# @lc code=end

