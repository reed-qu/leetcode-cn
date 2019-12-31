#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/2 下午5:57
# @Title   : 31. 下一个排列
# @Link    : https://leetcode-cn.com/problems/next-permutation/


QUESTION = """
实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列
如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。
必须原地修改，只允许使用额外常数空间。

以下是一些例子，输入位于左侧列，其相应输出位于右侧列。
    1,2,3 → 1,3,2
    3,2,1 → 1,2,3
    1,1,5 → 1,5,1
"""


THINKING = """
参考wiki: https://en.wikipedia.org/wiki/Permutation#Generation_in_lexicographic_order
1. 找到最大的索引k, 满足条件nums[k] < nums[k+1], 如果找不到k, 则翻转nums作为下一个排列
2. 找到最大的索引j, 满足条件 j > k 且 nums[k] < nums[j]
3. nums[k], nums[j] 二者对调
4. 翻转nums[k+1:]部分, 此时即是下一个排列的数组

按照正常的思路走一遍的话，会比较好理解，举例nums = [1, 2, 5, 4, 3, 1]
1. k代表的是，这个位置是一个翻转节点，从k+1开始，数字开始变小，下一个排列应该找到比k这个位置大的最小的内个数字
2. 这个j，就是比k这个位置大的最小的内个数字
3. 对调 j, k，即是"往前，且迈了最小的一步"，然后从k+1一直到最后，此时也一定是降序的是最大的
4. 翻转nums[k+1:]，即是把后面的数字变成最小的了，那么这个就是下一个排列的数组了

注: 如果找不到k的话就表示数组是降序的，这个排列就是最大的了，翻转就是下一个排列，即最小的排列
"""


from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> List:
        """
        Do not return anything, modify nums in-place instead.
        """

        l = len(nums)
        # 找出最大的索引 k 需要满足nums[k] < nums[k+1]
        # 同时找出最大的索引 j 需要满足 nums[j] > nums[k]
        k , j = -1, -1
        for i in range(l):
            if i < l-1 and nums[i+1] > nums[i]:
                k = i
            if nums[i] > nums[k]:
                j = i

        if k < 0:
            nums.reverse()
        else:
            nums[k], nums[j] = nums[j], nums[k]
            nums[k+1:] = nums[k+1:][::-1]
        return nums # delete this line, when submit in leetcode


if __name__ == '__main__':
    s = Solution()
    nums = [1, 2, 5, 4, 3, 1]
    print(s.nextPermutation(nums))
