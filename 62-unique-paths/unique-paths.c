int uniquePaths(int m, int n) {
    int grid[m][n];

    for(int i = 0; i < m; ++i){
        for (int j = 0; j < n; ++j){
            grid[i][j] = 0;
        }
    }
    grid[0][0] = 1;

    // The test cases are generated so that the answer will be less than or equal to 2 * 10^9 = 2 * (2^10)^3 = 2^31. -> int32 보장

    for (int i = 0; i < m; ++i){
        for (int j = 0; j < n; ++j){
            if (i > 0){
                grid[i][j] += grid[i-1][j];
            }
            if (j > 0){
                grid[i][j] += grid[i][j-1];
            }
        }
    }

    return grid[m-1][n-1];
}