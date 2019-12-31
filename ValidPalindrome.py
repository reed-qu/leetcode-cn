#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/29 上午10:57
# @Title   : 125. 验证回文串
# @Link    : https://leetcode-cn.com/problems/valid-palindrome/


QUESTION = """
给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写
说明：本题中，我们将空字符串定义为有效的回文串。

示例 1:
输入: "A man, a plan, a canal: Panama"
输出: true

示例 2:
输入: "race a car"
输出: false
"""


THINKING = """
首先只考虑字母和数字字符，可以用Python默认的ASCII码来比较，即 "a" <= x <= "z" 并不会报错
isValidStr即是判断字符是否合法的方法

首尾各置一个指针，同时向中间移动，移动的条件为左指针要在右指针的左边，即首索引<尾索引
初始化左右两部分的字符为空，每次移动一个合法字符则添加一个到对应的字符中
不停移动指针，当2指针指向的字符都是合法的情况，再添加到left, right中，否则分情况移动指针
最后return left == right
"""


class Solution:
    def isValidStr(self, s: str) -> bool:
        return "a" <= s <= "z" or "0" <= s <= "9"

    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s)-1
        x = s.lower()
        left, right = "", ""
        while i < j:
            if self.isValidStr(x[i]) and self.isValidStr(x[j]):
                left += x[i]
                right += x[j]
                i += 1
                j -= 1
            elif self.isValidStr(x[i]) and not self.isValidStr(x[j]):
                j -= 1
            elif not self.isValidStr(x[i]) and self.isValidStr(x[j]):
                i += 1
            else:
                i += 1
                j -= 1
        return left == right


if __name__ == '__main__':
    s = Solution()
    print(s.isPalindrome("A man, a plan, a canal: Panama"))
    print(s.isPalindrome("race a car"))
