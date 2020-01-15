#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/15 上午10:32
# @Title   : 148. 排序链表
# @Link    : https://leetcode-cn.com/problems/sort-list/


QUESTION = """
在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序。

示例 1:
输入: 4->2->1->3
输出: 1->2->3->4

示例 2:
输入: -1->5->3->4->0
输出: -1->0->3->4->5
"""


THINKING = """
...
"""


from utils.linked_list import ListNode, LinkedListGen


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        pass


if __name__ == '__main__':
    s = Solution()
    head = LinkedListGen.list_to_nodes([4, 2, 3, 1])
    result = s.sortList(head)
    print(LinkedListGen.nodes_to_list(result))
