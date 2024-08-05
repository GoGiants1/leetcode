char* kthDistinct(char** arr, int arrSize, int k) {

    for (int i = 0; i < arrSize; i++){
        bool is_distinct = true;
        for (int j = 0; j < arrSize; j++){
            if (i == j){
                continue;
            }

            if (strcmp(arr[i], arr[j]) == 0) {
                is_distinct = false;
                break;
            }
        }
        if (is_distinct) {
            k--;
            if (k == 0){
                return arr[i];
            }
        }
    }

    return "";
}