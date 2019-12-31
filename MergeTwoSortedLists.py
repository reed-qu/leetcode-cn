#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/29 上午11:57
# @Title   : 21. 合并两个有序链表
# @Link    : https://leetcode-cn.com/problems/merge-two-sorted-lists/


QUESTION = """
将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的

示例：
输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4
"""


THINKING = """
这里主要为递归的思想
1. 如果l1或者l2为None的话，即直接返回另外一个ListNode
2. 比较当前节点的大小，用小的内个ListNode.next与另外一个继续做merge，且返回小的内个ListNode

注意：这里也实现了一个链表的append方法，即判断加入数据是否为head，如果head不存在则置为head，否则遍历到最后一个节点
将最后一个节点的next设置成添加进去的Node
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedNode(object):
    def __init__(self):
        self.head = None

    def append(self, x):
        n = ListNode(x)
        if not self.head:
            self.head = n
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = n


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2


if __name__ == '__main__':
    l1 = LinkedNode()
    l1.append(1)
    l1.append(2)
    l1.append(4)

    l2 = LinkedNode()
    l2.append(1)
    l2.append(3)
    l2.append(4)

    head = l1.head
    while head:
        print(head.val)
        head = head.next


