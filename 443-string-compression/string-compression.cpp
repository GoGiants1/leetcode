class Solution {
public:

    void append(vector<char>& chrs, int &curr, const char c, int cnt){
        chrs[curr++] = c;
        if (cnt > 1){
            string int_s = to_string(cnt);
            for (char int_c: int_s){
                chrs[curr++] = int_c;
            }
        }
    }

    int compress(vector<char>& chars) {
        int curr = 0;
        int group_start = 0;
        int consecutive_cnt = 0;
        int n = chars.size();
        for (int i = 0; i < n; i++){
            if (chars[group_start] == chars[i]){
                consecutive_cnt++;
                // cout << chars[i] << ": " << consecutive_cnt << endl;
            }else{
                append(chars, curr, chars[i - 1], consecutive_cnt);
                consecutive_cnt = 1;
                group_start = i;
            }
        }

        if (consecutive_cnt > 0){
            append(chars, curr, chars[n - 1], consecutive_cnt);
        }

        return curr;
    }
};