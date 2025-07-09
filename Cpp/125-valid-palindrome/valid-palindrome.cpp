class Solution {
public:
    bool isPalindrome(string s) {
        for (int i = 0; i < s.length(); i++) {
            if (isalnum(s[i])) {
                if (!islower(s[i])) {
                    s[i] = tolower(s[i]);
                }
            }
            else {
                s.erase(i, 1);
                i--;
            }
        }
        string reverse;
        for (int i = s.length() - 1; i >= 0; i--) {
            reverse += s[i];
        }

        return s == reverse;
    }
};