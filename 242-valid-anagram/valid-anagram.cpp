class Solution {
public:
    bool isAnagram(string s, string t) {
        // check char freq!
        int m = s.size();
        int n = t.size();
        if (n != m) {
            return false;
        }
        // map<char, int> mp; bottle neck 지점 -> 그냥 맵은 search가 O(logn)
        // 따라서 unorderd_map이나 set을 써야함.
        unordered_map<char, int> mp; // O(1)로 원소 접근 가능.
        
        // O(m)
        for (int i = 0; i < m; ++i){
            ++mp[s[i]];
            --mp[t[i]];
        }
        // O(k), k is number of keys in each map
        for (auto a: mp){
            if (a.second != 0){
                return false;
            }
        }
        return true;
    }
};