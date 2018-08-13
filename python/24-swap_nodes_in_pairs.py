"""
Given a linked list, swap every two adjacent nodes and return its head.

Example:

Given 1->2->3->4, you should return the list as 2->1->4->3.
Note:

Your algorithm should use only constant extra space.
You may not modify the values in the list's nodes, only nodes itself may be changed.

"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        dummy_node = ListNode(0)
        dummy_node.next = head
        _pre = dummy_node
        node1 = head
        node2 = node1.next
        _next = node2.next
        
        while node1 and node2:
            _pre.next = node2
            node2.next = node1
            node1.next = _next
            
            if _next is None:
                break
            
            _pre = node1
            node1 = _next
            node2 = _next.next
            if node2 is None:
                break
            _next = node2.next
        
        return dummy_node.next
        