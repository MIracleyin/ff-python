# *coding: utf-8 -*
# !@time: 2021-03-19 18:57:59
# !@author: miracleyin @email: [miracleyin@live.com](mailto:miracleyin@live.com)
# !@question title: same-tree

# 给你两棵二叉树的根节点 p 和 q ，编写一个函数来检验这两棵树是否相同。 
# 
#  如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：p = [1,2,3], q = [1,2,3]
# 输出：true
#  
# 
#  示例 2： 
# 
#  
# 输入：p = [1,2], q = [1,null,2]
# 输出：false
#  
# 
#  示例 3： 
# 
#  
# 输入：p = [1,2,1], q = [1,1,2]
# 输出：false
#  
# 
#  
# 
#  提示： 
# 
#  
#  两棵树上的节点数目都在范围 [0, 100] 内 
#  -104 <= Node.val <= 104 
#  
#  Related Topics 树 深度优先搜索 
#  👍 586 👎 0

from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
import collections
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def generate_tree(self, nums):
        def level(index):
            if index >= len(nums):
                return None
            root = TreeNode(nums[index])
            root.left = level(2 * index + 1)
            root.right = level(2 * index + 2)
            return root
        return level(0)

class Solution:
    def isSameTree_dfs(self, p: TreeNode, q: TreeNode) -> bool:
        if (p == None and q == None): # 两个都空
            return True
        elif (p == None or q == None):# 现在不可能两个都空，只可能一空 一不空
            return False
        # 现在只可能两个都不空则比较值
        elif (p.val != q.val): # 如果两个值不同，那么假
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

    def isSameTree_bfs(self, p: TreeNode, q: TreeNode) -> bool:
        if (p == None and q == None):
            return True
        elif (p == None and q == None):
            return False
        queueQ = [p]
        queueP = [q]

        while queueQ and queueP:
            nodeQ = queueQ.pop(0)
            nodeP = queueP.pop(0)
            if nodeP.val != nodeQ.val:
                return False
            leftP, rightP = nodeP.left, nodeP.right
            leftQ, rightQ = nodeQ.left, nodeQ.right
            if (not leftP) ^ (not leftQ):
                return False
            if (not rightP) ^ (not rightQ):
                return False
            if leftP:
                queueP.append(leftP)
            if leftQ:
                queueQ.append(leftQ)
            if rightP:
                queueP.append(rightP)
            if rightQ:
                queueQ.append(rightQ)
        return not queueP and not queueQ



# leetcode submit region end(Prohibit modification and deletion)
def main():
    p = TreeNode().generate_tree([1, 2, 3, 4, 5])
    q = TreeNode().generate_tree([1, 2, 3, 4, 5, 6])

    res = Solution().isSameTree_bfs(p ,q)
    print(res)
main()