# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None

        while curr is not None:
            # temp store next node
            nextNode = curr.next

            # point curr to prev
            curr.next = prev
            
            # point prev to current node
            prev = curr

            # make curr the next node
            curr = nextNode
        
        return prev


        