# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr=head
        while curr:
            res=head
            while res!=curr:
                if res.val>curr.val:
                    res.val,curr.val=curr.val,res.val
                res=res.next
            curr=curr.next
        return head
        