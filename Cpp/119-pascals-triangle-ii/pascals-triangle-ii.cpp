class Solution {
public:
    vector<int> getRow(int rowIndex) {
        if (rowIndex == 0)
            return {1};
        
        vector<vector<int>> result(rowIndex + 1);

        for (int i = 0; i < rowIndex + 1; i++) {
            result[i].resize(i + 1, 1);
        }

        for (int i = 2; i < rowIndex + 1; i++) {
            for (int j = 1; j < result[i].size() - 1; j++) {
                result[i][j] = result[i - 1][j - 1] + result[i - 1][j];
            }
        }

        return result[rowIndex];
    }
};