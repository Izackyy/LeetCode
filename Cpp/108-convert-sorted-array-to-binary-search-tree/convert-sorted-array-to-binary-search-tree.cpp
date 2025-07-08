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
    TreeNode* sortedArrayToBST(vector<int>& nums) {
        if (nums.size() == 0) 
            return NULL;
        if (nums.size() == 1) {
            TreeNode* root = new TreeNode(nums[0]);
            return root;
        }

        int mid = nums.size() / 2;
        TreeNode* root = new TreeNode(nums[mid]);

        vector<int> left;
        left.assign(nums.begin(), nums.begin() + mid);
        root->left = sortedArrayToBST(left);

        vector<int> right;
        right.assign(nums.begin() + 1 + mid, nums.end());
        root->right = sortedArrayToBST(right);

        return root;
    }
};