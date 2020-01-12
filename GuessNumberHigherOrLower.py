#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/12 上午11:41
# @Title   : 374. 猜数字大小
# @Link    : https://leetcode-cn.com/problems/guess-number-higher-or-lower/


QUESTION = """
我们正在玩一个猜数字游戏。 游戏规则如下：
我从 1 到 n 选择一个数字。 你需要猜我选择了哪个数字。
每次你猜错了，我会告诉你这个数字是大了还是小了。
你调用一个预先定义好的接口 guess(int num)，它会返回 3 个可能的结果（-1，1 或 0）：

-1 : 我的数字比较小
1 : 我的数字比较大
0 : 恭喜！你猜对了！

示例 :
输入: n = 10, pick = 6
输出: 6
"""


THINKING = """
这他妈是一道语文题...
注意一点，这里说的"我的数字比较小", "我的数字比较大"中的"我的"，是guess接口中的正确的数字pick

其他没什么说的了，二分查找即可
"""


# The guess API is already defined for you.
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
def guess(num: int) -> int:
    pick = 19
    if num == pick:
        return 0
    elif num < pick:
        return 1
    else:
        return -1


class Solution:
    def guessNumber(self, n: int) -> int:

        left, right = 1, n
        while 1:
            guess_num = left + (right - left) // 2
            g = guess(guess_num)
            if g == 0:
                return guess_num
            elif g > 0:
                left = guess_num + 1
            else:
                right = guess_num


if __name__ == '__main__':
    s = Solution()
    n = 44
    print(s.guessNumber(n))
