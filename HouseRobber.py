#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/18 下午1:01
# @Title   : 198. 打家劫舍
# @Link    : https://leetcode-cn.com/problems/house-robber/


QUESTION = """
你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金
影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警
给定一个代表每个房屋存放金额的非负整数数组，计算你在不触动警报装置的情况下，能够偷窃到的最高金额。

示例 1:
输入: [1,2,3,1]
输出: 4
解释: 偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
     偷窃到的最高金额 = 1 + 3 = 4 。

示例 2:
输入: [2,7,9,3,1]
输出: 12
解释: 偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
     偷窃到的最高金额 = 2 + 9 + 1 = 12 。
"""


THINKING = """
总体来说是个动态规划的问题
个人最开始的思路是从第三个开始处理，是不是要取第三个，取决于第1、3个的和 和第二个比谁大而已
或者是假定只有3个数，只是比较1、3的和 和 第二个数的大小就行了
这样一来，从第三个开始，比较上述的两种情况那种更大，然后替换掉当前的数，然后再移到下一位，处理方式一样

实际测试中有这样一个问题，一个是[2, 1, 1, 2]问题，按照上面的流程处理，结果不是4，那是因为没有从第一位开始处理
如果要从第一位开始处理的话，就要让第一位之前有两个默认的值，设置成0, 0就可以了，这样就可以把第一位当做第三个来处理了
第1、2、3位分别是 previous, current, nums[i](即当前处理的数字)，看previous+nums[i] 和 current谁更大就行了
然后整体向后挪一位，previous挪到current, current挪到i, i挪到i+1
这里注意要把新的值更新到nums中，这样才能让记住之前处理过的数字
最后返回current或者nums[-1]即是最大的数据
"""


from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        l = len(nums)
        previous, current = 0, 0
        for i in range(l):
            nums[i] = max(previous + nums[i], current)
            previous = current
            current = nums[i]
        return current


if __name__ == '__main__':
    s = Solution()
    nums = [2,7,9,3,1]
    print(s.rob(nums))
