class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        map<int, int> m;
        for(int i=0; i<nums.size(); i++) {
            const int comp = target - nums[i];
            if (m.count(comp) == 1) {
                return vector<int> {i, m[comp]};
            }
            m[nums[i]] = i;
        }
        assert(false);
    }
};
