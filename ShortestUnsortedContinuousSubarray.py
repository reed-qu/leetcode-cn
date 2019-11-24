#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/22 下午6:29
# @Title   : 581. 最短无序连续子数组
# @Link    : https://leetcode-cn.com/problems/shortest-unsorted-continuous-subarray/


QUESTION = """
给定一个整数数组，你需要寻找一个连续的子数组，如果对这个子数组进行升序排序，那么整个数组都会变为升序排序。
你找到的子数组应是最短的，请输出它的长度。

示例 1:
输入: [2, 6, 4, 8, 10, 9, 15]
输出: 5

解释: 你只需要对 [6, 4, 8, 10, 9] 进行升序排序，那么整个表都会变为升序排序。

说明 :
输入的数组长度范围在 [1, 10,000]。
输入的数组可能包含重复元素 ，所以升序的意思是<=。
"""


THINKING = """
调整之后要是升序的，然后找出需要调整顺序的内一部分
那么就先排序，然后再对比每一位的索引就可以了，最小的索引 和 最大的索引，之间的内部分，就是需要调整的
把这部分调整好的话，那么自然也就和排序要的一样了，也是所求
Python实现起来代码量很少
"""


from typing import List

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        sort_nums = sorted(nums)
        diff = [i for i, (a, b) in enumerate(zip(sort_nums, nums)) if a != b]
        return len(diff) and max(diff) - min(diff) + 1


if __name__ == '__main__':
    s = Solution()
    nums = [2,6,4,8,10,9,15]
    print(s.findUnsortedSubarray(nums))
