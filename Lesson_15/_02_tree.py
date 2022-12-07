class Node:
    def __init__(self, main_root):
        self.main_root = main_root
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.main_root)

    def insert(self, data):
        if self.main_root:
            if data < self.main_root:
                if self.left is None:
                    self.left =Node(data)
                else:
                    self.left.insert(data)
            elif data > self.main_root:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.main_root.insert(data)

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.main_root)
        if self.right:
            self.right.print_tree()

    def list_insert(self, lst):
        for n in lst:
            self.insert(n)

    def min_value(self):
        while self.left is not None:
            self = self.left
        return str(self)

    def max_value(self):
        while self.right is not None:
            self = self.right
        return str(self)

    def delete_node(root, key):
        if root is None:
            return root
        if key < root.main_root:
            root.left = root.left.delete_node(key)
        elif key > root.main_root:
            root.right = root.right.delete_node(key)
        else:
            if root.left is None:
                temp = root.right
                return temp
            elif root.right is None:
                temp = root.left
                return temp
            temp = root.right.minValueNode()
            root.main_root = temp.main_root
            root.right = root.right.deleteNode(temp.main_root)
        return root


# root = Node(10)
# root.print_tree()
# print()
# root.list_insert([70, 60, 40, 50])
# root.print_tree()
# print()
# root.delete_node(50)
# root.print_tree()
# print("---")
# print(root.min_value())
# root.max_value()
