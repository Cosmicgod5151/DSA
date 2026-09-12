class Solution {
public:
    int maxArea(vector<int>& height) {
        int n=height.size();
        int maxw=0;
        int res=0;
        int l=0,r=n-1;
        while(l<r){
            int wid=r-l;
            int len=min(height[l],height[r]);
            maxw=wid*len;
            res=max(maxw,res);
            if(height[l]<height[r]){
                l++;
            }
            else{
                r--;
            }

        }
        return res;

        
    }
};