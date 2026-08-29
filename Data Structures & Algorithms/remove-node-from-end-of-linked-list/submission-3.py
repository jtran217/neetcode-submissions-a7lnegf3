# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        front = dummy
        tail = head

        while n > 0:
            tail = tail.next
            n-=1
        
        
        while tail:
            front = front.next
            tail = tail.next
        
        front.next = front.next.next

        return dummy.next