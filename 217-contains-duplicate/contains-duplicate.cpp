class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        std::map<int, int> cnt;
        for (int a: nums){
            if (cnt.count(a) > 0){
                return true;
            }
            ++cnt[a];
        }
        
        return false;
    }
};