#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/3 上午11:01
# @Title   : 141. 环形链表
# @Link    : https://leetcode-cn.com/problems/linked-list-cycle/


QUESTION = """
给定一个链表，判断链表中是否有环。
为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）
如果 pos 是 -1，则在该链表中没有环。

示例 1：
输入：head = [3,2,0,-4], pos = 1
输出：true
解释：链表中有一个环，其尾部连接到第二个节点。即是: 3 -> 2 -> 0 -> -4 -> 2 ...

示例 2：
输入：head = [1,2], pos = 0
输出：true
解释：链表中有一个环，其尾部连接到第一个节点。即是: 1 -> 2 -> 1 -> 2 ...

示例 3：
输入：head = [1], pos = -1
输出：false
解释：链表中没有环。

进阶：
你能用 O(1)（即，常量）内存解决此问题吗？
"""


THINKING = """
用哈希表来构建每一个节点是否重复出现了

有环，那必定是引用回去了，内存地址肯定是一样的，所以哈希表中的key就内存地址
每次遍历下一个节点，如果地址已经存在哈希表中了，那么肯定是存在环，导致引用回来了，返回True
否则没有环，就一定能找到最后的None，就返回False就可以了
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        node_addr = {}
        while head is not None:
            if id(head) in node_addr:
                return True
            else:
                node_addr[id(head)] = 1
            head = head.next
        return False


if __name__ == '__main__':
    s = Solution()
    head = ListNode(1)
    print(s.hasCycle(head))
