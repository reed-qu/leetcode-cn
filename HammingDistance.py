#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/21 上午11:10
# @Title   : 461. 汉明距离
# @Link    : https://leetcode-cn.com/problems/hamming-distance/


QUESTION = """
两个整数之间的汉明距离指的是这两个数字对应二进制位不同的位置的数目
给出两个整数 x 和 y，计算它们之间的汉明距离。

注意：
0 ≤ x, y < 2^31.

示例:
输入: x = 1, y = 4
输出: 2
解释:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

上面的箭头指出了对应二进制位不同的位置。
"""


THINKING = """
第一次用了很笨比的方式，就是跟着题设走，当然是可以计算出来

看了某位网友的回答，感觉才是精髓所在:
    两个数字进行位异或预算，不同的位即是"1"，计数"1"就行了
"""


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # 笨比算法
        if x == y:
            return 0
        else:
            bin_x = bin(x)[2:]
            len_x = len(bin_x)
            bin_y = bin(y)[2:]
            len_y = len(bin_y)
            l = len_x
            if len_x < len_y:
                bin_x = bin_x.zfill(len_y)
                l = len_y
            else:
                bin_y = bin_y.zfill(len_x)

            count = 0
            for i in range(l):
                if bin_x[i] != bin_y[i]:
                    count += 1
            return count

        # 精髓算法
        # return bin(x ^ y).count("1")


if __name__ == '__main__':
    s = Solution()
    x = 1
    y = 4
    print(s.hammingDistance(x, y))
