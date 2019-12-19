#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/18 下午2:48
# @Title   : 17. 电话号码的字母组合
# @Link    : https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number/


QUESTION = """
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。
给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。

    1    2    3
   !@#  abc  def
   
    4    5    6
   ghi  jkl  mno
    
    7    8    9
  pqrs  tuv  wxyz

示例:

输入："23"
输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

说明:
尽管上面的答案是按字典序排列的，但是你可以任意选择答案输出的顺序。
"""


THINKING = """
特判和构建字典或者其他数据结构这没啥好说的
主要是要实现依次拿出每个字符，然后每个字符要跟另外一个进行"全匹配"，仅仅是有2个字符的话，两层for循环就可以了
但是主要是我们不知道有几个字符，也就不知道要几层for循环，此时就需要加一些技巧，也不难想到，有多个字符仍然可以先处理前2个
这里用到队列的概念，就是说我们用个列表来记录遍历的结果，动态的添加和取出，知道字符遍历完
1. 首先假定第0个字符是""，有利于用同样的套路处理后面的字符
2. 第一个字符对应的n的字母，拿出第0个字符与这n个字母拼接，也就是["a", "b", "c"]
3. 到第个字符"3"对应的"def"，每次从列表中拿一个，循环处理这个"def"，处理结束就变成了["b", "c", "ad", "ae", "af"]
继续往后遍历就可以了，这道题的主要思路就是维护一个动态的列表，然后一步一步处理
"""


from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        phone = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        result = [""]

        for each in digits:
            size = len(result)
            letters = phone.get(each)

            for _ in range(size):
                current = result.pop(0)
                for l in letters:
                    result.append(current+l)

        return result


if __name__ == '__main__':
    s = Solution()
    digits = "23"
    print(s.letterCombinations(digits))
