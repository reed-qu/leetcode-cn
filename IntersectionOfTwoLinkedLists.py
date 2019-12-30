#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/9 上午10:12
# @Title   : 160. 相交链表
# @Link    : https://leetcode-cn.com/problems/intersection-of-two-linked-lists/


QUESTION = """
编写一个程序，找到两个单链表相交的起始节点。

示例 1：
输入：intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
输出：Reference of the node with value = 8
输入解释：相交节点的值为 8 （注意，如果两个列表相交则不能为 0）
    从各自的表头开始算起，链表 A 为 [4,1,8,4,5]，链表 B 为 [5,0,1,8,4,5]。在 A 中，相交节点前有 2 个节点；在 B 中，相交节点前有 3 个节点。

示例 2：
输入：intersectVal = 2, listA = [0,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
输出：Reference of the node with value = 2
输入解释：相交节点的值为 2 （注意，如果两个列表相交则不能为 0）
    从各自的表头开始算起，链表 A 为 [0,9,1,2,4]，链表 B 为 [3,2,4]。在 A 中，相交节点前有 3 个节点；在 B 中，相交节点前有 1 个节点。

示例 3：
输入：intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
输出：null
输入解释：从各自的表头开始算起，链表 A 为 [2,6,4]，链表 B 为 [1,5]。由于这两个链表不相交，所以 intersectVal 必须为 0，而 skipA 和 skipB 可以是任意值。
解释：这两个链表不相交，因此返回 null。

注意：
如果两个链表没有交点，返回 null.
在返回结果后，两个链表仍须保持原有的结构。
可假定整个链表结构中没有循环。
程序尽量满足 O(n) 时间复杂度，且仅用 O(1) 内存。
"""


THINKING = """
如果相交点之前，两个链表有同样的长度，那么就依次比较内存地址就可以了，第一个内存地址相同的地方就是相交点
但是这里二者不一样长，思路就从这里打开，就是想办法让二者同时走到相交点上
假设有2个人，从链表的头部走到尾部，因为相交的特性，每个人都把A, B两个链表分别走一遍
那么该人在走另外一个链表的时候，走到相交点，另外一个人也一定会走到这里，因为此时二者长度一致了
举例:
A: [1, 2, 9, 8, 7]
B: [1, 9, 8, 7]
拼接之后是:
AB: [1, 2, 9, 8, 7, 1, 9, 8, 7]
BA: [1, 9, 8, 7, 1, 2, 9, 8, 7]
                       ↑
显而易见，此点就是相交点
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        ha, hb = headA, headB
        while ha != hb:
            ha = ha.next if ha else headB
            hb = hb.next if hb else headA
        return ha


if __name__ == '__main__':
    s = Solution()
    headA = ListNode(1)
    headB = ListNode(2)
    print(s.getIntersectionNode(headA, headB))
