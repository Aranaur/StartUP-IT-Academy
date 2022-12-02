class Node:
    def __init__(self, main_root):
        self.main_root = main_root
        self.left = None
        self.right = None

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


root = Node(10)
root.print_tree()
print()
root.list_insert([70, 60, 40, 50])
root.print_tree()
