"""
You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Follow up:
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

Example:

Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l1_list = []
        l2_list = []
        while l1:
            l1_list.append(l1.val)
            l1 = l1.next
        while l2:
            l2_list.append(l2.val)
            l2 = l2.next
        pre = None
        cur = None
        carry = 0
        while l1_list or l2_list:
            tmp = 0
            if l1_list:
                tmp += l1_list.pop()
            if l2_list:
                tmp += l2_list.pop()
            if carry:
                tmp += carry
                carry = 0
            carry = tmp // 10
            tmp = tmp % 10
            head = ListNode(tmp)
            
            if not cur:
                cur = head
            else:
                head.next = cur
                cur = head
        if carry:
            head = ListNode(carry)
            head.next = cur
            cur = head
        return cur


if __name__ == "__main__":


    tmp1 = ListNode(7)
    tmp2 = ListNode(2)
    tmp3 = ListNode(4)
    tmp4 = ListNode(3)

    tmp1.next = tmp2
    tmp2.next = tmp3
    tmp3.next = tmp4

    a = ListNode(5)
    b = ListNode(6)
    c = ListNode(4)
    a.next = b
    b.next = c

    s = Solution()
    res = s.addTwoNumbers(tmp1, a)

    while res:
        print(res.val)
        res = res.next