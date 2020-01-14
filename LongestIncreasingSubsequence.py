#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/14 上午10:38
# @Title   : 300. 最长上升子序列
# @Link    : https://leetcode-cn.com/problems/longest-increasing-subsequence/


QUESTION = """
给定一个无序的整数数组，找到其中最长上升子序列的长度。

示例:
输入: [10,9,2,5,3,7,101,18]
输出: 4 
解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。

说明:
可能会有多种最长上升子序列的组合，你只需要输出对应的长度即可。
你算法的时间复杂度应该为 O(n^2) 。

进阶: 你能将算法的时间复杂度降低到 O(n log n) 吗?
"""


THINKING = """
动态规划问题，首先思考这个题里的状态是啥
状态其实就是一个一个找呗，且是升序的找，只在每个数字的后面，找比当前数字大的才能构成子序列

这里涉及到2层循环，第一层遍历每个数字，第二层遍历是从当前数字到最后
为什么要这么做呢？因为只要后面有比当前数字大的，都会组成一个长度为2的子序列，即每个数字都有可能作为一个子序列的开头(当然并不是每1个都是最长的)

如果第一层遍历移到下一位了，就可以继续做上述说的比较的动作，但是要引入一个数组dp，来记录状态转移时的变化
dp默认值都是1，因为最坏情况下，数组中的数据是严格递减的话，最长子序列就是每个数字本身，即1
这时候动态规划的状态就出来了，就是在第一层遍历中，每换一个数字，做的事情都是一样的，只不过是搜索升序的范围变了

在第二层遍历中，每次比较与第一层遍历中的数字的大小，如果大，则是升序的，即可以构成子序列，但是要比较一下
当前的这个子序列长，还是之前某个数字构成的子序列更长，所以要比较一下也就是max(dp[j], dp[i]+1)
最后输出这个dp中的最大值，就是最长的子序列
"""


from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        size = len(nums)
        if size <= 1:
            return size

        dp = [1] * size
        for i in range(size):
            for j in range(i+1, size):
                if nums[j] > nums[i]:
                    dp[j] = max(dp[j], dp[i]+1)

        return max(dp)


if __name__ == '__main__':
    s = Solution()
    nums = [8,9,2,5,3,7,101,18]
    print(s.lengthOfLIS(nums))
