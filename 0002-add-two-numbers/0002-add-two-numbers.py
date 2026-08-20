# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        num1, num2 = 0, 0
        curr = l1
        tens = 1
        while curr:
            num1 += tens * curr.val
            tens *= 10
            curr = curr.next
        curr = l2
        tens = 1
        while curr:
            num2 += tens * curr.val
            tens *= 10
            curr = curr.next
        num = num1 + num2
        head = None
        if num == 0:
            return ListNode(0, None)
        else:
            head = ListNode(num % 10)
            num //= 10
        curr = head
        while num > 0:
            curr.next = ListNode(num % 10, None)
            curr = curr.next
            num //= 10
        return head
        