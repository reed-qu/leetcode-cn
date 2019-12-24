#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/25 上午10:04
# @Title   : 448. 找到所有数组中消失的数字
# @Link    : https://leetcode-cn.com/problems/find-all-numbers-disappeared-in-an-array/solution/


QUESTION = """
给定一个范围在  1 ≤ a[i] ≤ n ( n = 数组大小 ) 的 整型数组，数组中的元素一些出现了两次，另一些只出现一次。
找到所有在 [1, n] 范围之间没有出现在数组中的数字。

您能在不使用额外空间且时间复杂度为O(n)的情况下完成这个任务吗? 你可以假定返回的数组不算在额外空间内。

示例:
输入:
[4,3,2,7,8,2,3,1]

输出:
[5,6]
"""


THINKING = """
笨比实现方式
借助集合set来实现，并不满足题设中"不使用额外空间"的假设，但是实现起来很简单，效率还不错
set(a).discard(object)并不需要检查元素是否存在

TODO 以后有时间再回来研究
"""


from typing import List

class Solution:
    def findDisappearedNumbers_stupid(self, nums: List[int]) -> List[int]:
        # 笨比算法
        normal_nums = set(range(1, len(nums)+1))
        for each in set(nums):
            normal_nums.discard(each)
        return list(normal_nums)

    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # TODO
        pass


if __name__ == '__main__':
    s = Solution()
    nums = [4,3,2,7,8,2,3,1]
    print(s.findDisappearedNumbers(nums))
