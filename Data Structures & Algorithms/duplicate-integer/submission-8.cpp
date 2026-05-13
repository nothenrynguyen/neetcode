class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        // 1) brute force: sort and then traverse using 2 pointers
        // 2) hashmap for frequencies
        // 3) set to compare lengths
        unordered_set<int> ms;
        for (int i = 0; i < nums.size(); i++) {
            ms.insert(nums[i]);
        }

        if (nums.size() > ms.size())
            return true;
        else
            return false;
    }
};