class Solution {
public:
    int findMin(vector<int> &nums) {
        // 1. Brute force: go through every element and then find the minimum value
        int l = 0, r = nums.size()-1;
        while (l < r) {
            int mid = l + (r-l) / 2; // use the overflow-safe formula instead of the traditional (l+r)/2, rounds down automatically
            if (nums[mid] > nums[r]) {
                l = mid+1; // the min must be somewhere after l
            }
            else
                r = mid; // mid could be the minimum
        }
        return nums[l];
    }
};
