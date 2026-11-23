# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        c1=headA
        c2=headB
        while c1!=c2:
            c1=c1.next
            c2=c2.next
            if c1==c2:
                return c1
            if c1==None:
                c1=headB
            if c2==None:
                c2=headA
        return c1