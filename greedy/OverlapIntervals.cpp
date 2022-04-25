#include <algorithm>
#include <vector>

using namespace std;
// Firstly you need to understand why use greedy strategy here: return the minimum number of...
// Then, try to define what exactly is overlapping?
// Or what you gonna to do will help you judge overlapping?
// Cos you gonna to use this in the if statement.
class Solution {
public:
    static int eraseOverlapIntervals(vector<vector<int>>& intervals) {
        //Sort the intervals, with starting index
        auto compare = [](vector<int>& a, vector<int>& b) {return a[0] < b[0];};
        sort(intervals.begin(), intervals.end(), compare);

        int total = 0;
        int size = (int)intervals.size();
        int prev = intervals[0][1];

        for (int i = 1; i < size; ++i) {
            if (intervals[i][0] < prev) {
                ++total;
                if (prev > intervals[i][1]) {
                    prev = intervals[i][1];
                }
            } else {
                prev = intervals[i][1];
            }
        }
        return total;
    }
};
