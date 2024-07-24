// #include <string.h>

// char* gcdOfStrings(char* str1, char* str2) {
//     int m = strlen(str1);
//     int n = strlen(str2);
//     int max_len = m > n ? m : n;
//     int gcd_end = 0;
//     int remainder = 0;
//     // time_complexity: O(max_len)
//     for (int i = 0; i < max_len; i++){
//         // gcd 찾기 (서로 같은 부분 문자열)
//         if (i < m && i < n){
//             if (str1[i] == str2[i]){
//                 gcd_end++;
//             }
//             else{
//                 gcd_end = 0;
//                 break;
//             }
//         }else{
//             // 각 문자열에서 잘 반복되고 있는지 체크
//             if (i < m){
//                 if (str1[i % gcd_end] != str1[i]){
//                     return "";
//                 }
                
//             }

//             if (i < n){
//                 if (str2[i % gcd_end] != str2[i]){
//                     return "";
//                 }
//             }
//             remainder++;
            
//         }
//     }

//     // 찾아낸 cd 중에 
//     int gcd_len = gcd_end < remainder ? gcd_end : remainder == 0 ? gcd_end : remainder;
//     int l = gcd_end;
//     int r = remainder;
//     int div = gcd_len;
//     while (div > 0){
//         if (l % div == 0 && r % div == 0){
//             break;
//         }
//         div--;
//     }
    

//     char* gcd = calloc(div + 1, sizeof(char));
//     gcd = strncpy(gcd, str1, div);

//     return gcd;
// }

char* gcdOfStrings(char* str1, char* str2) {
    int pointer = 0;
    while (str1[pointer] != '\0' && str2[pointer] != '\0'){
        if(str1[pointer] == str2[pointer]){
            pointer++;
        }
        else{
            return "";
        }
    }
    if (str1[pointer] == '\0' && str2[pointer] == '\0'){
        return str1;
    }
    else {
        if (str1[pointer] == '\0'){
            return gcdOfStrings(str1, str2 + pointer);
        }
        else{
            return gcdOfStrings(str1 + pointer, str2);
        }
    }
}