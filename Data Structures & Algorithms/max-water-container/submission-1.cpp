class Solution {
public:
    int maxArea(vector<int>& heights) {
        int left = 0;
        int right = heights.size()-1;
        int best = 0;

        while (right > left) {
            int area = min(heights[right], heights[left]) * (right-left);
            best = max(area, best);
            if (heights[left] <= heights[right]) 
                left++;
            else
                right--;
        }
        return best;
    }
};
