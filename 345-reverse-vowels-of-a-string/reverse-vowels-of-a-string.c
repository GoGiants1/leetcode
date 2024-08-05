char* reverseVowels(char* s) {
    // Use Stack  
    // 1. push vowel in first pass 
    // 2. swap in reverse order

    int n = strlen(s);

    int pos[n];
    int cur = 0;

    for (int i = 0; i < n; ++i) {
        if (s[i] == 'a' || s[i] == 'e' || s[i] == 'i' || s[i] == 'o' || s[i] == 'u' || s[i] == 'A' || s[i] == 'E' || s[i] == 'I' || s[i] == 'O' || s[i] == 'U') {
            pos[cur] = i;
            cur++;
        }
    }
    int loop_count = cur / 2;

    for (int i = 0; i < loop_count; i++) {
        char tmp = s[pos[i]];
        s[pos[i]] = s[pos[--cur]];
        s[pos[cur]] = tmp;
    }

    return s;

}