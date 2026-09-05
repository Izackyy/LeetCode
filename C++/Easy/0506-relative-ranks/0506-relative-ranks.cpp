class Solution {
public:
    vector<string> findRelativeRanks(vector<int>& score) {
        unordered_map<int, int> m;
        vector<int> pos = score;
        sort(pos.begin(), pos.end(), greater<int>());
        vector<string> rank(size(score));

        for (int i = 0; i < size(score); i++) {
            m[score[i]] = i;
        }
        for (int j = 0; j < size(rank); j++) {
            if (j == 0) {
                rank[m[pos[j]]] = "Gold Medal";
            }
            else if (j == 1) {
                rank[m[pos[j]]] = "Silver Medal";
            }
            else if (j == 2) {
                rank[m[pos[j]]] = "Bronze Medal";
            } else {
                rank[m[pos[j]]] = to_string(j + 1);
            }
        }

        return rank;
    }
};
