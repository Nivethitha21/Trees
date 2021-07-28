class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        if root is None:
            return 0
        queue=[]
        sum=0
        queue.append(root)
        while(len(queue)):
            node=queue.pop(0)
            print(node.val)
            if node.val%2==0:
                # print("in")
                if node.left:
                    if node.left.left:
                        sum+=node.left.left.val
                    if node.left.right:
                        sum+=node.left.right.val
                if node.right:
                    if node.right.left:
                        sum+=node.right.left.val
                    if node.right.right:
                        sum+=node.right.right.val
            if node.left:
                if node.left.left or node.left.right:
                    queue.append(node.left)
            if node.right:
                if node.right.right or node.right.left:
                    queue.append(node.right)
        return sum
                
        
