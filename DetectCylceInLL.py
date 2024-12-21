from typing import Optional
class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        dummy = ListNode(0,head)
        my_set = set()

        pointer = dummy
        while pointer:
            if pointer in my_set:
                return True
            my_set.add(pointer)
            pointer = pointer.next

        return False