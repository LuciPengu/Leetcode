class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        map<int,int> freq;
        
        for(int i = 0; i < nums.size(); i++){
            int val = target - nums[i];
            if (freq.count(val)){
                return {i, freq[val]};
            }
            freq[nums[i]] = i;
        }
        return {-1,-1};
    }
};