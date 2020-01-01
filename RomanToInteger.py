#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/1 下午10:56
# @Title   : 13. 罗马数字转整数
# @Link    : https://leetcode-cn.com/problems/roman-to-integer/


QUESTION = """
罗马数字包含以下七种字符: I， V， X， L，C，D 和 M。

字符          数值
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

例如， 罗马数字 2 写做 II ，即为两个并列的 1。12 写做 XII ，即为 X + II 。 27 写做  XXVII, 即为 XX + V + II 。

通常情况下，罗马数字中小的数字在大的数字的右边。
但也存在特例，例如 4 不写做 IIII，而是 IV。数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。

同样地，数字 9 表示为 IX。这个特殊的规则只适用于以下六种情况：

    I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
    X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。 
    C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。

给定一个罗马数字，将其转换成整数。输入确保在 1 到 3999 的范围内。

示例 1:
输入: "III"
输出: 3

示例 2:
输入: "IV"
输出: 4

示例 3:
输入: "IX"
输出: 9

示例 4:
输入: "LVIII"
输出: 58
解释: L = 50, V= 5, III = 3.

示例 5:
输入: "MCMXCIV"
输出: 1994
解释: M = 1000, CM = 900, XC = 90, IV = 4.
"""


THINKING = """
穷举6种特殊情况，跟罗马数字一样，形成映射关系，表示4, 9, 40, 90, 400, 900
然后每2个2个的字符的来判断，先判断是否是组合字符
如果不是的话再判断单个字符，硬逻辑处理即可
"""


class Solution:
    def romanToInt(self, s: str) -> int:
        roman_digit = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        combine_roman_digit = {"IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}

        l = len(s)
        current_point = 0
        result = 0

        if l >= 2:
            while current_point < l:
                current_string = s[current_point: current_point + 2]
                if current_string in combine_roman_digit:
                    result += combine_roman_digit.get(current_string)
                    current_point += 2
                else:
                    result += roman_digit.get(current_string[0])
                    current_point += 1
        else:
            result = roman_digit.get(s)

        return result


if __name__ == '__main__':
    s = Solution()
    string = "MCMXCIV"
    print(s.romanToInt(string))
