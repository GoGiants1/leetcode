#include <string.h>
#include <stdlib.h>
#include <stdbool.h>

#define MAX_LEN 1000

int memo[MAX_LEN][MAX_LEN];
char* s;
int start, maxLen;

int expandAroundCenter(int left, int right) {
    while (left >= 0 && right < strlen(s) && s[left] == s[right]) {
        left--;
        right++;
    }
    return right - left - 1;
}

void updateLongestPalindrome(int newStart, int newLen) {
    if (newLen > maxLen) {
        start = newStart;
        maxLen = newLen;
    }
}

int dp(int i, int j) {
    if (i >= j) return 1;
    if (memo[i][j] != -1) return memo[i][j];
    
    if (s[i] == s[j] && dp(i+1, j-1)) {
        updateLongestPalindrome(i, j-i+1);
        return memo[i][j] = 1;
    }
    
    dp(i+1, j);
    dp(i, j-1);
    
    return memo[i][j] = 0;
}

char* longestPalindrome(char* str) {
    s = str;
    int n = strlen(s);
    if (n < 2) return strdup(s);
    
    start = 0;
    maxLen = 1;
    
    memset(memo, -1, sizeof(memo));
    
    dp(0, n-1);
    
    for (int i = 0; i < n; i++) {
        int len1 = expandAroundCenter(i, i);
        updateLongestPalindrome(i - len1/2, len1);
        
        int len2 = expandAroundCenter(i, i+1);
        updateLongestPalindrome(i - len2/2 + 1, len2);
    }
    
    char* result = (char*)malloc((maxLen + 1) * sizeof(char));
    strncpy(result, s + start, maxLen);
    result[maxLen] = '\0';
    
    return result;
}