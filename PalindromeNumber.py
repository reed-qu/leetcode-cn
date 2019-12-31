#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/28 下午8:13
# @Title   : 9. 回文数
# @Link    : https://leetcode-cn.com/problems/palindrome-number/


QUESTION = """
判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数

示例 1:
输入: 121
输出: true

示例 2:
输入: -121
输出: false
解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。

示例 3:
输入: 10
输出: false
解释: 从右向左读, 为 01 。因此它不是一个回文数。

进阶:
你能不将整数转为字符串来解决这个问题吗？
"""


THINKING = """
首先要确定负数肯定不可以
其次结尾是0，且数字本身并不是0的情况也是不行的，不符合题设，这两种情况都直接返回False

解决办法有很多，比如转成字符串，用Python的内置方法很容易实现，或者是把数字翻转然后比较大小即可，但是都不是最高效的
思路是既然是正反对称的，那么翻转一半儿的数字，应该和数字的前半段是相等的，那么啥时候才知道某一次循环到了数字的一半儿呢
就是：数字本身 < 翻转的数字时 就停止取数动作进行翻转
数字长度为偶数的话，当再取一次，数字本身就比翻转的数字少2位了，比如2112，翻转的数字是21，数字本身为21，return 21==21
数字长度为奇数的话，按照上面这种办法的话，12321 翻转的数字是123，数字本身是12，但是可以return 12==123//10

注意：Python3中向下取整为 //，数字翻转参考ReverseInteger.py
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reverse_num = 0
        while x > reverse_num:
            tail = x % 10
            reverse_num = reverse_num * 10 + tail
            x = x // 10

        return x == reverse_num or x == reverse_num // 10


if __name__ == '__main__':
    s = Solution()
    print(s.isPalindrome(12321))
