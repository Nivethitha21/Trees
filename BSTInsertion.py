class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if root is None:
            return TreeNode(val)
        if val<root.val:
            if root.left:
                self.insertIntoBST(root.left,val)
            else:
                node=TreeNode(val)
                root.left=node
        else:
            if root.right:
                self.insertIntoBST(root.right,val)
            else:
                node=TreeNode(val)
                root.right=node
        return root
