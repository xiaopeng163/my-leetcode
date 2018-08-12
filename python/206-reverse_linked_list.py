

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return []
        _pre = None
        _cur = head
        _next = head.next
        while _cur.next is not None:
            _cur.next = _pre
            _pre = _cur
            _cur = _next
            _next = _next.next
        _cur.next = _pre
        res = [_cur.val]
        while _cur.next:
            _cur = _cur.next
            res.append(_cur.val)
        return res


if __name__ == "__main__":
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    s = Solution()

    print(s.reverseList(node1))