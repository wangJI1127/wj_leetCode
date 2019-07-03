"""
你有两个用链表代表的整数，其中每个节点包含一个数字。数字存储按照在原来整数中相反的顺序，使得第一个数字位于链表的开头。写出一个函数将两个整数相加，用链表形式返回和。

样例
样例 1:

输入: 7->1->6->null, 5->9->2->null
输出: 2->1->9->null
样例解释: 617 + 295 = 912, 912 转换成链表:  2->1->9->null
样例 2:

输入:  3->1->5->null, 5->9->2->null
输出: 8->0->8->null
样例解释: 513 + 295 = 808, 808 转换成链表: 8->0->8->null
"""
"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    @param l1: the first list
    @param l2: the second list
    @return: the sum list of l1 and l2
    """
    def addLists(self, l1, l2):
        # write your code here
        carry = 0
        l = list()
        while(l1 and l2):
            sum = l1.val + l2.val + carry
            l.append(sum % 10)
            carry = 1 if sum // 10 == 1 else 0
            l1 = l1.next
            l2 = l2.next
        while l1:
            sum = l1.val + carry
            l.append(sum % 10)
            carry = 1 if sum // 10 == 1 else 0
            l1 = l1.next
        while l2:
            sum = l2.val + carry
            l.append(sum % 10)
            carry = 1 if sum // 10 == 1 else 0
            l2 = l2.next
        if carry == 1:
            l.append(1)
        l.reverse()
        for i in range(len(l)):
            if i == 0:
                l3 = ListNode(l[i])
            else:
                l3 = ListNode(l[i], l3)
        return l3



