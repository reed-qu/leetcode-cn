#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/12 下午2:13
# @Title   : 242. 有效的字母异位词
# @Link    : https://leetcode-cn.com/problems/valid-anagram/


QUESTION = """
给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词

示例 1:
输入: s = "anagram", t = "nagaram"
输出: true

示例 2:
输入: s = "rat", t = "car"
输出: false

说明:
你可以假设字符串只包含小写字母。

进阶:
如果输入字符串包含 unicode 字符怎么办？你能否调整你的解法来应对这种情况
"""


THINKING = """
首先什么是"字母异位词"，就是字母都是相同的，但是顺序可以是不同的
解题思路就是把一个字符串转为每个字符的频率，生成一张哈希表
然后遍历另外一个字符串，如果存在哈希表中则频率-1，如果频率被减为小于0了，则返回False
否则遍历完则返回True
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 都是空，则返回True
        if not s and not t:
            return True
        # 有一个为空，则返回False
        if not s or not t:
            return False
        # 二者长度不同则返回True
        if len(s) != len(t):
            return False

        frequency = {}
        for each in s:
            if each not in frequency:
                frequency[each] = 1
            else:
                frequency[each] += 1

        for each in t:
            if each in frequency:
                frequency[each] -= 1
                current_number = frequency[each]
                if current_number < 0:
                    return False
            else:
                return False
        return True


if __name__ == '__main__':
    s = Solution()
    string = "anagram"
    t = "nagaram"
    print(s.isAnagram(string, t))
