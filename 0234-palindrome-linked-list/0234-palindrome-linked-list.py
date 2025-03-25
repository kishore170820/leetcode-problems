# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return True
        left,right=head,head
        while right and right.next:
            left=left.next
            right=right.next.next
        prev=None
        while left:
            next_node=left.next
            left.next=prev
            prev=left
            left=next_node
        while prev:
            if head.val!=prev.val:
                return False
            head=head.next
            prev=prev.next
        return True