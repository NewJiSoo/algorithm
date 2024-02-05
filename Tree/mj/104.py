# https://leetcode.com/problems/maximum-depth-of-binary-tree/description/

from collections import deque


def maxDepth(root):
    depth = 0
    if root is None:
        return depth
    q = deque()
    q.append((root, 1))
    while q:
        cur_node, cur_depth = q.popleft()
        depth = max(depth, cur_depth)
        if cur_node.left:
            q.append((cur_node.left, cur_depth+1))
        if cur_node.right:
            q.append((cur_node.right, cur_depth+1))

    return depth


root = [3, 9, 20, None, None, 15, 7]


class TreeNode:
    def __init__(self, left=None, right=None, v=0):
        self.left = left
        self.right = right
        self.v = v


root = TreeNode(v=3)
root.left = TreeNode(v=9)
root.right = TreeNode(v=20)
root.left.left = TreeNode(v=15)
root.right.right = TreeNode(v=7)

print(maxDepth(root))
