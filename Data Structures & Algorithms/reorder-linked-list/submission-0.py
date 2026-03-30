# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        # Find middle point
        slow,fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Set second graph
        second = slow.next
        # because the start of second graph will point to Null becuase we plan to reverse it.
        prev = slow.next = None

        # Reverse second half
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        
        first,second = head, prev

        while second:
            tmp1,tmp2 = first.next, second.next
            first.next = second
            # Inserting between first and first.next
            second.next = tmp1 
            first, second = tmp1, tmp2 




        