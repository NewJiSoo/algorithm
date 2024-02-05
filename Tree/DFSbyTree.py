def dfs(root):
    if root is None:
        return
    dfs(root.left)
    dfs(root.right)


# 전위 순회
def preorder(root):
    if root is None:
        return
    print(root)
    preorder(root.left)
    preorder(root.right)


# 중위 순회
def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root)
    inorder(root.right)


# 후위 순회
def postorder(root):
    if root is None:
        return
    postorder(root.left)
    postorder(root.right)
    print(root)
