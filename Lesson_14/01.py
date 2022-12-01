class Tree:
    def __init__(self, id_node):
        self.key = id_node
        self.left = None
        self.right = None


def insert_list(lst, i):
    """Insert function from a list """
    root_new = None

    # Base case for recursion
    if i < NUM:
        root_new = Tree(lst[i])

        # insert left child
        root_new.left = insert_list(lst, 2 * i + 1)

        # insert right child
        root_new.right = insert_list(lst, 2 * i + 2)
    return root_new


def inorder(root):
    """Print tree nodes in inorder fashion"""
    if root is not None:
        inorder(root.left)
        print(root.key, end=" ")
        inorder(root.right)


list_data = [20, 30, 40, 50, 60, 70, 80]
NUM = len(list_data)
root_from_list = insert_list(list_data, 0)
inorder(root_from_list)