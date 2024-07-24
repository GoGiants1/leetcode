class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        int m = word1.size();
        int n = word2.size();
        int max_len = max(m,n);

        vector<char> out;

        for (int i = 0; i < max_len; ++i){
            if (i < m){
                out.push_back(word1[i]);
            }
            if (i < n){
                out.push_back(word2[i]);
            }
        }
        
        string str_out(out.begin(), out.end());

        return str_out;
    }
};