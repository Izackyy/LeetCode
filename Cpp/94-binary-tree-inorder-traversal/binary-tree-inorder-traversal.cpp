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
    vector<int> inorderTraversal(TreeNode* root) {
        stack<TreeNode*> stack;
        vector<int> result;
        TreeNode* cur = root;

        while (cur != nullptr || !stack.empty()) {
            while (cur != nullptr) {
                stack.push(cur);
                cur = cur->left;
                }

            cur = stack.top();
            result.push_back(cur->val);
            stack.pop();
            cur = cur->right;
        }

        return result;
    }
};