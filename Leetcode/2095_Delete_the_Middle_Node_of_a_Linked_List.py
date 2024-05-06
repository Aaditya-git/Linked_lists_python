'''

Link : https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/description/?envType=study-plan-v2&envId=leetcode-75
You are given the head of a linked list. Delete the middle node, and return the head of the modified linked list.

The middle node of a linked list of size n is the ⌊n / 2⌋th node from the start using 0-based indexing, where ⌊x⌋ denotes the largest integer less than or equal to x.

For n = 1, 2, 3, 4, and 5, the middle nodes are 0, 1, 1, 2, and 2, respectively.

'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        slow = head
        dummy = ListNode(-1)
        curr = dummy
        curr.next = head
        if slow.next is None:
            return None
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            curr = curr.next
        curr.next = slow.next
        slow.next = None
        return head
'''
Optimal Solution :

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        
        fast = head
        slow = head
        prev = None
        
        1->2->3
        P
        F
        S
        Next while iteration :
        1->2->3
              F
        P  S     
        
        Then just remove the node :) 
             
        while fast and fast.next:
            fast = fast.next.next
            prev = slow              
            slow = slow.next
        
        # Remove the middle node
        prev.next = slow.next
        
        return head

'''
