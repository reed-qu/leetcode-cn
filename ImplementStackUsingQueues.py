#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/13 上午10:59
# @Title   : 225. 用队列实现栈
# @Link    : https://leetcode-cn.com/problems/implement-stack-using-queues/


QUESTION = """
使用队列实现栈的下列操作：

push(x) -- 元素 x 入栈
pop() -- 移除栈顶元素
top() -- 获取栈顶元素
empty() -- 返回栈是否为空

注意:
你只能使用队列的基本操作-- 也就是 push to back, peek/pop from front, size, 和 is empty 这些操作是合法的。
你所使用的语言也许不支持队列。 你可以使用 list 或者 deque（双端队列）来模拟一个队列 , 只要是标准的队列操作即可。
你可以假设所有操作都是有效的（例如, 对一个空的栈不会调用 pop 或者 top 操作）。
"""


THINKING = """
栈，先进后出，栈顶是最后加入的元素，这样就好实现了
"""


class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """

        self.stack = []


    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """

        self.stack.append(x)


    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """

        if not self.empty():
            return self.stack.pop()


    def top(self) -> int:
        """
        Get the top element.
        """

        return self.stack[-1]


    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """

        return not self.stack


if __name__ == '__main__':
    # Your MyStack object will be instantiated and called as such:
    obj = MyStack()
    x = 4
    obj.push(x)
    param_2 = obj.pop()
    param_3 = obj.top()
    param_4 = obj.empty()
