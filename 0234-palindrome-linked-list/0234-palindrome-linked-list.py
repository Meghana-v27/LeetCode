# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:
        def reverse_ll(cur):
            prev=None
            while cur!=None:
                temp=cur.next
                cur.next=prev
                prev=cur
                cur=temp
            return prev
        slow=head
        fast=head
        while fast!=None and fast.next!=None:
            slow=slow.next
            fast=fast.next.next
        head2=reverse_ll(slow)
        while head2!=None:
            if head.val!=head2.val:
                return False
            head=head.next
            head2=head2.next
        return True