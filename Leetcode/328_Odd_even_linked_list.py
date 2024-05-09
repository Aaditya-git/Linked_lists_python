'''
https://leetcode.com/problems/odd-even-linked-list/?envType=study-plan-v2&envId=leetcode-75

  '''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        odd = head
        even = head.next
        evenhead = even

        while even is not None and even.next is not None:
            odd.next = odd.next.next
            odd = odd.next

            even.next = even.next.next
            even = even.next

        odd.next = evenhead
        return head


    '''
    1-2-3-4-5-None
    
    line 20
    
    |----|
    1 2->3-4-5
    O
    
    Line 21
    |----|
    1 2->3-4-5
         O
    
    '''