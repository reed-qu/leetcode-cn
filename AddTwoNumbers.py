#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/20 下午6:32
# @Title   : 2. 两数相加
# @Link    : https://leetcode-cn.com/problems/add-two-numbers/


QUESTION = """
给出两个 非空 的链表用来表示两个非负的整数
其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：
输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807
"""


THINKING = """
个人的思路比较死板，即是按着题设的流程去走
1. 引入multiplier乘子，将l1和l2这两个链表倒装成数字，然后相加为total
2. 然后把数字反着生成为一个新的链表就行了

这样当然是有隐患的，如果链表很长的话，就表示数字也要很大才可以
对于Python来说还好，如果对于强类型语言来说就有溢出的风险
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num_l1 = 0
        num_l2 = 0

        multiplier = 1
        while l1:
            num_l1 = num_l1 + multiplier * l1.val
            l1 = l1.next
            multiplier *= 10

        multiplier = 1
        while l2:
            num_l2 = num_l2 + multiplier * l2.val
            l2 = l2.next
            multiplier *= 10

        total = num_l1 + num_l2
        head = ListNode(0)
        curr = head
        while 1:
            curr.next = ListNode(total % 10)
            curr = curr.next
            total = total // 10
            if not total:
                break
        return head.next


if __name__ == '__main__':
    s = Solution()
    l1 = ListNode(2)
    l1_1 = ListNode(4)
    l1_2 = ListNode(3)
    l1.next = l1_1
    l1_1.next = l1_2

    l2 = ListNode(5)
    l2_1 = ListNode(6)
    l2_2 = ListNode(4)
    l2.next = l2_1
    l2_1.next = l2_2

    new_list_node = s.addTwoNumbers(l1, l2)
    while new_list_node:
        print(new_list_node.val)
        new_list_node = new_list_node.next
