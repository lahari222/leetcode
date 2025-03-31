# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None:
            return head
        length=0
        curr=head
        while curr is not None:
            length+=1
            curr=curr.next
        if n==length:
            return head.next
        element=length-n
        curr=head
        for i in range(element-1):
            curr=curr.next
        if curr.next:
            curr.next=curr.next.next
        return head
        