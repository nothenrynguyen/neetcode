class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        vector<int> res;
        int left = 0, right = numbers.size()-1;
        
        while (left < right) {
            int sum = numbers[left]+numbers[right];
            std::cout << "sum: " << sum << endl;
            if (sum == target) {
                std::cout << "1" << endl;
                res.push_back(left+1);
                res.push_back(right+1);
                break;
            }
            else if (sum > target) {
                std::cout << "2" << endl;
                right--;
            }
            else if (sum < target) {
                std::cout << "3" << endl;
                left++;
            }
        }

        return res;
    }
};
