class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        q=[]
        q.append(root)
        li=[]
        
        while(q):
            sum=0
            lenLev=len(q)
            for i in range(lenLev):
                node=q.pop(0)
                sum+=node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            li.append(sum)
        return li.index(max(li))+1
                
