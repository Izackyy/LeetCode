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
    vector<int> postorderTraversal(TreeNode* root) {
        if (root == NULL) 
            return {};
        
        vector<int> result;
        stack<TreeNode*> stack;
        TreeNode* temp, *lastVisited;
        stack.push(root);

        while (!stack.empty()) {
            temp = stack.top();
            if ((temp->left != NULL) && (temp->left != lastVisited) && (temp->right != lastVisited)) {
                stack.push(temp->left);
            }
            else if ((temp->right != NULL) && (temp->right != lastVisited)) {
                stack.push(temp->right);
            }
            else {
                result.push_back(temp->val);
                lastVisited = temp;
                stack.pop();
            }
        }

        return result;
    }
};