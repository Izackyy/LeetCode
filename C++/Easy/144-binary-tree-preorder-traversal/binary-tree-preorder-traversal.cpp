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
    vector<int> preorderTraversal(TreeNode* root) {
        if (root == NULL) {
            return {};
        }

        stack<TreeNode*> stack;
        vector<int> result;
        TreeNode* temp;
        stack.push(root);

        while(!stack.empty()) {
            temp = stack.top();
            result.push_back(temp->val);
            stack.pop();

            if (temp->right != NULL)
                stack.push(temp->right);
            if (temp->left != NULL)
                stack.push(temp->left);
        }

        return result;
    }
};