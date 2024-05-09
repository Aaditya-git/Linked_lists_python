'''
https://leetcode.com/problems/reverse-linked-list/?envType=study-plan-v2&envId=leetcode-75

206 - Reverse the linked List.
  '''



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        temp = head
        curr = head
        while curr:
            temp = curr
            curr = temp.next
            temp.next = prev
            prev = temp
        return temp

'''
P = None
 T
 C
 1->2->3->4->5
 -------------------------
 Line number 20 and 21
 
 T   C
 1->2->3->4->5
 
 Line number 22 :
       T C
 Prev<-1 2->3->4
 
 Line 23:
        P
        T C
 None <-1 2->3->4

Loop it
'''