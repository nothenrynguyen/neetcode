class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        vector<vector<int>> freq(nums.size() + 1);
        unordered_map<int, int> mp;

        for (int i = 0; i < nums.size(); i++) {
            mp[nums[i]]++; // hashmap of frequencies
        }
        for (const auto& n : mp) {
            freq[n.second].push_back(n.first); // map the second part of each hashmap element (the frequency) to the same index in freq and insert the first part of the element (the num)
        }
        vector<int> res;
        for (int i = freq.size()-1; i > 0; i--) {
            for (int n : freq[i]) {
                res.push_back(n); // from right to left (biggest freq to lowest), push back the nums until we get k elements
                if (res.size() == k)
                    return res;
            }
        }
        return res;
    }
};
