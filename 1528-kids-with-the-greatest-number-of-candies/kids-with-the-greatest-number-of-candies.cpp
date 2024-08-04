class Solution {
public:
    vector<bool> kidsWithCandies(vector<int>& candies, int extraCandies) {
        int n = candies.size();
        vector<bool> result(n,false);

        // find the greatest number
        int greatest_candy_cnt = 0;
        for (int c :candies){
            greatest_candy_cnt = max(greatest_candy_cnt, c);
        }

    
        for (int i=0; i < n; i++){
            if (greatest_candy_cnt <= candies[i] + extraCandies){
                result[i]=true;
            }
        }

        return result;
    }
};