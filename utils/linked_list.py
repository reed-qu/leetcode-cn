#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/27 下午6:50
# @Title   : 链表


from typing import List


class ListNode(object):
    """
    链表节点的定义
    """

    def __init__(self, x):
        self.val = x
        self.next = None


    def __repr__(self):
        return f"<ListNode> val: {self.val}"


class LinkedListGen(object):
    """
    链表生成器，快速生成一个可供调试的链表
    """

    @classmethod
    def list_to_nodes(cls, items: List):
        size = len(items)
        if items:
            head = current = ListNode(items[0])
            for i in range(1, size-1):
                current.next = ListNode(items[i])
                current = current.next
            return head
        return None


    @classmethod
    def nodes_to_list(cls, head: ListNode):
        nodes = []
        while head:
            nodes.append(head.val)
            head = head.next
        return nodes


if __name__ == '__main__':
    a = LinkedListGen.list_to_nodes([1, 2, 3, 4])
    print(LinkedListGen.nodes_to_list(a))
