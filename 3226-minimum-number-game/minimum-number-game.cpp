class Solution {
public:
    vector<int> numberGame(vector<int>& nums) {
        // even length (include 0 len)
        // A pop, B pop from nums -> B push, A push to arr
        // 풀이법: sort.
        vector<int> arr;
        std::sort(nums.begin(), nums.end());

        for(int i = 0; i < nums.size(); i += 2){
            arr.push_back(nums[i+1]);
            arr.push_back(nums[i]);
        }

        return arr;
    }
};