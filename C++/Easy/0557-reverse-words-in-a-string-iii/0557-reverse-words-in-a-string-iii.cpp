class Solution {
public:
    string reverseWords(string s) {
        int start = 0;

        for (int end = 1; end <= s.size(); end++) {
            if (s[end] == ' ' || end == s.size()) {
                reverse(s.begin() + start, s.begin() + end);
                start = end + 1;
            }
        }

        return s;
    }
};
