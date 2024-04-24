class Solution {
public:
    bool isAnagram(string s, string t) {
        // check char freq!
        int m = s.size();
        int n = t.size();
        if (n != m) {
            return false;
        }
        map<char, int> sm;
        map<char, int> tm;

        // O(m)
        for (int i = 0; i < m; ++i){
            ++sm[s[i]];
            ++tm[t[i]];
        }
        // O(k), k is number of keys in each map
        for (auto a: sm){
            if (a.second != tm[a.first]){
                return false;
            }
        }
        return true;
    }
};