#
# @lc app=leetcode id=234 lang=python3
#
# [234] Palindrome Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        list1 = []
        current_node = head
        while current_node is not None:
            list1.append(current_node.val)
            current_node = current_node.next

        l=0
        r=len(list1)-1
        while l<=r:
            if list1[l] != list1[r]:
                return False
            l +=1
            r -=1
        return True
# @lc code=end

