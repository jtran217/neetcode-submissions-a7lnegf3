# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # node has tail
        # need to basically reverse where tail points to.
        # End of tail usually points to null so shall make new null node

        current = head
        prev = None
        while current:
            # Store Current.next in variable
            # change current.next to prev
            # set current = variable containing current.next

            tmp = current.next
            current.next = prev
            prev = current
            current = tmp
        return prev
        
