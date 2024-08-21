
int dp(int i, int j, int **memo) {
    if (i == 0 || j == 0) {
        return 1;
    }

    if (memo[i][j] != 0) {
        return memo[i][j];
    }

    memo[i][j] = dp(i - 1, j, memo) + dp(i, j - 1, memo);
    return memo[i][j];
}

int uniquePaths(int m, int n) {
    int **memo = (int **)malloc(m * sizeof(int *));
    for (int i = 0; i < m; i++) {
        memo[i] = (int *)calloc(n, sizeof(int));
    }

    int result = dp(m - 1, n - 1, memo);

    // 메모리 해제
    for (int i = 0; i < m; i++) {
        free(memo[i]);
    }
    free(memo);

    return result;
}