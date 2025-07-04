class Solution {
    public:
        int strStr(string haystack, string needle) {
            int n = haystack.size();
            int m = needle.size();
            int charJump[26];

            computeJumps(needle, m, charJump);
            int j = m - 1, k = m - 1;

            while (j < n) {
                if (k < 0) 
                    return j + 1;
                
                if (haystack[j] == needle[k]) {
                    j--;
                    k--;
                }
                else {
                    j += max(charJump[haystack[j] - 'a'], m - k);
                    k = m - 1;
                }
            }
            return -1;
        }

    private:
        void computeJumps(string P, int m, int charJump[]) {
            for (int ch = 0; ch < 26; ch++) {
                charJump[ch] = m;
            }
            for (int k = 0; k < m; k++) {
                charJump[P[k] - 'a'] = m - 1 - k;
            }
        }

};