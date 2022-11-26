from queue import Queue

class BSTNode:
    def __init__(self, data = None) -> None:
        self.data = data
        self.left_child = None
        self.right_child = None
        
def insert(root, value):
    if root.data == None:
        root.data = value
    elif value <= root.data:
        if root.left_child is None:
            root.left_child = BSTNode(value)
        else:
            insert(root.left_child, value)
    else:
        if root.right_child is None:
            root.right_child = BSTNode(value)
        else:
            insert(root.right_child, value)
    
    return "inserted successfully"

def search(root, value):
    if root == None:
        return "not found"
    if root.data == value:
        return "found"
    elif value <= root.data:
        return search(root.left_child, value)
    else:
        return search(root.right_child, value)


def in_order(root):
    if not root:
        return
    
    in_order(root.left_child)
    print(root.data)
    in_order(root.right_child)

def min_value_node(root):
    temp = root
    
    while temp.left_child is not None:
        temp = temp.left_child
    
    return temp

def delete(root, value):
    if root is None:
        return root
    
    if value < root.data:
        root.left_child = delete(root.left_child, value)
    elif value > root.data:
        root.right_child = delete(root.right_child, value)
    else:
        # one child
        if root.left_child is None:
            temp = root.right_child
            root = None
            return temp
        if root.right_child is None:
            temp = root.left_child
            root = None
            return temp
        
        # two child
        temp = min_value_node(root.right)
        root.data = temp.data

        root.right_child = delete(root.right_vhild, temp.data)
    
    return root

root = BSTNode()
print(insert(root, 10))
print(insert(root, 40))
print(insert(root, 20))
print(insert(root, 5))
print(insert(root, 15))
print(insert(root, 100))
print(insert(root, 120))
print(insert(root, 180))

in_order(root)
print(search(root, 1000))

root = delete(root, 120)
in_order(root)

root = delete(root, 5)
in_order(root)

