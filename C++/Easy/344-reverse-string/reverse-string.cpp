class Solution {
public:
    void reverseString(vector<char>& s) {
        int n = s.size();
        if (n == 1)
            return;
        int start = 0, end = n - 1;

        while (start < end) {
            char temp = s[start];
            s[start] = s[end];
            s[end] = temp;
            start++, end--;
        }
    }
};