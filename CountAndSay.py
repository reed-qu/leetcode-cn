#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/17 下午2:42
# @Title   : 38. 报数
# @Link    : https://leetcode-cn.com/problems/count-and-say/


QUESTION = """
报数序列是一个整数序列，按照其中的整数的顺序进行报数，得到下一个数。其前五项如下：
1.     1
2.     11
3.     21
4.     1211
5.     111221

1 被读作  "one 1"  ("一个一") , 即 11。
11 被读作 "two 1s" ("两个一"）, 即 21。
21 被读作 "one 2",  "one 1" （"一个二" ,  "一个一") , 即 1211。

给定一个正整数 n（1 ≤ n ≤ 30），输出报数序列的第 n 项。

注意：整数顺序将表示为一个字符串。

示例 1:
输入: 1
输出: "1"

示例 2:
输入: 4
输出: "1211"
"""


THINKING = """
题意不太好理解，可以这么理解，第一个人报"1"，第二个人听到第一个人的"1"，所以报"1个1"，所以是"11"
第三个人听到第二个人报的"11"，所以第三个人报"2个1"，所以是"21"，以此类推

这样的话就比较好处理了，其实就是按照上面的解释，循环下去
首先初始化第一个人报的"1"，然后第n个人是根据第n-1个人报出来的数，按照规则再报出来他的数
所以这里有两层循环，第一层是n个人，n个循环
第二层是对于第k个人来说，第k-1个人报出来的数，第k个人要从头遍历一遍才能整理出来他自己的数

首先初始化3个变量，下一个人的报数next_person是""，然后每一次节点整理出来的数字往里添加
计数变量count，需要计数某一个数字一共重复多少次，然后用"几个几"来报，默认是1
当前数字current，默认是第一个，然后每一次往后移动一个数

假设第k-1个人报的数是"1211"，那么第k个人要从头开始遍历
初始化当前的数字是第一个数，即是"1"，遍历到第二个的时候是"2"，不等于当前数字"1"，那么就是"1个1"，即"11"
next_person = "11"， current = "2", count = 1
下一次的数字是"1"，"1" != "2"，则又是一个节点，就是"1个2"，即"12"
next_person = "1112", current = "1", count = 1
在下一次的数字是"1"， "1" == "1"，则count += 1，为2，那么就是"2个1"，即"21"
next_person = "111221"
因为可能还要继续往第k+1个人循环，所以对k+1个人来说，第k个人就是上一个人，所以这里把他在作为上一个人来处理
总是返回上一个人的数即可
"""


class Solution:
    def countAndSay(self, n: int) -> str:
        pre_person = "1"
        for i in range(1, n):
            count = 1
            current = pre_person[0]
            next_person = ""
            for each in pre_person[1:]:
                if each == current:
                    count += 1
                else:
                    next_person += str(count) + current
                    current = each
                    count = 1
            next_person += str(count) + current
            pre_person = next_person
        return pre_person


if __name__ == '__main__':
    s = Solution()
    n = 5
    print(s.countAndSay(n))
