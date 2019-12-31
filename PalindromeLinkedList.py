#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/20 上午10:35
# @Title   : 234. 回文链表
# @Link    : https://leetcode-cn.com/problems/palindrome-linked-list/


QUESTION = """
请判断一个链表是否为回文链表

示例 1:
输入: 1->2
输出: false

示例 2:
输入: 1->2->2->1
输出: true

进阶：
你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？
"""


THINKING = """
方法有很多，个人有2种
1. 不考虑O(1)空间复杂度的限制，可以引入一个列表，list == list[::-1]即可
2. 考虑复杂度，用数学的方法，从头部head开始遍历，正序asc的构建方法为*10+当前数字
逆序desc的构建方法为通过一个multiplier的一个乘数，每次向数字的前面加一位，拿1->2->2->1举例来说

正序：1 -> 1*10+2 -> 12*10+2 -> 122*10+1     -> 1221
逆序：1 -> 2*10+1 -> 2*100+21 -> 1*1000+221  -> 1221
比较二者即可，如果链表较长，有数字较大的隐患，这也是为什么测试效率较低

看了大家的解答方式，正解是引入快慢指针，移动速度：快 = 2*慢，这样快指针走到末尾的时候，慢指针走到链表中间
同时慢指针走的时候翻转链表，然后一部分是从头到中间，另一部分是从中间到末尾，比较二链表是否相同即可
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        asc = 0
        desc = 0
        multiplier = 1

        while head != None:
            asc = asc * 10 + head.val
            desc = desc + multiplier * head.val
            multiplier *= 10
            head = head.next
        return asc == desc


if __name__ == '__main__':
    s = Solution()
    head = ListNode(1)
    l1 = ListNode(2)
    l2 = ListNode(2)
    l3 = ListNode(1)
    head.next = l1
    l1.next = l2
    l2.next = l3
    print(s.isPalindrome(head))
