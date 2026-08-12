class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int h) {
        // hours must be at least the num of piles otherwise even if we take the largest pile as our k val koko can't eat all (if in mock we should ask this edgecase)
        // therefore, MAX k will be the val of the largest pile
        // 1) brute force: try each k starting from 1 to the largest pile and iterate thru arr to see if we can get thru all piles within the time limit
        // 2) binary search on brute force method (narrows down the ks we test --> O((max(piles)*p)) to O(log(max(piles)*p))
        int low = 1, high = *max_element(piles.begin(), piles.end()); // slowest possible speed is 1 and fastest is largest pile
        int ans = high;
        while (low <= high) {
            int mid = low + (high-low)/2;
            long long totalTime = 0;
            for (int i : piles) {
                totalTime += ceil((double)i/mid);
            }
            if (totalTime <= h) { // if koko can finish within h hours then mid is a valid answer and try to find an even smaller speed by searching the left half, if koko needs too many hours then mid is too slow and search right half for a larger speed
                ans = mid;
                high = mid - 1;
            }
            else
                low = mid + 1;
        }
        return ans;
    }
};
