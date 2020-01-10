#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/10 下午6:18
# @Title   : 203. 移除链表元素
# @Link    : https://leetcode-cn.com/problems/remove-linked-list-elements/


QUESTION = """
删除链表中等于给定值 val 的所有节点。

示例:
输入: 1->2->6->3->4->5->6, val = 6
输出: 1->2->3->4->5
"""


THINKING = """
如果要删除的节点是中间节点的话，那没什么可说的
主要就是要考虑头节点和尾节点，要想解决这个问题，就是在头部的前一位给一个原始节点origin

然后用previous和current两个指针来表示origin和head
开始遍历head，每次结束都要移动current = current.next
    如果head.val == val则，previous.next = current.next，表示跳过current当前的节点
    否则的话，previous = current
不管怎样，每次结束都要移动current = current.next
"""


from utils.linked_list import ListNode, LinkedListGen


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        origin = ListNode(0)
        origin.next = head

        previous, current = origin, head
        while current:
            if current.val == val:
                previous.next = current.next
            else:
                previous = current
            current = current.next

        return origin.next


if __name__ == '__main__':
    s = Solution()
    head = LinkedListGen.list_to_nodes([1, 2, 3, 4, 3, 4, 5])
    val = 3
    result = s.removeElements(head, val)
    print(LinkedListGen.nodes_to_list(result))
