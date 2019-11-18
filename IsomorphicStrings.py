#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/18 上午10:20
# @Title   : 205. 同构字符串
# @Link    : https://leetcode-cn.com/problems/isomorphic-strings/


QUESTION = """
给定两个字符串 s 和 t，判断它们是否是同构的。
如果 s 中的字符可以被替换得到 t ，那么这两个字符串是同构的。
所有出现的字符都必须用另一个字符替换，同时保留字符的顺序。两个字符不能映射到同一个字符上，但字符可以映射自己本身。

示例 1:
输入: s = "egg", t = "add"
输出: true

示例 2:
输入: s = "foo", t = "bar"
输出: false

示例 3:
输入: s = "paper", t = "title"
输出: true

说明:
你可以假设 s 和 t 具有相同的长度。
"""


THINKING = """
思路是用哈希表来表示映射
有2种情况需要特殊处理一下就可以了
1. s = "aa", t = "ab", 这是正序的情况，第一步"a" -> "a", 下一步的时候发现"a" -> "b"则违背，则返回False
2. s = "ab", t = "aa", 这是倒序的情况，第一步"a" -> "a", 下一步的时候发现"b" -> "a"
    这里，"b"没有建立映射且"a"已经有了某个 x 对之的映射，则返回False
排除以上两种情况，则正常建立映射  
"""


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        l = len(s)
        letter_map = {}
        for i in range(l):
            # 情况 1
            if s[i] in letter_map and t[i] != letter_map[s[i]]:
                return False
            # 情况 2
            if s[i] not in letter_map and t[i] in letter_map.values():
                return False
            # 正常建立映射
            letter_map[s[i]] = t[i]
        return True


if __name__ == '__main__':
    s = Solution()
    str_s = "bar"
    str_t = "foo"
    print(s.isIsomorphic(str_s, str_t))
