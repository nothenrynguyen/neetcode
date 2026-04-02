"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        # two passes
        
        oldToCopy = { None: None} # the none:none is for the 2nd pass for when cur.next = None

        # first pass 
        # 1 creates a deep copy of each node and 
        # 2 makes a hashmap where we map every old node to the new copy

        cur = head
        while cur:
            copy = Node(cur.val) # creates a copy of the node
            oldToCopy[cur] = copy # creates a hashmap mapping old node to copy
            cur = cur.next

        # second pass is the pointer connecting (next / random)

        cur = head
        while cur: 
            copy = oldToCopy[cur]
            copy.next = oldToCopy[cur.next]
            copy.random = oldToCopy[cur.random]
            cur = cur.next

        return oldToCopy[head]

        # O(n) time and space
