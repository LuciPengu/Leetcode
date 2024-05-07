class Solution {
public:
    int findMaxK(vector<int>& nums) {
        int ans = -2;
        map<int, int> storage;
        for (auto x: nums){
            if (storage.count((x*-1)) > 0){
                ans = max(ans, storage[((x*-1))]);
            }
            
            storage[x] = x < 0 ? x*-1 : x;
        }
        return max(-1, ans);
    }
};