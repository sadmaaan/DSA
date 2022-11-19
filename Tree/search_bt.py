from queue import Queue

class TreeNode():
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None

def search_level_order(root, value):
    if not root:
        return "tree doesn't exist"
    else:
        queue = Queue()
        queue.put(root)

        while not queue.empty():
            root_node = queue.get()
            if root_node.data == value:
                return "found!!!"
            
            if root_node.left is not None:
                queue.put(root_node.left)
            
            if root_node.right is not None:
                queue.put(root_node.right)
        
        return "not found :)"



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

    print(search_level_order(b_tree, "coffee"))