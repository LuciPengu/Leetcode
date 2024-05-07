class Solution {
public:
    int findMaxK(vector<int>& nums) {
        int ans = -1;
        map<int, int> storage;
        for (auto x: nums){
            ans = max(ans, storage[((x*-1))]);
            
            storage[x] = x < 0 ? x*-1 : x;
        }
        return ans == 0 ? -1 : ans;
    }
};