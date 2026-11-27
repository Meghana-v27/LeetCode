# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        res=ListNode(-1)
        curr=res
        pq=[]
        for i in range(0,len(lists)):
            if lists[i]!=None:
                heapq.heappush(pq,(lists[i].val,i,lists[i]))
        while len(pq)!=0:
            value,i,node=heapq.heappop(pq)
            curr.next=node
            curr=curr.next
            if node.next!=None:
                heapq.heappush(pq,(node.next.val,i,node.next))
        return res.next