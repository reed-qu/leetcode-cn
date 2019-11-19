#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/18 下午5:30
# @Title   : 278. 第一个错误的版本
# @Link    : https://leetcode-cn.com/problems/first-bad-version/


QUESTION = """
你是产品经理，目前正在带领一个团队开发新的产品。不幸的是，你的产品的最新版本没有通过质量检测
由于每个版本都是基于之前的版本开发的，所以错误的版本之后的所有版本都是错的。

假设你有 n 个版本 [1, 2, ..., n]，你想找出导致之后所有版本出错的第一个错误的版本。
你可以通过调用 bool isBadVersion(version) 接口来判断版本号 version 是否在单元测试中出错
实现一个函数来查找第一个错误的版本。你应该尽量减少对调用 API 的次数。

示例:
给定 n = 5，并且 version = 4 是第一个错误的版本。
调用 isBadVersion(3) -> false
调用 isBadVersion(5) -> true
调用 isBadVersion(4) -> true
所以，4 是第一个错误的版本。 
"""


THINKING = """
首先肯定是要用二分查找的，这个没什么好说的
只不过在查找的过程中有一个校验的过程，分2种情况
1. 如果是"错误的版本"，则校验前一个版本，如果前一个版本没问题，那么这个"错误的版本"即为输出
2. 如果是正常的版本，则校验后一个版本呢，如果后一个版本是"错误的版本"，那么后一个的"错误的版本"即为输出
最后如果二者都不是即继续二分查找
"""


def isBadVersion(version: int) -> bool:
    if version >= 2:
        return True
    return False


class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n
        while left <= right:
            middle = left + (right - left) // 2
            if isBadVersion(middle):
                if not isBadVersion(middle-1):
                    return middle
                right = middle
            else:
                if isBadVersion(middle+1):
                    return middle+1
                left = middle


if __name__ == '__main__':
    s = Solution()
    n = 2
    print(s.firstBadVersion(n))
