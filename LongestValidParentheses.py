#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @Time    : 2021/03/23 17:16:03
# @Title   : 32. 最长有效括号
# @Link    : https://leetcode-cn.com/problems/longest-valid-parentheses/


QUESTION = """
给你一个只包含 '(' 和 ')' 的字符串，找出最长有效（格式正确且连续）括号子串的长度。

示例 1：
输入：s = "(()"
输出：2
解释：最长有效括号子串是 "()"

示例 2：
输入：s = ")()())"
输出：4
解释：最长有效括号子串是 "()()"

示例 3：
输入：s = ""
输出：0
 
提示：
0 <= s.length <= 3 * 104
s[i] 为 '(' 或 ')'
"""


THINKING = """
动态规划
1. 判空
2. 构建动态数组 dp = [0] * len(s)，记录s截止第i个字符的最长有效括号，dp[i]表示s字符串中第i位的截止的子字符串的最长有效括号

3. 首先如果第i位是 ( 的话，与任何左边的都形成不了有效括号，所以有可能行程有效括号的肯定是 ) 才可以，所以遍历的时候前提是 ) 才会需要往前找，进行判断是否形成有效括号
4. 考虑以下字符串
    s:  a    b    (    )   )
index: i-4  i-3  i-2  i-1  i

此时需要考虑一下几点：
    1. b 是否是 ( ，如果是的话，则和i形成的有效括号 则 +2，否则不可以 则还为0，b点的索引则是 i - dp[i-1] - 1
        i - dp[i-1] - 1 则是跳过 i-1 i-2 这两个括号， 中间可能有多个有效括号，所以要动态的减去dp[i-1]个
        特殊的，如果是 .... ( )，i-1是 ( , 所以此时dp[i-1]为0, 所以i - df[i-1] -1 则为 i-1，同样兼容
    2. a 点之前有 dp[i-4] 个有效括号 要考虑进来，a点的索引则是 i - dp[i-1] - 1 - 1
    3. i-1 点有 df[i-1] 个有效括号 要考虑进来
所以dp[i] = 2 + df[i-1] + df[i - dp[i-1] - 2]
从头遍历到尾，最后dp中最大的则是所求最长有效括号
"""


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        if n==0:
            return 0

        dp = [0] * n
        for i in range(n):
            if s[i] == ')' and i-dp[i-1]-1 >= 0 and s[i-dp[i-1]-1] == '(':
               dp[i] = dp[i-1] + dp[i-dp[i-1]-2] + 2
        return max(dp)


if __name__ == "__main__":
    s = Solution()
    print(s.longestValidParentheses("()(())"))
