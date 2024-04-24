#include <cstdlib>
class Solution {
public:
    int scoreOfString(string s) {
        int score = 0;
        for(auto it = s.begin(); it != s.end() -1; ++it){
            score += std::abs(*it - *(it + 1));
        }
        return score;
    }
};