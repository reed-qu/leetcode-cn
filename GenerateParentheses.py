#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/20 上午10:41
# @Title   : 22. 括号生成
# @Link    : https://leetcode-cn.com/problems/generate-parentheses/
# @TODO    : 提交没有通过，超时 -_-!!


QUESTION = """
给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。

例如，给出 n = 3，生成结果为：

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""


THINKING = """
思路参考 https://leetcode-cn.com/problems/generate-parentheses/solution/gua-hao-tai-fu-za-shu-zi-zhuan-hua-ta-by-da-lian-m/
即是把左括号"(" 映射成 1，右括号")" 映射成 -1，这样只要前任意位的和>=0，则表示左右括号闭环了
然后再把-1, 1替换会左右括号，思路比较取巧，但是
"""


from typing import List
from more_itertools import distinct_permutations


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        num_map = {1: "(", -1: ")"}
        result = []
        perm = distinct_permutations([-1, 1] * n)
        perm = filter(lambda x: x[0] == 1 and x[-1] == -1, perm)
        for each in perm:
            all_bigger_than_0 = True
            for i in range(1, n*2+1):
                if sum(each[:i]) < 0:
                    all_bigger_than_0 = False
                    break

            if all_bigger_than_0:
                result.append(each)
        return ["".join([num_map.get(x) for x in each]) for each in result]


if __name__ == '__main__':
    s = Solution()
    n = 6
    print(s.generateParenthesis(n))
