int memo[101][101];

int dp(int i, int j) {
    if (i == 0 || j == 0) {
        return 1;
    }

    if (memo[i][j] != 0) {
        return memo[i][j];
    }

    memo[i][j] = dp(i - 1, j) + dp(i, j - 1);
    return memo[i][j];
}

int uniquePaths(int m, int n) {
    for (int i = 0; i < m; i++){
        memo[i][0] = 0;
    }
    for (int j = 0; j < n; j++){
        memo[0][j] = 0;
    }

    int result = dp(m - 1, n - 1);

    return result;
}