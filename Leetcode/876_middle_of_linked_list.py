'''876. Middle of the Linked List

https://leetcode.com/problems/middle-of-the-linked-list/description/
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow_node = head
        fast_node = head
        while fast_node is not None and fast_node.next is not None:
            fast_node = fast_node.next.next
            slow_node = slow_node.next

        return slow_node
