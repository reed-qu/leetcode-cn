#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/30 上午10:14
# @Title   : 189. 旋转数组
# @Link    : https://leetcode-cn.com/problems/rotate-array/


QUESTION = """
给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。

示例 1:
输入: [1,2,3,4,5,6,7] 和 k = 3
输出: [5,6,7,1,2,3,4]
解释:
向右旋转 1 步: [7,1,2,3,4,5,6]
向右旋转 2 步: [6,7,1,2,3,4,5]
向右旋转 3 步: [5,6,7,1,2,3,4]

示例 2:
输入: [-1,-100,3,99] 和 k = 2
输出: [3,99,-1,-100]
解释: 
向右旋转 1 步: [99,-1,-100,3]
向右旋转 2 步: [3,99,-1,-100]

说明:
尽可能想出更多的解决方案，至少有三种不同的方法可以解决这个问题。
要求使用空间复杂度为 O(1) 的 原地 算法。
"""


THINKING = """
这个题比较简单，既可以按照题设思路一个一个处理
也可以直接切片拼接，原地修改就是不用返回值，直接修改nums即可
"""


from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> List:
        """
        Do not return anything, modify nums in-place instead.
        """

        n = len(nums)
        nums[:] = nums[n-k:] + nums[:n-k]
        return nums


if __name__ == '__main__':
    s = Solution()
    nums = [1,2,3,4,5,6,7]
    k = 3
    print(s.rotate(nums, k))
