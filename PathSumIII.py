#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/12 上午11:37
# @Title   : 437. 路径总和 III
# @Link    : https://leetcode-cn.com/problems/path-sum-iii/


QUESTION = """
给定一个二叉树，它的每个结点都存放着一个整数值。
找出路径和等于给定数值的路径总数。
路径不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）
二叉树不超过1000个节点，且节点数值范围是 [-1000000,1000000] 的整数。

示例：
root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

返回 3。和等于 8 的路径有:
1.  5 -> 3
2.  5 -> 2 -> 1
3.  -3 -> 11
"""


THINKING = """
思路就是遍历出所有可能的路径和，但是这里要求是只允许从上往下
所以这里可以递归遍历，递归到某一个节点的时候，记录当前节点and当前节点与之前所有路径和 的和
然后每次返回这一层递归中有几次出现和为sum + 左子树的以上逻辑 + 右子树的以上逻辑

递归不太好理解，结合代码注释和测试样例debug比较好理解
参考: https://leetcode-cn.com/problems/path-sum-iii/solution/pythondan-di-gui-dfskong-jian-fu-za-du-jiao-gao-da/
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if not root:
            return 0

        def count_sum(node, sums):
            # 初始化left, right为0，这样递归到叶子节点的时候不能继续往下遍历的时候即+0
            left, right = 0, 0

            # 这里是递归的上一层的所有路径求和，依次与此节点的数值求和，再加上当前节点本身
            # 思想就是求出所有路径的和，计算出和为sum的次数
            current_sums = [num + node.val for num in sums] + [node.val]
            if node.left:
                left = count_sum(node.left, current_sums)
            if node.right:
                right = count_sum(node.right, current_sums)
            return current_sums.count(sum) + left + right

        return count_sum(root, [])


if __name__ == '__main__':
    s = Solution()
    root = TreeNode(1)
    left = TreeNode(2)
    right = TreeNode(3)
    left_left = TreeNode(4)
    left_right = TreeNode(5)
    right_left = TreeNode(6)
    right_right = TreeNode(7)
    left.left = left_left
    left.right = left_right
    right.left = right_left
    right.right = right_right
    root.left = left
    root.right = right
    """
          1
        /   \
       2     3
      / \   / \
     4   5 6   7
    """
    sum = 3
    print(s.pathSum(root, sum))
