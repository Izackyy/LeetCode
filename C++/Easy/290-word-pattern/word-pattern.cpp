class Solution {
public:
    bool wordPattern(string pattern, string s) {
        unordered_map<char, string> mapPS;
        unordered_map<string, char> mapSP;
        istringstream iss(s);
        string word;

        for (char ch : pattern) {
            iss >> word;

            if (mapPS.count(ch)) {
                if (mapPS[ch] != word)
                    return false;
            }
            else {
                mapPS[ch] = word;
            }

            if (mapSP.count(word)) {
                if (mapSP[word] != ch)
                    return false;
            }
            else {
                mapSP[word] = ch;
            }
        }
        if (iss >> word)
            return false;

        return true;
    }
};