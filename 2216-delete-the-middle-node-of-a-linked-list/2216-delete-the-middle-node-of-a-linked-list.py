# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        length=0
        curr=head
        while curr is not None:
            length+=1
            curr=curr.next
        mid=length//2
        if mid==0:
            return head.next
        curr=head
        for i in range(mid-1):
            curr=curr.next
        if curr.next:
            curr.next=curr.next.next
        return head
        