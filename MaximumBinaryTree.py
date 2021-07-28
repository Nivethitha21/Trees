class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if len(nums)==0:
            return 
        max1=max(nums)
        i=nums.index(max1)
        rootNode=TreeNode(max1)
        rootNode.left=self.constructMaximumBinaryTree(nums[:i])
        rootNode.right=self.constructMaximumBinaryTree(nums[i+1:])
        return rootNode
