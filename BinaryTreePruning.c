int containsOne(struct TreeNode* node)
{
    if (node==NULL)
        return 0;
    int l=containsOne(node->left);
    int r=containsOne(node->right);
    if(l==0)
        node->left=NULL;
    if(r==0)
        node->right=NULL;
    return node->val==1 || l ||r;
}
struct TreeNode* pruneTree(struct TreeNode* root){
    return containsOne(root)?root:NULL;
    }
