#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/4 下午3:12
# @Title   : 155. 最小栈
# @Link    : https://leetcode-cn.com/problems/min-stack/


QUESTION = """
设计一个支持 push，pop，top 操作，并能在常数时间内检索到最小元素的栈

push(x) -- 将元素 x 推入栈中。
pop() -- 删除栈顶的元素。
top() -- 获取栈顶元素。
getMin() -- 检索栈中的最小元素。

示例:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> 返回 -3.
minStack.pop();
minStack.top();      --> 返回 0.
minStack.getMin();   --> 返回 -2.
"""


THINKING = """
用Python的列表来实现
因为要记录栈中的最小值，所以引入辅助列表

1. 首先push进入栈的时候，正常栈正常append元素x
    辅助栈要判断辅助栈的最后一位(也就是最小的数值)，如果更小，则辅助栈append(x)，否则的话辅助栈则添加辅助栈的最后一位(即最小的)
2. pop则两个栈都是正常pop
3. top则也是正常取正常栈的最后一位
4. 获取最小的值则取辅助栈的最后一位

这个问题主要就是处理push和pop的关系，如果添加队列是降序的话，那么就不需要辅助栈了
如果有一个数字比之前的最小值大了，那就往辅助栈里添加之前数列中最小的值，这样的话pop的时候删除了一个值
辅助栈中最后一位还是记录的之前队列中最小的值，就可以继续操作下去了
"""


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.helper = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.helper or x <= self.helper[-1]:
            self.helper.append(x)
        else:
            self.helper.append(self.helper[-1])

    def pop(self) -> None:
        if self.stack:
            self.helper.pop()
            return self.stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]

    def getMin(self) -> int:
        if self.helper:
            return self.helper[-1]


if __name__ == '__main__':
    # Your MinStack object will be instantiated and called as such:
    obj = MinStack()
    x = 1
    obj.push(-2)
    obj.push(0)
    obj.push(-3)
    print("最小值是: {}".format(obj.getMin()))
    print("移除栈顶项: {}".format(obj.pop()))
    param_3 = obj.top()
    print(f"此时栈顶为{param_3}")
    param_4 = obj.getMin()
    print(f"此时最小值为{param_4}")
