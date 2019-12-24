#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/23 下午6:57
# @Title   : 46. 全排列
# @Link    : https://leetcode-cn.com/problems/permutations/


QUESTION = """
给定一个没有重复数字的序列，返回其所有可能的全排列。

示例:
输入: [1,2,3]
输出:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""


THINKING = """
回溯方法，也就是递归搜索的一种方法，是一种很通用的方法
引入一个额外的数组，在递归的过程中记录数字是否被应用 used 初始化全是False，也就是一个也没有被使用
然后在处理的过程要持续的改变“这个数字是否被使用”的状态，如果没有被使用则要使用它
递归调用的时候用index这个变量来记录是否遍历到数组的最后，如果遍历完了，则要记录下来这次遍历的顺序
然后是最重要的，在递归向上返回的时候要把之前记录的状态重置回去，这样一层一层的向上重置
当递归向上重置到[1, 2, 3]的2这一层的时候，此时used重置为[True, False, False]，这样for循环在这一步的时候会继续往下进行到i=2时
此时因为状态重置了，所以到i=2的时候还会继续处理
那么就做到了全排列，具体的细节在IDE的debug模式下更好理解一些
"""


from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return []

        size = len(nums)
        used = [False] * size
        result = []

        def _dfs(index, nums, tmp, used):
            if index == size:
                result.append(tmp.copy())
                return

            for i in range(size):
                if not used[i]:
                    used[i] = True
                    tmp.append(nums[i])

                    _dfs(index+1, nums, tmp, used)

                    used[i] = False
                    tmp.pop()

        _dfs(0, nums, [], used)

        return result


if __name__ == '__main__':
    s = Solution()
    nums = [1,2,3]
    print(s.permute(nums))
