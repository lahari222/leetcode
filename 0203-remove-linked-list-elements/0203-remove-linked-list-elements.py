# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy_node=ListNode(-1)
        dummy_node.next=head
        temp=dummy_node
        while temp.next is not None:
            if temp.next.val==val:
                temp.next=temp.next.next
            else:
                temp=temp.next
        return dummy_node.next
        
        