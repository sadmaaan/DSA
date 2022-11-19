from queue import Queue

class TreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None


def level_order_travarsal(root):
    if not root:
        return
    else:
        queue = Queue()
        queue.put(root)

        while not queue.empty():
            root_node = queue.get()
            print(root_node.data)

            if root_node.left is not None:
                queue.put(root_node.left)
            if root_node.right is not None:
                queue.put(root_node.right)

def get_deepest_node(root):
    if not root:
        return
    else:
        queue = Queue()
        queue.put(root)

        while not queue.empty():
            root_node = queue.get()

            if root_node.left is not None:
                queue.put(root_node.left)
            if root_node.right is not None:
                queue.put(root_node.right) 
        
        return root_node # deepest node

def delete_deepest_node(root, deepest_node):
    if not root:
        return
    else:
        queue = Queue()
        queue.put(root)

        while not queue.empty():
            root_node = queue.get()
            if root_node is deepest_node:
                root_node = None
                # print("deleted successfully!")
                return

            if root_node.right is not None:
                if root_node.right is deepest_node:
                    root_node.right = None
                    # print("deleted successfully!")
                    return
                else:
                    queue.put(root_node.left)
            if root_node.left is not None:
                if root_node.left is deepest_node:
                    root_node.left = None
                    # print("deleted successfully!")
                    return
                else:
                    queue.put(root_node.right)     

def delete(root, value):
    if not root:
        return "value doesn't esist!"
    else:
        queue = Queue()
        queue.put(root)

        while not queue.empty():
            root_node = queue.get()

            if root_node.data == value:
                deepest_node = get_deepest_node(root)
                root_node.data = deepest_node.data
                delete_deepest_node(root, deepest_node)
                return "deleted successfully!"
            if root_node.left is not None:
                queue.put(root_node.left)
            if root_node.right is not None:
                queue.put(root_node.right) 

def delete_BT(root):
    root.data = None
    root.left = None
    root.right = None

    return "BT deleted successfully!"


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


    # level_order_travarsal(root)
    # deepest_node = get_deepest_node(root).data
    # print("deepest node:", deepest_node)
    # delete_deepest_node(root, deepest_node)
    # delete(root, "coffee")
    delete_BT(root)
    level_order_travarsal(root)