#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/2 上午10:33
# @Title   : 345. 反转字符串中的元音字母
# @Link    : https://leetcode-cn.com/problems/reverse-vowels-of-a-string/


QUESTION = """
编写一个函数，以字符串作为输入，反转该字符串中的元音字母。

示例 1:
输入: "hello"
输出: "holle"

示例 2:
输入: "leetcode"
输出: "leotcede"

说明:
元音字母不包含字母"y"。
"""


THINKING = """
双指针的思想，对称替换一般都是采用双指针的套路

首先把字符串转成列表，这样更方便修改，首位各一个指针开始往中间移动，有以下3种情况
1. 当前首尾都是元音，则交换位置，然后同时移动一位
2. 如果左边不是元音，则左指针移动
3. 如果右边不是元音，则右指针移动

最后再拼接成一个字符串返回
"""


class Solution:
    def reverseVowels(self, s: str) -> str:
        n = len(s)
        if not n:
            return ""
        vowels = ["a", "e", "i", "o", "u"]
        left, right = 0, n - 1
        string = list(s)
        while left < right:
            s_left = s[left]
            s_right = s[right]
            if s_left.lower() in vowels and s_right.lower() in vowels:
                string[left] = s_right
                string[right] = s_left
                left += 1
                right -= 1
                continue
            if s_left.lower() not in vowels:
                left += 1
            if s_right.lower() not in vowels:
                right -= 1

        return ''.join(string)


if __name__ == '__main__':
    s = Solution()
    string = "leetcode"
    print(s.reverseVowels(string))
