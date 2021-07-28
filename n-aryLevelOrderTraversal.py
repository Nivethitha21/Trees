class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root is None:
            return 
        queue=[]
        queue.append(root)
        li=[]
        while(len(queue)):
            lenLev=len(queue)
            temp=[]
            for i in range(lenLev):
                node=queue.pop(0)
                temp.append(node.val)
                for child in node.children:
                    queue.append(child)
            li.append(temp)
        return li
