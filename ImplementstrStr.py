#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/30 下午1:07
# @Title   : 28. 实现 strStr()
# @Link    : https://leetcode-cn.com/problems/implement-strstr/


QUESTION = """
实现 strStr() 函数。
给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。

示例 1:
输入: haystack = "hello", needle = "ll"
输出: 2

示例 2:
输入: haystack = "aaaaa", needle = "bba"
输出: -1

说明:
当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。
对于本题而言，当 needle 是空字符串时我们应当返回 0 。这与C语言的 strstr() 以及 Java的 indexOf() 定义相符。
"""


THINKING = """
strStr:
从haystack头部开始遍历，每次比较i:i+len(needle)是否与needle相同，相同则返回索引，遍历到最后也没有匹配的话返回-1

strStr_2:
从haystack头部开始遍历，比较i:i+len(needle)是否与needle相同，与strStr不同的是，如果不同的话，下一次所以挪到i+len(needle)
判断第i+len(needle)个字符是否在needle中，如果存在，则i+=1，如果不存在则跳过中间字符，直接从第i+len(needle)处开始往后遍历
相较于strStr速度更快一些
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        if not haystack:
            return -1
        l_h, l_n = len(haystack), len(needle)
        for i in range(l_h):
            if haystack[i:i+l_n] == needle:
                return i
        return -1

    def strStr_2(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        if not haystack:
            return -1
        l_h, l_n = len(haystack), len(needle)
        i = 0
        while i <= l_h - l_n:
            if haystack[i:i+l_n] == needle:
                return i
            else:
                if haystack[i+l_n] in needle:
                    i += 1
                else:
                    i += l_n
        return -1


if __name__ == '__main__':
    s = Solution()
    haystack = "aaaaab"
    needle = "ab"
    print(s.strStr(haystack, needle))
    print(s.strStr_2(haystack, needle))
