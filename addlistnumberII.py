# Definition for singly-linked list.
# To change list to int maybe much easier
class ListNode(object):
    def __int__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l1_stack = []
        l2_stack = []
        while l1:
            l1_stack.append(l1.val)
            l1 = l1.next
        while l2:
            l2_stack.append(l2.val)
            l2 = l2.next
        header = None
        left = 0
        i = len(l1_stack) - 1
        j = len(l2_stack) - 1
        while i >= 0 and j >= 0:
            solution = l1_stack[i] + l2_stack[j] + left
            newnode = ListNode(solution % 10)
            newnode.next = header
            left = solution / 10
            i -= 1
            j -= 1
            header = newnode
        while i >= 0:
            solution = l1_stack[i] + left
            newnode = ListNode(solution % 10)
            newnode.next = header
            left = solution / 10
            i -= 1
            header = newnode
        while j >= 0:
            solution = l2_stack[j] + left
            newnode = ListNode(solution % 10)
            newnode.next = header
            left = solution / 10
            j -= 1
            header = newnode
        if left > 0:
            newnode = ListNode(left)
            newnode.next = header
            header = newnode
        return header
