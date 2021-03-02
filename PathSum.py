#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/03/02 下午16:50
# @Title   : 112. 路径总和
# @Link    : https://leetcode-cn.com/problems/path-sum/


QUESTION = """
给你二叉树的根节点 root 和一个表示目标和的整数 targetSum ，判断该树中是否存在 根节点到叶子节点 的路径，这条路径上所有节点值相加等于目标和 targetSum 。
叶子节点 是指没有子节点的节点。

示例 1：
       5
     /  \
    4    8
   /    / \
  11   13  4
 / \        \
7   2        1
输入：root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
输出：true

示例 2：
       1
     /  \
    2    3
输入：root = [1,2,3], targetSum = 5
输出：false

示例 3：
输入：root = [1,2], targetSum = 0
输出：false
 
提示：
树中节点的数目在范围 [0, 5000] 内
-1000 <= Node.val <= 1000
-1000 <= targetSum <= 1000
"""


THINKING = """
递归
起初的思路是求解每一种路径的和，然后再判断targetSum是否存在即可，但是这样没有“短路”机制，就是必须要所有都计算完，才能从里面找出来，而且复杂度较高
然后的思路就是“做减法”，从根节点一直减到叶节点，如果减到叶节点正好是0，则代表有，则是True
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False

        # 到达叶节点之后，判断减到此的值是否和节点值一样就可以了，一样的话就返回True
        if not root.left and not root.right:
            return targetSum == root.val

        # 到达叶节点之前，对左、右节点递归，有任意为True，就表示有路径和=targetSum
        return self.hasPathSum(root.left, targetSum-root.val) or self.hasPathSum(root.right, targetSum-root.val)


if __name__ == "__main__":
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
    targetSum = 10
    print(s.hasPathSum(root, targetSum))
