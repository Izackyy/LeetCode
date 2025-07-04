class Solution {
public:
    bool rotateString(string s, string goal) {  // Boyer Moore Algorithm 
        if (goal.size() != s.size())
            return false;

        string combine = s + s;
        int n = combine.size();
        int m = goal.size();
        int charJump[26];

        computeJumps(goal, m, charJump);
        int j = m - 1, k = m - 1;
        
        while (j < n) {
            if (k < 0) 
                return true;
            
            if (combine[j] == goal[k]) {
                j--;
                k--;
            }
            else {
                j += max(charJump[combine[j] - 'a'], m - k);
                k = m - 1;
            }
        }
        return false;
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