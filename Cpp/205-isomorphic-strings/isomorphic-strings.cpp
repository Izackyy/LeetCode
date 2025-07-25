class Solution {
public:
    bool isIsomorphic(string s, string t) {
        unordered_map<char, char> mapST, mapTS;

        for (int i = 0; i < s.length(); i++) {
            if (mapST.count(s[i])) {
                if (mapST[s[i]] != t[i]) {
                    return false;
                }
            }
            else {
                mapST[s[i]] = t[i];
            }

            if (mapTS.count(t[i])) {
                if (mapTS[t[i]] != s[i]) {
                    return false;
                }
            }
            else {
                mapTS[t[i]] = s[i];
            }
        }

        return true;
    }
};