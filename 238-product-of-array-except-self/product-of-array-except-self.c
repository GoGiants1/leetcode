/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* productExceptSelf(int* nums, int numsSize, int* returnSize) {
    // calc whole product of nums
    // divide itself

    // Brute force solution
    // *returnSize = numsSize;
    // int *out = calloc(*returnSize, sizeof(int));
    
    // for (int i = 0; i < *returnSize; i++){
    //     out[i] = 1;
    //     for (int j = 0; j < *returnSize; j++){
    //         if(i != j){
    //             out[i] *= nums[j];
    //         }
    //     }
    // }

    // return out;

    // Prefix array and Suffix array
    *returnSize = numsSize;
    int *out = calloc(*returnSize, sizeof(int));
    
    int prefix[numsSize];
    int suffix[numsSize];

    int n = numsSize;
    for (int i = 0; i < n; ++i){
        if (i == 0){
            prefix[i] = nums[i];
            suffix[n - 1 - i] = nums[n - 1 - i];
            continue;
        }
        prefix[i] = prefix[i - 1] * nums[i];
        suffix[n - 1 - i] = suffix[n - i] * nums[n - 1 - i];
    }

    for (int i = 0; i < n; ++i){
        if(i == 0){
            out[i] = suffix[i + 1];
        }else if (i == n - 1){
            out[i] = prefix[i - 1];
        }else{
            out[i] = prefix[i-1] * suffix[i + 1];
        }
    }
    return out;

}