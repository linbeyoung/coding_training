#include <iostream>
#include "Circle.h"
using namespace std;

class Solution {
public:
    int findPeakElement(std::vector<int> &nums) {
        int left = 0, right = nums.size() - 1;
        while (left < right) {
            int lmid = (left + right) / 2;
            int rmid = lmid + 1;  // 整数里加一位即可
            if (nums[lmid] <= nums[rmid]) left = lmid + 1;
            else right = rmid - 1;
        }
        return right;
    }
};
