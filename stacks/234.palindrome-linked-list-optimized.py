#SLOW AND FAST POINTER TECHNIQUE
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
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next
            fast = fast.next
            slow = slow.next
            # slow pointer will be in the middle till the time fast pointer is at null or end of the linked list

        #reversing 2nd half of the list
        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp

        # checking palindrome
        left,right = head,prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True
             
# @lc code=end

