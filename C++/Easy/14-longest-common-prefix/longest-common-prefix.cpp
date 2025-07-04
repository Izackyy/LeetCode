class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        if (strs.empty()) 
            return "";

        string temp = strs[0];

        for (int i = 1; i < strs.size(); i++) {
            while (strs[i].find(temp) != 0) {
                temp = temp.substr(0, temp.length() - 1);
                if (temp.empty()) 
                    return "";
            }
        }
        return temp;
    }
};