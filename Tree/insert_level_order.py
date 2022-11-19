from queue import Queue

class TreeNode():
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None

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

def insert(root, value):
    val = TreeNode(value)

    if not root:
        return "tree not exist!"
    else:
        queue = Queue()
        queue.put(root)

        while not queue.empty():
            root_node = queue.get()

            if root_node.left is not None:
                queue.put(root_node.left)
            else:
                root_node.left = val
                return "inserted successfully!"

            if root_node.right is not None:
                queue.put(root_node.right)
            else:
                root_node.right = val
                return "inserted successfully!"

if __name__ == '__main__':
    root = TreeNode("Drinks")
    left = TreeNode("hot")
    right = TreeNode("cold")
    root.left = left
    root.right = right

    left_hot = TreeNode("tea")
    right_hot = TreeNode("coffee")
    left.left = left_hot
    left.right = right_hot
    left_hot.left = TreeNode("green tea")
    left_hot.right = TreeNode("milk tea")

    print(insert(root, "coke"))
    print(insert(root, "fanta"))
    level_order(root)