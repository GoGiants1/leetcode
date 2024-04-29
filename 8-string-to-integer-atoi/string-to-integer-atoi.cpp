#include <limits.h>
class Solution {
public:
    int myAtoi(string s) {
        unordered_set<char> ints;
        for (int i = 0; i < 10; ++i){
            ints.insert(i + '0');
        }
        vector<int> digits;
        int sign = 1;
        int non_digit_cnt = 0;
        for (auto c: s){
            if (c == ' ') {
                if (digits.empty() && non_digit_cnt == 0){
                    continue;
                }else{
                    break;
                }
            }

            if (ints.count(c) == 0) {

                if (!digits.empty()){ // after digits
                    break;
                }

                // before digits
                if (c == '+' || c == '-'){ // buffer one time
                    if (c == '-'){
                        sign = -1;
                    }
                    if (non_digit_cnt > 0){
                        break;
                    }
                    ++non_digit_cnt;
                    continue;
                }

                break;
            }

            digits.push_back(c - '0');
        }
        int acc = 0;        
        for (auto it = digits.begin(); it != digits.end(); ++it){
            int curr = *it;
            if (acc > INT_MAX / 10 || (acc == INT_MAX / 10 && INT_MAX - (INT_MAX / 10 * 10) < curr)) {
                acc = INT_MAX;
                break;
            }
            if (acc < INT_MIN / 10 || (acc == INT_MIN / 10 && -(INT_MIN - (INT_MIN / 10 * 10)) < curr)) {
                acc = INT_MIN;
                break;
            }

            int new_acc = 10 * acc + curr * sign;

            acc = new_acc;
        }

        return acc;
    }
};