class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def createTree():
    data = input("Enter node value: ")

    if data == "-1":
        return None

    root = Node(int(data))

    print("Enter left child of", root.data)
    root.left = createTree()

    print("Enter right child of", root.data)
    root.right = createTree()

    return root

def mergeTrees(t1, t2):
    if t1 is None:
        return t2
    if t2 is None:
        return t1

    t1.data = t1.data + t2.data

    t1.left = mergeTrees(t1.left, t2.left)
    t1.right = mergeTrees(t1.right, t2.right)

    return t1

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)

print("Enter first tree:")
tree1 = createTree()

print("\nEnter second tree:")
tree2 = createTree()

merged = mergeTrees(tree1, tree2)

print("\nMerged Tree (Inorder):")
inorder(merged)
