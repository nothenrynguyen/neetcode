class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        // can there b duplicates? non-decreasing order --> yes(?)
        int rows = matrix.size();
        int cols = matrix[0].size();
        // check if target is within bounds of each row aka btwn first and last element of row 
        for (int i = 0; i < matrix.size(); i++) { // iterate thru all rows
            // perform binary search
            if (target >= matrix[i][0] && target <= matrix[i][cols-1]) {
                int left = 0, right = cols-1;
                int m = (right-left)/2;
                while (left <= right) {
                    if (target > matrix[i][left]) {
                        left++;
                    }
                    else if (target < matrix[i][right])
                        right--;
                    else
                        return true;
                }
            }
            else
                continue;
        }
        return false;
    }
};
