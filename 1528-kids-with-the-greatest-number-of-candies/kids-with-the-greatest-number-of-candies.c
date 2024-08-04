/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
bool* kidsWithCandies(int* candies, int candiesSize, int extraCandies, int* returnSize) {
    *returnSize = candiesSize;

    bool* result = (bool*) malloc(*returnSize * sizeof(bool));


    int max_candy_cnt = 0;
    for (int i = 0; i < candiesSize; ++i){
        max_candy_cnt = max_candy_cnt > candies[i] ? max_candy_cnt : candies[i];
    }

    for (int i = 0; i < *returnSize; ++i){
        result[i] = candies[i] + extraCandies >= max_candy_cnt;
    }

    return result;

}