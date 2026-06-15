def bToDLL(root):
    head = None
    prev = None

    def inorder(node):
        nonlocal head, prev

        if not node:
            return

        inorder(node.left)

        if prev is None:
            head = node
        else:
            prev.right = node
            node.left = prev

        prev = node

        inorder(node.right)

    inorder(root)

    return head
