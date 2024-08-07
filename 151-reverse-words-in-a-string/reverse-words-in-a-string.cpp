class Solution {
public:
    string reverseWords(string s) {
        vector<string> words;
        
        int cur = 0;
        int n = s.size();
        while(cur < n) {
            string word = "";
            while(cur < n && s[cur] != ' '){
                word.push_back(s[cur]);
                cur++;
            }
            if (word.size() > 0){
                words.push_back(word);
            }
            cur++;

        }
        int word_cnt = words.size();
        string out;
        for (int i = word_cnt - 1; i >= 0; --i){
            out += words[i];
            
            if (i > 0){
                out += ' ';
            }
        }

        return out;
    }
};