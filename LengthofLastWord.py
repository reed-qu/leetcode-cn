#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/6 上午11:33
# @Title   : 58. 最后一个单词的长度
# @Link    : https://leetcode-cn.com/problems/length-of-last-word/


QUESTION = """
给定一个仅包含大小写字母和空格 ' ' 的字符串，返回其最后一个单词的长度
如果不存在最后一个单词，请返回 0 。

说明：一个单词是指由字母组成，但不包含任何空格的字符串。

示例:
输入: "Hello World"
输出: 5
"""


THINKING = """
先左右去空格，再按照空格分隔取最后一个求长度
"""


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        result = s.split(" ")[-1]
        return len(result)


if __name__ == '__main__':
    s = Solution()
    string = "Hello World"
    print(s.lengthOfLastWord(string))
