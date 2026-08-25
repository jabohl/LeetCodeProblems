# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        Delete the given (non-tail) node from a singly-linked list by copying
        the next node's value into this node and bypassing the next node.

        :type node: ListNode
        :rtype: None
        """
        if node is None or node.next is None:
            # This method cannot delete the tail node.
            raise ValueError("Cannot delete the tail node with this method")

        next_node = node.next
        node.val = next_node.val
        node.next = next_node.next
