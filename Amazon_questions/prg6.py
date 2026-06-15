def isBST(root):
    def solve(node, low, high):
        if not node:
            return True

        if node.data <= low or node.data >= high:
            return False

        return solve(node.left, low, node.data) and solve(node.right, node.data, high)

    return 1 if solve(root, float('-inf'), float('inf')) else 0
