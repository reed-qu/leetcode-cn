#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/19 上午10:56
# @Title   : 290. 单词规律
# @Link    : https://leetcode-cn.com/problems/word-pattern/


QUESTION = """
给定一种规律 pattern 和一个字符串 str ，判断 str 是否遵循相同的规律。
这里的 遵循 指完全匹配，例如，pattern 里的每个字母和字符串 str 中的每个非空单词之间存在着双向连接的对应规律。

示例1:
输入: pattern = "abba", str = "dog cat cat dog"
输出: true

示例 2:
输入:pattern = "abba", str = "dog cat cat fish"
输出: false

示例 3:
输入: pattern = "aaaa", str = "dog cat cat dog"
输出: false

示例 4:
输入: pattern = "abba", str = "dog dog dog dog"
输出: false

说明:
你可以假设 pattern 只包含小写字母， str 包含了由单个空格分隔的小写字母。
"""


THINKING = """
和 205. 同构字符串 IsomorphicStrings.py 一毛一样
都是建立映射关系
"""


class Solution:
    def wordPattern(self, pattern: str, string: str) -> bool:
        strings = string.split(" ")
        l = len(pattern)
        if len(strings) != l:
            return False

        pat_map = {}
        for i in range(l):
            current_pat = pattern[i]
            if current_pat in pat_map and strings[i] != pat_map[current_pat]:
                return False
            if current_pat not in pat_map and strings[i] in pat_map.values():
                return False
            pat_map[current_pat] = strings[i]
        return True


if __name__ == '__main__':
    s = Solution()
    pattern = "abba"
    string = "dog dog dog dog"
    print(s.wordPattern(pattern, string))
