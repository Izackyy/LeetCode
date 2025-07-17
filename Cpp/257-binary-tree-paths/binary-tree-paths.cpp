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
    vector<string> binaryTreePaths(TreeNode* root) {
        if (root == NULL) 
            return {};

        vector<string> result;
        string temp;

        dfs(root, temp, result);

        return result;
    }

private:
    void dfs(TreeNode* root, string temp, vector<string> &result) {
        if (root == NULL) 
            return;
        
        temp += to_string(root->val) + "->";

        if (root->left == NULL && root->right == NULL) {
            temp.resize(temp.length() - 2);
            result.push_back(temp);
            return;
        }
        dfs(root->left, temp, result);
        dfs(root->right, temp, result);
    }
};