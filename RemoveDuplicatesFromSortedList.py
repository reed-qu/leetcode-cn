#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/27 下午6:04
# @Title   : 83. 删除排序链表中的重复元素
# @Link    : https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list/


QUESTION = """
给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。

示例 1:
输入: 1->1->2
输出: 1->2

示例 2:
输入: 1->1->2->3->3
输出: 1->2->3
"""


THINKING = """
引入变量duplicate_nodes记录新的ListNode的头部，previous生成这个ListNode
从头开始遍历，在previous和head的val属性不相等的时候
    previous.next = ListNode(head.val) # 将这个节点实例化
    previous = previous.next           # previous挪到下一个节点
head也往后挪一位head = head.next
最后返回previous的头部duplicate_nodes
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head:
            duplicate_nodes = previous = ListNode(head.val)
            while head:
                if head.val != previous.val:
                    previous.next = ListNode(head.val)
                    previous = previous.next
                head = head.next
            return duplicate_nodes


if __name__ == '__main__':
    from utils.linked_list import LinkedListGen
    s = Solution()
    head = LinkedListGen.list_to_nodes([1, 1, 2, 3, 3])
    duplicate_nodes = s.deleteDuplicates(head)
    print(LinkedListGen.nodes_to_list(duplicate_nodes))
