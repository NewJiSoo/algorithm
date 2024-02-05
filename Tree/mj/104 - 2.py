# https://leetcode.com/problems/maximum-depth-of-binary-tree/description/

def maxDepth(root):
    max_depth = 0

    if root is None:
        return 0
    left_depth = maxDepth(root.left)
    right_depth = maxDepth(root.right)
    max_depth = max(left_depth, right_depth) + 1

    return max_depth


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
