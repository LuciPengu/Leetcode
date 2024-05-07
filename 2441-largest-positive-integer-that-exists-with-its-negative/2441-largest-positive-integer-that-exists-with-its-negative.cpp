class Solution {
public:
    int findMaxK(vector<int>& nums) {
        sort(nums.begin(), nums.end(), std::greater<>());
        int ans = -2;
        map<int, int> storage;
        for (auto x: nums){
            cout << x;
            if (storage.count((x*-1)) > 0){
                ans = max(ans, storage[((x*-1))]);
            }
            storage[x] = x;
        }
        return max(-1, ans);
    }
};