#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/8 下午12:12
# @Title   : 78. 子集
# @Link    : https://leetcode-cn.com/problems/subsets/


QUESTION = """
给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

说明：解集不能包含重复的子集。

示例:
输入: nums = [1,2,3]
输出:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""


THINKING = """
先思考归纳子集的动作
1. []是任何集合的子集
2. 遍历到数组元素，第一次是 1，则加入本身 [1]
3. 第二次是 2，则要加入自身 [2] 和 前一个的[1] 形成 [1, 2]

这样就大概有了思路，其实就是遍历数组，往一个结果集中不断的放入
但是放入的规则就是要和 上一次遍历 形成的所有子集，都拼接上本身
"""


from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        for i in nums:
            size = len(result)
            for j in range(size):
                current = result[j] + [i]
                result.append(current)
        return result


if __name__ == '__main__':
    s = Solution()
    nums = [1, 2, 3]
    print(s.subsets(nums))
