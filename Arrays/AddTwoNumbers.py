# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        index=0
        newString=0
        while l1:
            newString+=((10**index)*l1.val)
            index+=1
            l1=l1.next
        index=0
        while l2:
            newString+=((10**index)*l2.val)
            index+=1
            l2=l2.next
        val =newString
        node=ListNode(int(str(val)[len(str(val))-1]))
        test=node
        for i in range(len(str(val))-2,-1,-1):
            node.next=ListNode(int(str(val)[i]))
            node=node.next
        
        return test
