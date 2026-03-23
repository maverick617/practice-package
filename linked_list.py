# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        sum1 = 0
        sum2 = 0
        i = 0
        
        while l1:
            sum1 += l1.val * (10 ** i)
            l1 = l1.next
            i += 1
        
        i = 0
        while l2:
            sum2 += l2.val * (10 ** i)
            l2 = l2.next
            i += 1
        
        sum3 = sum1 + sum2
        
        l3 = []

        if sum3 == 0:
            l3.append(0)
        
        while sum3 > 0:
            l3.append(sum3 % 10)
            sum3 = sum3 // 10
        
        dummy = ListNode(0)
        cur = dummy
        
        for num in l3:
            cur.next = ListNode(num)
            cur = cur.next
        
        return dummy.next