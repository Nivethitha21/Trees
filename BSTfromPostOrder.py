class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        head = root = TreeNode(preorder.pop(0))
        while preorder:
            temp=preorder.pop(0)
            while(root):
                if temp>root.val:
                    if not root.right:
                        root.right=TreeNode(temp)
                        break
                    root=root.right
                if temp<root.val:
                    if not root.left:
                        root.left=TreeNode(temp)
                        break
                    root=root.left
            root=head
        return head
