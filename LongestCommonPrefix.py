#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/1 下午11:21
# @Title   : 14. 最长公共前缀
# @Link    : https://leetcode-cn.com/problems/longest-common-prefix/


QUESTION = """
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

示例 1:
输入: ["flower","flow","flight"]
输出: "fl"

示例 2:
输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。

说明:
所有输入只包含小写字母 a-z 。
"""


THINKING = """
硬逻辑实现
"""


from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""
        point = 0

        if not strs:
            return result

        max_len = min(len(s) for s in strs)
        while point < max_len:
            prefix_set = set(s[point] for s in strs)
            if len(prefix_set) > 1:
                break
            else:
                result = result + strs[0][point]
                point += 1

        return result


if __name__ == '__main__':
    s = Solution()
    strs = ["flower","flow","flight"]
    print(s.longestCommonPrefix(strs))
