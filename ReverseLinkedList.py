#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/11 上午10:25
# @Title   : 206. 反转链表
# @Link    : https://leetcode-cn.com/problems/reverse-linked-list/


QUESTION = """
反转一个单链表。

示例:
输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL

进阶:
你可以迭代或递归地反转链表。你能否用两种方法解决这道题？
"""


THINKING = """
迭代的方式实现
引入临时变量tmp，cur, pre
初始化pre=None 从头往后遍历的过程中，pre跟着往前走，走到最后即是新的head，最后一个为None，所以初始化为None
初始化cur=head
从头开始遍历，每次把中间的链接拆开，拆成前后两部分，tmp是后面的链表，cur是当前节点
前面的部分，把pre赋值到cur.next，反向连接上
后面的部分重新赋值给cur，继续迭代

举例:
原始链表为: 1->2->3->None, pre = None, cur就是这个链表
1. tmp: 2->3->None; pre: 1->None;       cur: 2->3->None
2. tmp: 3-None;     pre: 2->1->None;    cur: 3-None
3. tmp: None;       pre: 3->2->1->None; cur: None
翻转成功
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        pre = None
        cur = head
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre


if __name__ == '__main__':
    s = Solution()
    head = ListNode(1)
    l1 = ListNode(2)
    l2 = ListNode(3)
    l1.next = l2
    head.next = l1
    print(s.reverseList(head))
