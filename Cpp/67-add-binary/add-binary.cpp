class Solution {
public:
    string addBinary(string a, string b) {
        string result;
        int i = a.length() - 1;
        int j = b.length() - 1;
        int carry = 0;

        while (i >= 0 || j >= 0) {
            int x = (i >= 0) ? a[i] - '0' : 0;
            int y = (j >= 0) ? b[j] - '0' : 0;
            int sum = x + y + carry;

            if (sum == 0 || sum == 1) {
                result.insert(result.begin(), sum + '0');
                carry = 0;
            }
            else if (sum == 2) {
                result.insert(result.begin(), '0');
                carry = 1;
            }
            else {
                result.insert(result.begin(), '1');
                carry = 1;                
            }

            i--;
            j--;
        }

        if (carry == 1) {
            result.insert(result.begin(), '1');
        }

        return result;
    }
};