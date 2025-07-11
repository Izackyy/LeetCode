class Solution {
public:
    string convertToTitle(int columnNumber) {
        int n = columnNumber;
        string s;

        while (n > 0) {
            n -= 1;
            s.insert(0, 1, 'A' + n % 26);
            n /= 26;
        }

        return s;
    }
};