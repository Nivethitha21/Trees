class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        li=[]
        def inOrd(root):
            if root is None:
                return 
            inOrd(root.left)
            li.append(root.val)
            inOrd(root.right)
        inOrd(root)
        print(li)
        v=li[len(li)-1]
        for i in range(len(li)-2,-1,-1):
            li[i]=li[i]+v
            v=li[i]
            
        print(li)
        def inOrder(root):
            if root is None:
                return 
            inOrder(root.left)
            root.val=li.pop(0)
            print(root.val)
            inOrder(root.right)
        inOrder(root)
        return root
