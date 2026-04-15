class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        if(nums.size()==0)
        return 0;
        int temp=1;
        sort(nums.begin(), nums.end());
        for(int i=1;i<nums.size();i++)
        {
            if(nums[i]==nums[i-1])
           {
            return true;
           }
        }return false;
    }
};