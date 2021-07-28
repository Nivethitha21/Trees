class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        if root is None:
            return 0
        sum=0
        queue=[]
        queue.append(root)
        while(len(queue)):
            lenLev=len(queue)
            sum=0
            for i in range(lenLev):
                node=queue.pop(0)
                sum+=node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return sum
        
