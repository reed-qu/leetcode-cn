#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/13 上午10:19
# @Title   : 387. 字符串中的第一个唯一字符
# @Link    : https://leetcode-cn.com/problems/first-unique-character-in-a-string/


QUESTION = """
给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。

案例:
s = "leetcode"
返回 0.

s = "loveleetcode",
返回 2.

注意事项：您可以假定该字符串只包含小写字母。
"""


THINKING = """
建立哈希表，用空间换时间，记录每个字符出现的次数，然后过滤出只出现1次的
因为Python内置的字典是无序的，所以过滤出出现1次的字符，还要继续找出哪个是第一次出现的
也可以用有序字典

看解答中有一种思路个人感觉很不错，是反向思维，就是说如果字符串很长的话，因为这里只有26个小写字母
可以遍历这26个小写字母，同时从字符串的前后查找，如果找到的是同一个，则表示出现一次，也可以实现
"""


class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = {}

        for letter in s:
            if letter in count:
                count[letter] += 1
            else:
                count[letter] = 1

        unique_letters = [k for k, _ in filter(lambda x: x[1] == 1, count.items())]

        for i, letter in enumerate(s):
            if letter in unique_letters:
                return i

        return -1


if __name__ == '__main__':
    s = Solution()
    string = "loveleetcode"
    print(s.firstUniqChar(string))
