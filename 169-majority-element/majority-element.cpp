class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int cand=nums[0];
        int c=0;
        for(int i=0;i<nums.size();i++){
            if(c==0){
                cand=nums[i];
            }
            c+=(cand==nums[i]) ? 1:-1;
        }
        return cand;
        
    }
};