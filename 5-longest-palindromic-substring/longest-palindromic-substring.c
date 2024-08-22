#include <string.h>
#include <stdlib.h>
#include <stdbool.h>

char* longestPalindrome(char* s) {
    int n = strlen(s);
    if (n < 2) return strdup(s);

    int start = 0, max_len = 1;
    bool dp[1000][1000] = {false};

    // 길이 1인 팰린드롬 초기화
    for (int i = 0; i < n; i++) {
        dp[i][i] = true;
    }

    // 길이 2인 팰린드롬 검사
    for (int i = 0; i < n - 1; i++) {
        if (s[i] == s[i+1]) {
            dp[i][i+1] = true;
            start = i;
            max_len = 2;
        }
    }

    // 길이 3 이상인 팰린드롬 검사
    for (int len = 3; len <= n; len++) {
        for (int i = 0; i < n - len + 1; i++) {
            int j = i + len - 1;
            if (s[i] == s[j] && dp[i+1][j-1]) {
                dp[i][j] = true;
                if (len > max_len) {
                    start = i;
                    max_len = len;
                }
            }
        }
    }

    char* result = (char*)malloc((max_len + 1) * sizeof(char));
    strncpy(result, s + start, max_len);
    result[max_len] = '\0';

    return result;
}