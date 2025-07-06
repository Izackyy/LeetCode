class Solution {
public:
    bool isValid(string s) {
        vector<char> stack;

        for (int i = 0; i < s.length(); i++) {
            if (!stack.empty() &&
                ((peek(stack) == '(' && s[i] == ')') ||
                (peek(stack) == '{' && s[i] == '}') ||
                (peek(stack) == '[' && s[i] == ']'))) {
                pop(stack);
            }
            else {
                push(stack, s[i]);
            }
        }

        return stack.empty();
    }

private:
    void push(vector<char> &stack, char x) {
        stack.push_back(x);
    }
    void pop(vector<char> &stack) {
        if (stack.empty()) {
            cout << "Stack empty" << endl;
        }
        else {
            stack.pop_back();
        }
    }
    char peek(vector<char> &stack) {
        return stack.back();
    }
};