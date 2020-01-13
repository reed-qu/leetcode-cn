#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/13 上午11:14
# @Title   : 232. 用栈实现队列
# @Link    : https://leetcode-cn.com/problems/implement-queue-using-stacks/


QUESTION = """
使用栈实现队列的下列操作：

push(x) -- 将一个元素放入队列的尾部。
pop() -- 从队列首部移除元素。
peek() -- 返回队列首部的元素。
empty() -- 返回队列是否为空。
示例:

MyQueue queue = new MyQueue();

queue.push(1);
queue.push(2);  
queue.peek();  // 返回 1
queue.pop();   // 返回 1
queue.empty(); // 返回 false

说明:
你只能使用标准的栈操作 -- 也就是只有 push to top, peek/pop from top, size, 和 is empty 操作是合法的。
你所使用的语言也许不支持栈。你可以使用 list 或者 deque（双端队列）来模拟一个栈，只要是标准的栈操作即可。
假设所有操作都是有效的 （例如，一个空的队列不会调用 pop 或者 peek 操作）。
"""


THINKING = """
主要是了解一下栈和队列的概念，就行了

[栈](https://zh.wikipedia.org/wiki/%E5%A0%86%E6%A0%88)
[队列](https://zh.wikipedia.org/wiki/%E9%98%9F%E5%88%97)
"""


class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = []


    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """

        self.queue.insert(0, x)


    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """

        return self.queue.pop()


    def peek(self) -> int:
        """
        Get the front element.
        """

        return self.queue[-1]


    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """

        return not self.queue


if __name__ == '__main__':
    # Your MyQueue object will be instantiated and called as such:
    obj = MyQueue()
    x = 2
    obj.push(x)
    param_2 = obj.pop()
    param_3 = obj.peek()
    param_4 = obj.empty()
