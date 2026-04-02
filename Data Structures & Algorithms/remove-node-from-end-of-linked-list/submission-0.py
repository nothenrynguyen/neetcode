# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        # official leetcode follow-up is to do this in one pass

        # we can do this in 2 pointers where the right pointer is moved forward by n,
        # so we shift them to the end and by then, the left pointer is at the node we want to delete
        # but we need to delete that node, so we instead start the left pointer at a starting dummy node

        dummy = ListNode(0, head)
        left = dummy
        right = head

        # this is to shift the right pointer to n from the end
        while n > 0 and right:
            right = right.next
            n -= 1

        while right:
            left = left.next
            right = right.next

        # delete 
        left.next = left.next.next

        return dummy.next # cuz we don't want to include dummy and dummy.next is the head

