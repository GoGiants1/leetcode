class Solution {
public:
    bool isAnagram(string s, string t) {
        int m, n;
        m = s.size();
        n = t.size();
        
        if (m != n){
            return false;
        }

        unordered_map<char, int> cnt_1;
        unordered_map<char, int> cnt_2;


        // O(N)
        for (int i=0; i < m; ++i){
            cnt_1[s[i]] += 1;
            cnt_2[t[i]] += 1;
        }

        for (auto el: cnt_1){
            char c;
            int count;
            tie(c, count) = el;
            if (cnt_2.count(c) > 0){
                if(cnt_2[c] != count){
                    return false;
                }
            }
            else{
                return false;
            }
        }
        return true;
    }
};