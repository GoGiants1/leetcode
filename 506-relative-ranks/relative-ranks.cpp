class Solution {
public:
    vector<string> findRelativeRanks(vector<int>& score) {
        int n = score.size();
        map<int, int> score_to_idx;
        vector<string> out(n);
        for(int i = 0; i < n; ++i){
            score_to_idx[score[i]] = i;
        }
        
        int rank = 1;
        for(auto rit = score_to_idx.rbegin(); rit != score_to_idx.rend(); ++rit){
            if (rank == 1){
                out[rit -> second] = "Gold Medal";
            }else if (rank == 2){
                out[rit -> second] = "Silver Medal";
            }else if (rank == 3){
                out[rit -> second] = "Bronze Medal";
            }else{
                out[rit -> second] = to_string(rank);
            }
            ++rank;
        }
        return out;
    }
};