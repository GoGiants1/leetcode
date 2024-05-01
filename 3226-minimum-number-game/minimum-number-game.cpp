class Solution {
public:
    vector<int> numberGame(vector<int>& nums) {
        // even length (include 0 len)
        // A pop, B pop from nums -> B push, A push to arr
        // 풀이법: sort.
        std::sort(nums.begin(), nums.end());

        // vector<int> arr;
        // for(int i = 0; i < nums.size(); i += 2){
        //     arr.push_back(nums[i+1]);
        //     arr.push_back(nums[i]);
        // }

        // return arr;
        for(int i = 0; i < nums.size(); i += 2){
            std::swap(nums[i], nums[i+1]);
        }
        return nums;
    }
};