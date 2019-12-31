#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/21 上午11:41
# @Title   : 3. 无重复字符的最长子串
# @Link    : https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/


QUESTION = """
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:
输入: "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

示例 2:
输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。

示例 3:
输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串
"""


THINKING = """
思路是引入两个指针，一个慢指针，指向最长不重复子串的起始位置，一个快指针，指向最长不重复子串的结束位置
引入哈希表，哈希表的键值关系是：当前不重复子串的字符: 当前不重复子串的索引(同时也是当前这个子串的长度)

i留在原地，j往前走，如果在哈希表中不存在则加入一条记录，j自增1，不重复子串的索引自增
如果在哈希表中存在的话则 i, j要重新设置，设置的要求就是看与当前子串重复的字符的索引，比如和第一个字符重复的话，就+1
和第二个字符重复就+2，并且tmp 和 哈希表都要重置

同时每次循环比较tmp和result的大小，每次都取最大的长度最为result
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i, j = 0, 0
        l = len(s)
        if not s:
            return 0

        result = 0
        tmp = 0
        tmp_set = {}
        while i < l and j < l:
            tmp_letter = s[j]
            if tmp_letter in tmp_set:
                i += tmp_set[tmp_letter] + 1
                j = i
                tmp = 0
                tmp_set = {}
            else:
                tmp_set[tmp_letter] = tmp
                j += 1
                tmp += 1
            if tmp > result:
                result = tmp
        return result


if __name__ == '__main__':
    s = Solution()
    string = "bbtablud"
    print(s.lengthOfLongestSubstring(string))
