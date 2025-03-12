# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res=[]
        curr=head
        while curr:
            res.append(curr.val)
            curr=curr.next
        res.sort()
        curr=head
        for i in range(len(res)):
            curr.val=res[i]
            curr=curr.next
        return head