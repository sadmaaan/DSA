class BinaryTree:
    def __init__(self, size) -> None:
        self.custom_list = size * [None]
        self.last_used_index = 0
        self.max_size = size

    def insert(self, value):
        if self.last_used_index + 1 == self.max_size:
            return "tree is full!!!"
        
        self.custom_list[self.last_used_index + 1] = value
        self.last_used_index += 1
        return "value inserted successfully!"
    
    def search(self, value):
        for i in range(len(self.custom_list)):
            if self.custom_list[i] == value:
                return "found!!!"
        return "not found!"

    def delete(self, value):
        if self.last_used_index ==0:
            return "tree doesn't exist!"

        for i in range(1, self.last_used_index + 1):
            if self.custom_list[i] == value:
                self.custom_list[i] = self.custom_list[self.last_used_index]
                self.custom_list[self.last_used_index] = None
                self.last_used_index -= 1
                return "node deleted successfully!"
    
    def delete_bt(self):
        self.custom_list = None
        self.last_used_index = 0
        return "tree deleted successfully!"

    
    def pre_order(self, index = 1):
        if index > self.last_used_index:
            return
        
        print(self.custom_list[index])
        self.pre_order(index * 2)
        self.pre_order(index * 2 + 1)
    
    def in_order(self, index = 1):
        if index > self.last_used_index:
            return
        
        self.in_order(index * 2)
        print(self.custom_list[index])
        self.in_order(index * 2 + 1)
    
    def post_order(self, index = 1):
        if index > self.last_used_index:
            return
        
        self.post_order(index * 2)
        self.post_order(index * 2 + 1)
        print(self.custom_list[index])

    def level_order(self, index = 1):
        for i in range(index, self.last_used_index + 1):
            print(self.custom_list[i])

    
        


bt = BinaryTree(8)
bt.insert("Drinks")
bt.insert("hot")
bt.insert("cold")
bt.insert("tea")
bt.insert("coffee")
# print(bt.custom_list, bt.last_used_index)
# print(bt.search("tea"))
# bt.pre_order()
# bt.in_order()
# bt.post_order()
# bt.level_order()
print(bt.delete("hot"))
bt.level_order()
print(bt.custom_list, bt.last_used_index)
print(bt.delete_bt())
print(bt.custom_list, bt.last_used_index)

