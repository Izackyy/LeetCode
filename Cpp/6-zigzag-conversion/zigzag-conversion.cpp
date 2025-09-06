class Solution {
public:
    string convert(string s, int numRows) {
        if (numRows == 1 || numRows >= s.length()) {
            return s;
        }
        vector<vector<char>> rows(numRows);

        int index = 0, d = 0;
        for (char c : s) {
            rows[index].push_back(c);
            if (index == 0) {
                d = 1;
            } else if (index == numRows - 1) {
                d = -1;
            }
            index += d;
        }
        
        string result;
        for (const auto& col : rows) {
            for (char c : col) {
                result += c;
            }
        }

        return result;
    }
};

