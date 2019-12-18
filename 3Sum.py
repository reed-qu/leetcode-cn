#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/17 上午10:02
# @Title   : 15. 三数之和
# @Link    : https://leetcode-cn.com/problems/3sum/


QUESTION = """
给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。
注意：答案中不可以包含重复的三元组。

例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，
满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""


THINKING = """
首先要对列表进行排序，排序之后才能有方向的查找，否则就变成暴力查找，效率很低
k索引从列表头，开始往后遍历到导数第三位(因为还需要另外两个索引)，然后主要寻找领完两个索引i, j来满足三者之和为0
要排序就在这时候发挥作用，如果nums[k]>0，就没必要继续往后找了，因为后面都是比0大的，不可能三者之和为0
每次k往后移一位，则重新初始化i, j = k+1, len(nums)-1，即是k后一位和最后一位，在之间找符合条件的数，k前面的之前肯定找过所以就必要查找了
然后每次求和的结果s，判断与0的关系
    如果小于0，则表示要往大的方向走，则i(小的索引)后移一位
    如果大于0，则表示要往小的方向走，则j(大的索引)前移一位
    如果等于0，则表示此为结果其一，记录下来
此时为了避免重复解，要多判断一下i, j同时移一位之后与上一位的关系，如果相等的话，则跳过这一个就行了

主要的思路就是通过排序，来为查找找到合理的方向，同时避免重复解
"""


from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        l = len(nums)
        if not nums or l < 3:
            return []

        nums.sort()
        result, k  = [], 0
        for k in range(l-2):
            current = nums[k]
            if current > 0:
                break

            if k > 0 and current == nums[k-1]:
                continue

            i, j = k+1, l-1
            while i < j:
                s = current + nums[i] + nums[j]
                if s < 0:
                    i += 1

                if s > 0:
                    j -= 1

                if s == 0:
                    result.append([current, nums[i], nums[j]])
                    i += 1
                    j -= 1
                    while i < j and nums[i] == nums[i-1]:
                        i += 1
                    while i < j and nums[j] == nums[j+1]:
                        j -= 1

        return result


if __name__ == '__main__':
    s = Solution()
    nums = [-1, 0, 1, 2, -1, -4]
    print(s.threeSum(nums))
