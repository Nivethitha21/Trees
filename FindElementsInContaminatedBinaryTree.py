class FindElements:

    def __init__(self, root: TreeNode):
        self.mapping = {}
        root.val = 0

        def correct(node):
            if node:
                self.mapping[node.val] = 1
                if node.left:
                    node.left.val = 2 * node.val + 1
                    correct(node.left)
                if node.right:
                    node.right.val = 2 * node.val + 2
                    correct(node.right)
        correct(root)

    def find(self, target: int) -> bool:
        return True if self.mapping.get(target) else False
