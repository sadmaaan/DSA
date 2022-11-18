from queue import Queue

class TreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None

def pre_order(root):
    if not root:
        return
    
    print(root.data)
    pre_order(root.left)
    pre_order(root.right)

def in_order(root):
    if not root:
        return

    in_order(root.left)
    print(root.data)
    in_order(root.right)

def post_order(root):
    if not root:
        return

    post_order(root.left)
    post_order(root.right)
    print(root.data)

def level_order(root):
    if not root:
        return 
    else:
        queue = Queue()
        queue.put(root)

        while not queue.empty():
            root_node = queue.get()
            print(root_node.data)

            if root_node.left is not None:
                # print(root_node.left.data)
                queue.put(root_node.left)

            if root_node.right is not None:
                # print(root_node.data)
                queue.put(root_node.right)


if __name__ == '__main__':
    b_tree = TreeNode("Drinks")
    left = TreeNode("hot")
    right = TreeNode("cold")
    b_tree.left = left
    b_tree.right = right

    left_hot = TreeNode("tea")
    right_hot = TreeNode("coffee")
    left.left = left_hot
    left.right = right_hot
    left_hot.left = TreeNode("green tea")
    left_hot.right = TreeNode("milk tea")

    # print(b_tree.left.data)
    
    # pre_order(b_tree)
    # in_order(b_tree)
    # post_order(b_tree)
    level_order(b_tree)
