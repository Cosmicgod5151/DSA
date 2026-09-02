class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int,int> pmap;
        for(int i=0;i<nums.size();i++){
            int diff=target-nums[i];
            if(pmap.find(diff)!=pmap.end()){
                return {pmap[diff],i};
            }
            pmap.insert({nums[i],i});
        }
        return {0,0};
    }
};