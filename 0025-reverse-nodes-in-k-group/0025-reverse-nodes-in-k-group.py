# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:
        def reverse(curr):
            prev=None
            while curr!=None:
                next_node=curr.next
                curr.next=prev
                prev=curr
                curr=next_node
            return prev


        def find_kth_node(curr,k):
            while curr!=None and k!=1:
                curr=curr.next
                k-=1
            return curr
       
        temp=head
        prev_node=None
        while temp!=None:
            kth_node=find_kth_node(temp,k)
            if(kth_node==None):
                if prev_node !=None:
                    prev_node.next=temp
                    break
            next_node=kth_node.next
            kth_node.next=None
            new_head=reverse(temp)
            if head==temp:
                head=new_head
            else:
                prev_node.next=new_head
            prev_node=temp
            temp=next_node
        return head
            