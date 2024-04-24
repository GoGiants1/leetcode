class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        map<int, int> needed = {};  // (number, index)
        vector<int> ans;
        int idx = 0;
        for (auto n: nums){
            if (needed.count(target - n) > 0) {
                ans.push_back(idx);
                ans.push_back(needed[target - n]);
                return ans;
            }else{
                needed[n] = idx;
            }
            ++idx;
        }
        ans.push_back(idx-1);
        ans.push_back(needed[target - nums[idx-1]]);
        return ans;
    }
};