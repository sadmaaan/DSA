class Node:
    def __init__(self, data=None) -> None:
        self.data = data
        self.left  = None
        self.right = None

class BinaryTree:
    def __init__(self) -> None:
        self.root = None
    
    # insert
    def insert(self, data):
        val = Node(data)

        if self.root is None:
            self.root = val
        
        current_node = self.root

        while True:
            if current_node.left is None:
                current_node.left = val
                break 

            current_node = current_node.left

            if current_node.right is None:
                current_node.right = val
                break
            current_node = current_node.right
        return self.root
    
    # travarsal -> in-order
    def in_order(self, node):
        if node.left:
            self.in_order(node.left)
        print(node.data)
        if node.right:
            self.in_order(node.right)  
          
    def PreOrder(self,root):
        if root == None:
            pass
        else:
            print(root.data)
            self.PreOrder(root.left)
            self.PreOrder(root.right)
        

if __name__ == '__main__':
    tree = BinaryTree()
    tree.insert(2)
    tree.insert(3)
    tree.insert(4)
    print(tree.root)
    tree.PreOrder(tree.root)
