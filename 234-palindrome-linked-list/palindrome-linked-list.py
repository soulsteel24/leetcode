# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True
        s = head
        f = head
        while f and f.next:
            s= s.next
            f = f.next.next
        
        prev = None
        current = s
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        first_half = head
        second_half = prev

        while second_half:
            if first_half.val != second_half.val:
                return False
            first_half = first_half.next
            second_half = second_half.next
        return True

            