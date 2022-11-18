class TreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None


if __name__ == '__main__':
    b_tree = TreeNode("Drinks")
    left = TreeNode("hot")
    right = TreeNode("cold")
    b_tree.left = left
    b_tree.right = right

    print(b_tree.left.data)