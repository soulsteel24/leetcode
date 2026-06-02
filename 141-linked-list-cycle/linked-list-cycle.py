# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        s = head
        f = head

        while f and f.next is not None:
            s = s.next
            f = f.next.next
            if f == s:
                return True
        return False

        