class Solution {
public:
    bool isPalindrome(int x) {
        
        if (x < 0) 
            return false;

        long result = 0;
        int original = x;
        while (x != 0) {
            int digit = x % 10;
            result = result * 10 + digit;
            x /= 10;
        }
        return (result == original);
    }
};