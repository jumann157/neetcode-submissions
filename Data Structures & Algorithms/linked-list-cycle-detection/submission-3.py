# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        pointer_a, pointer_b = head, head

        while pointer_b:
            print(f"a: {pointer_a.val}, b: {pointer_b.val}")
            pointer_a = pointer_a.next
            pointer_b = pointer_b.next.next if pointer_b.next else None
            if pointer_b and pointer_a and pointer_a == pointer_b:
                return True
        
        return False
