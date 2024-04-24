class Solution {
public:
    bool isAnagram(string s, string t) {
        // check char freq!
        int m = s.size();
        int n = t.size();
        if (n != m) {
            return false;
        }
        map<char, int> mp;

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