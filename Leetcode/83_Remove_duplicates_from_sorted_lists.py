# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# link to problem 
''' 'https://leetcode.com/problems/remove-duplicates-from-sorted-list/?envType=problem-list-v2&envId=linked-list' '''

'''
maintain an array to push elements if found while traversing. Maintain a previous pointer as well to Delete the duplicate
element. If found in array then do prev.next = curr.next 
'''

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr =[]

        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        curr = head

        while curr:
            
            if curr.val not in arr:
                arr.append(curr.val)
                prev = prev.next  
            else:
                
                prev.next = curr.next

        
            curr = curr.next

        return head


        