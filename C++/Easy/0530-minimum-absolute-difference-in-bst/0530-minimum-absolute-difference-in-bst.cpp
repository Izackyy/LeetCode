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
    int min_diff = 1e5 + 1;
    int prev_val = -1;

    int getMinimumDifference(TreeNode* root) {
        inorder(root);
        return min_diff;
    }

private: 
    void inorder(TreeNode* node) {
        if (node == nullptr) return;

        inorder(node->left);
        if (prev_val != -1) {
            min_diff = min(min_diff, abs(node->val - prev_val));
        }
        prev_val = node->val;
        inorder(node->right);
    }
};
