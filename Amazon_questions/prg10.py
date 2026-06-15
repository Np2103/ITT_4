def check(root):
    level = [-1]

    def solve(node, depth):
        if not node:
            return True

        if not node.left and not node.right:
            if level[0] == -1:
                level[0] = depth
                return True
            return level[0] == depth

        return solve(node.left, depth + 1) and solve(node.right, depth + 1)

    return 1 if solve(root, 0) else 0
