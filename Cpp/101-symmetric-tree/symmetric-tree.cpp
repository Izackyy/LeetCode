/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    bool isSymmetric(TreeNode* root) {
        if (root == NULL) 
            return 1;

        return mirrorTree(root->left, root->right);
    }

private:
    bool mirrorTree(TreeNode* p, TreeNode* q) {
        if (p == NULL && q == NULL)
            return 1;
    
        if (p == NULL || q == NULL || p->val != q->val)
            return 0;

        return mirrorTree(p->left, q->right) && mirrorTree(p->right, q->left);
    }
};