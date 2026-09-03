class Solution {
public:
    vector<string> generateParenthesis(int n) {
        string str;
        vector<string> result;
        parenthesis(result, str, n, n);
        
        return result;
    }

    void parenthesis(vector<string> &result, string &str, int left, int right) {
        if (left == 0 && right == 0) {
            result.push_back(str);
            return;
        }
        if (left > 0) {
            str.push_back('(');
            parenthesis(result, str, left - 1, right);
            str.pop_back();
        }
        if (left < right) {
            str.push_back(')');
            parenthesis(result, str, left, right - 1);
            str.pop_back();
        }
    }
};