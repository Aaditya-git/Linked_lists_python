'''
https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/description/?envType=study-plan-v2&envId=leetcode-75


'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        stk = []
        maxx = 0
        value = 0
        dummy = ListNode(10)
        curr = dummy
        curr.next = head
        slow = head
        fast = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            curr = curr.next
            stk.append(curr.val)

        while stk:
            value = stk.pop() + slow.val
            slow = slow.next

            if value > maxx:
                maxx = value

        return maxx