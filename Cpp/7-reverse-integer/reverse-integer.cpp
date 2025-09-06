class Solution {
public:
    int reverse(int x) {
        int ans = 0;
        int max = 2147483647, min = -2147483648;
        
        while (x != 0) {
            int temp = x % 10;
            if ((ans > max / 10) || (ans < min / 10)) 
                return 0;
            ans = ans * 10 + temp;
            x /= 10;
        }

        return ans;
    }
};