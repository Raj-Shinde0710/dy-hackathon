class Node:
    def __init__(self, city, pop):
        self.city = city
        self.pop = pop
        self.left = None
        self.right = None


def insert(root, city, pop):
    if not root:
        return Node(city, pop)
    if city < root.city:
        root.left = insert(root.left, city, pop)
    elif city > root.city:
        root.right = insert(root.right, city, pop)
    return root


def inorder(root):
    if root:
        inorder(root.left)
        print(root.city, root.pop)
        inorder(root.right)


# Main program
root = None
root = insert(root, "Pune", 5000000)
root = insert(root, "Mumbai", 12000000)
root = insert(root, "Delhi", 18000000)
root = insert(root, "Nagpur", 3000000)

print("Cities in Ascending Order:")
inorder(root)
