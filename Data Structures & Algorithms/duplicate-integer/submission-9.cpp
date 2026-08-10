class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
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