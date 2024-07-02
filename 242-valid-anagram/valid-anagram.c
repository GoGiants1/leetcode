bool isAnagram(char* s, char* t) {
    int s_len = strlen(s);
    int t_len = strlen(t);

    if (s_len != t_len) return false;
    
    int s_cnt[26] = {0};
    int t_cnt[26] = {0};

    for (int i = 0; i < s_len; ++i){ 
        s_cnt[s[i] - 'a'] += 1;
        t_cnt[t[i] - 'a'] += 1;
    }

    for (int j = 0; j < 26; ++j){
        if (s_cnt[j]!= t_cnt[j]){
            return false;
        }
    }
    return true;
}