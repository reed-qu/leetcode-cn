#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/19 下午12:06
# @Title   : 19. 删除链表的倒数第N个节点
# @Link    : https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list/


QUESTION = """
给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。

示例：
给定一个链表: 1->2->3->4->5, 和 n = 2.
当删除了倒数第二个节点后，链表变为 1->2->3->5.

说明：
给定的 n 保证是有效的。

进阶：
你能尝试使用一趟扫描实现吗？
"""


THINKING = """
问题在于如何遍历一遍之后回头找到倒数n内个位置，然后倒数n+1.next = 倒数n-1就可以
思路是从头往后遍历，用列表记录每一次的节点，然后回头用n来索引就可以了
但是列表的两头，第一位和最后一位需要特殊处理，还有链表只有1个节点的时候
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        nodes = []
        size = 0
        while head:
            size += 1
            nodes.append(head)
            head = head.next

        if n == 1:
            if size == 1:
                return None
            else:
                nodes[-2].next = None
        elif n == size:
            return nodes[1]
        else:
            nodes[-n-1].next = nodes[-n+1]
        return nodes[0]


if __name__ == '__main__':
    s = Solution()
    head = ListNode(1)
    x = 1
    print(s.removeNthFromEnd(head, x))
