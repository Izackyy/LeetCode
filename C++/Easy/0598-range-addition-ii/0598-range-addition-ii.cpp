class Solution {
public:
    int maxCount(int m, int n, vector<vector<int>>& ops) {
        if (ops.size() == 0) return m * n;

        int r = m, c = n;

        for (auto& op : ops) {
            r = min(r, op[0]);
            c = min(c, op[1]);
        }

        return r * c;
    }
};
