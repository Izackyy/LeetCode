class Solution {
public:
    bool isPalindrome(string s) {
        string reverse;
        for (int i = s.length() - 1; i >= 0; i--) {
            if (isalnum(s[i])) {
                s[i] = tolower(s[i]);
                reverse += s[i];
            }
            else {
                s.erase(i, 1);
            }
        }

        return s == reverse;
    }
};