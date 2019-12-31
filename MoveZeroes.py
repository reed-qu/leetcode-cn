#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/20 上午10:08
# @Title   : 283. 移动零
# @Link    : https://leetcode-cn.com/problems/move-zeroes/


QUESTION = """
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序

示例:
输入: [0,1,0,3,12]
输出: [1,3,12,0,0]

说明:
必须在原数组上操作，不能拷贝额外的数组。
尽量减少操作次数。
"""


THINKING = """
有两种思路
1. 从头遍历，遇到0，则放到最后一位
2. 从头遍历，遇到非0，则放到第一位，下一次遇到放到第二位
"""


from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index = 0
        number_of_zero = 0
        length = len(nums)
        while index < (length - number_of_zero):
            if nums[index] == 0:
                nums.pop(index)
                nums.append(0)
                number_of_zero += 1
            else:
                index += 1
        print(nums)


if __name__ == '__main__':
    s = Solution()
    nums = [0,1,0,3,12]
    print(s.moveZeroes(nums))
