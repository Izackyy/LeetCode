class Solution {
public:
    vector<string> findWords(vector<string>& words) {
        unordered_map<char, int> m;
        string qwer = "qwertyuiop";
        string asdf = "asdfghjkl";
        string zxcv = "zxcvbnm";

        for (char c : qwer) m[c] = 1;
        for (char c : asdf) m[c] = 2;
        for (char c : zxcv) m[c] = 3;

        vector<string> ans;

        for (string s : words) {
            int x = m[tolower(s[0])];
            bool check = true;

            for (char ch : s) {
                ch = tolower(ch);
                if (m[ch] != x) {
                    check = false;
                    break;
                }
            }

            if (check) ans.push_back(s);
        }

        return ans;
    }
};
