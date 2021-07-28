class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        li=[]
        def inorder(p):
            if p is None:
                return 
            inorder(p.left)
            li.append(p.val)
            inorder(p.right)
        inorder(root1)
        inorder(root2)
        return sorted(li)
