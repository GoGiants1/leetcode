char* reverseVowels(char* s) {
    // Use Stack  
    // 1. push vowel in first pass 
    // 2. swap in reverse order

    int n = strlen(s);

    char vowels[n];
    int pos[n];
    int cur = 0;

    for (int i = 0; i < n; ++i) {
        if (s[i] == 'a' || s[i] == 'e' || s[i] == 'i' || s[i] == 'o' || s[i] == 'u' || s[i] == 'A' || s[i] == 'E' || s[i] == 'I' || s[i] == 'O' || s[i] == 'U') {
            vowels[cur] = s[i];
            pos[cur] = i;
            cur++;
        }
    }
    int loop_count = cur;

    for (int i = 0; i < loop_count; i++) {
        s[pos[i]] = vowels[--cur];
    }

    return s;

}