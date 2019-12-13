#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/12 下午5:26
# @Title   : 538. 把二叉搜索树转换为累加树
# @Link    : https://leetcode-cn.com/problems/convert-bst-to-greater-tree/


QUESTION = """
给定一个二叉搜索树（Binary Search Tree），把它转换成为累加树（Greater Tree)
使得每个节点的值是原来的节点值加上所有大于它的节点值之和。

例如：
输入: 二叉搜索树:
              5
            /   \
           2     13

输出: 转换为累加树:
             18
            /   \
          20     13
"""


THINKING = """
所谓二叉搜索树，即是右节点的值始终大于当前节点，左节点始终小于当前节点
所以思路就是降序的来遍历整棵树，这样就可以一步一步的累加
引入两个变量total记录累加值，stack栈记录遍历顺序
首先判断栈是否为空，和当前节点是否为None
如果stack不为空表示当前节点和右子树还没有遍历完，node不为空则表示还可以继续往下搜索，二者其一为True则要继续遍历

1. 搜索右子树，每次把右节点压入栈
2. 从栈顶取节点，也就是最大的那个节点，total累计上当前的节点值，然后把这个最右的节点的上一节点(最近的一个比这个数字小的值)赋值为total
3. 然后再把处理左节点，如果此时有左节点或者栈中还有数据没处理完就要继续处理

总体来说的处理顺序就是，先从树的右下角(最大的数字)开始，依次向上一层再往左再往上，这样处理到左下角(最小的数字)结束
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        total = 0
        node = root
        stack = []

        while stack or node is not None:
            while node is not None:
                stack.append(node)
                node = node.right

            node = stack.pop()
            total += node.val
            node.val = total

            node = node.left
        return root


if __name__ == '__main__':
    s = Solution()
    root = TreeNode(5)
    left = TreeNode(2)
    right = TreeNode(13)
    root.left = left
    root.right = right
    print(s.convertBST(root))
