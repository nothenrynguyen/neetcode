class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        // 1. sorting but doesn't fit the time complexity constraints
        // sort(nums.begin(), nums.end());
        // int count = 1;
        // int maxCount = 1;
        // if (nums.size() == 0 || nums.size() == 1) {
        //     return nums.size();
        // }
        // for (int i = 1; i < nums.size(); i++) {
        //     if (nums[i] == nums[i-1]+1)
        //         count++;
        //     else if (nums[i] == nums[i-1])
        //         continue;
        //     else {
        //         maxCount = max(maxCount, count);
        //         count = 1;
        //     }
        // }
        // return max(maxCount, count);

        // 2. Hashset
        unordered_set<int> ms(nums.begin(), nums.end());
        int maxCount = 0;
        for (int n : ms) {
            if (!ms.contains(n-1)) { // a num is the start of a sequence if num-1 is not in the set aka if num-1 is in the set, we loop until sequence breaks
                int length = 1;
                while (ms.contains(n+length)) {
                    length++;
                }
                maxCount = max(maxCount, length);
            }
        }
        return maxCount;
    }
};
