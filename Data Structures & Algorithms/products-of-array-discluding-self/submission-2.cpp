class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        // 1. Brute force: nested loop for every element calculate the total product of every other value but this is incredibly expensive the runtime is O(n^2)
        // 2. Slightly more optimized: find total product and go through nums, replacing the value with the total product divided by current num (except special case 0). runtime much better O(n)
        // 3. Optimized: two sliding windows essentially, prefix and suffix
        int n = nums.size();
        vector<int> res(n);
        vector<int> prefix(n);
        vector<int> postfix(n);
        prefix[0] = 1;
        postfix[n-1] = 1;
        for (int i = 1; i < n; i++) {
            prefix[i] = prefix[i-1] * nums[i-1];
        }
        for (int i = n-2; i >= 0; i--) {
            postfix[i] = postfix[i+1] * nums[i+1];
        }
        for (int i = 0; i < n; i++) {
            res[i] = prefix[i] * postfix[i];
        }
        return res;
    }
};
