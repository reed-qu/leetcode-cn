#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @Time    : 2021/03/18 15:23:53
# @Title   : 202. 快乐数
# @Link    : https://leetcode-cn.com/problems/happy-number/


QUESTION = """
编写一个算法来判断一个数 n 是不是快乐数。

「快乐数」定义为：
对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和。
然后重复这个过程直到这个数变为 1，也可能是 无限循环 但始终变不到 1。
如果 可以变为  1，那么这个数就是快乐数。
如果 n 是快乐数就返回 true ；不是，则返回 false 。

示例 1：
    输入：19
    输出：true
    解释：
    1^2 + 9^2 = 82
    8^2 + 2^2 = 68
    6^2 + 8^2 = 100
    1^2 + 0^2 + 0^2 = 1

示例 2：
    输入：n = 2
    输出：false
 
提示：
1 <= n <= 2^31 - 1
"""


THINKING = """
1. 起个循环一直计算，如果算到1则返回True，如果一直没有算到1，且结果在之前出现过，则表示进入死循环，即可跳出返回False
2. 考虑保存计算结果的List或者Set，如果导致无限大，那么也是不可行的，但是这里没问题，因为n有上限，且最大的数字也就是小于2^31 - 1的 1999... 的哪个数字，9^2=81，10个9也只有810个结果而已，所以空间复杂度不大
3. 到这里就很好解决了，注意计算循环的流程控制即可
"""


class Solution:
    def sum_square(self, n: int) -> int:
        result = 0
        while n >= 10:
            a = n % 10
            result += a ** 2
            n = n // 10
        a = n % 10
        result += a ** 2
        return result

    def isHappy(self, n: int) -> bool:
        sum_set = set()
        ss = self.sum_square(n)
        while ss != 1:
            if ss in sum_set:
                return False
            sum_set.add(ss)
            ss = self.sum_square(ss)
        return True


if __name__ == "__main__":
    s = Solution()
    n = 19
    print(s.isHappy(n))
