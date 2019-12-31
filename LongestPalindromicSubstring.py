#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/25 下午2:56
# @Title   : 5. 最长回文子串
# @Link    : https://leetcode-cn.com/problems/longest-palindromic-substring/


QUESTION = """
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000

示例 1：
输入: "babad"
输出: "bab"

注意: "aba" 也是一个有效答案。

示例 2：
输入: "cbbd"
输出: "bb"
"""


THINKING = """
理解成一个动态规划的过程，借鉴用户liweiwei1419在此题下的动态规划部分的作答
l, r 表示left, right索引，题设就是说找到最长的s[l:r+1]，且其为回文串

首先根据回文串的特点，如果s[l] == s[r] 且 l+1, r-1索引的字符串也同样为回文串
主要此时l+1 < r-1这个特点(左索引始终不能超越右索引)，否则的话，就表示l, r之间有1个或0个字符，此时肯定是回文的

同时引入二维列表，初始化全是False，然后过程中如果是回文串则记录l, r的索引为True
引入longest_l常量，记录回文串的最长长度，如果新的要比这个要长，则替换掉
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        size = len(s)
        if size <= 1:
            return s
        dp = [[False for _ in range(size)] for _ in range(size)]

        longest_l = 1
        res = s[0]

        for r in range(1, size):
            for l in range(r):
                if s[l] == s[r] and (l + 1 >= r - 1 or dp[l + 1][r - 1]):
                    dp[l][r] = True
                    cur_len = r - l + 1
                    if cur_len > longest_l:
                        longest_l = cur_len
                        res = s[l:r + 1]
        return res


if __name__ == '__main__':
    s = Solution()
    string = "ababad"
    print(s.longestPalindrome(string))
