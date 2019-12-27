#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/26 下午2:59
# @Title   : 56. 合并区间
# @Link    : https://leetcode-cn.com/problems/merge-intervals/


QUESTION = """
给出一个区间的集合，请合并所有重叠的区间。

示例 1:
输入: [[1,3],[2,6],[8,10],[15,18]]
输出: [[1,6],[8,10],[15,18]]
解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].

示例 2:
输入: [[1,4],[4,5]]
输出: [[1,5]]
解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。
"""


THINKING = """
首先排序这样可以从头开始遍历，而不至于每次都全遍历
每两个之间做比较，假设命名为: [[low, merge_high], [new_low, new_high]]
1. low肯定是4个数字中最小的，合并还是不合并，low都是[a, b]中的a
2. merge_high为如果可能合并的话，需要和后面的数字进行合并的
3. 可以合并的条件就是 merge_high >= new_low
4. 合并之后的右区间b为 max(merge_high, new_high)，更新merge_high，用于下次合并
"""


from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x: x[0])
        n = len(intervals)
        current = 0
        result = []

        while current < n:
            low, merge_high = intervals[current]

            for i in range(current+1, n):
                new_low, new_high = intervals[i]
                if merge_high >= new_low:
                    current += 1
                    merge_high = max(merge_high, new_high)

            result.append([low, merge_high])
            current += 1

        return result


if __name__ == '__main__':
    s = Solution()
    intervals = [[1,3],[2,6],[8,10],[15,18]]
    print(s.merge(intervals))
