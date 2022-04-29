#include <vector>

using namespace std;

class Solution {
public:
    static bool canPlaceFlowers(vector<int>& flowerbed, int n) {
        int max = 0;
        int size = (int)flowerbed.size();

        for (int i = 0; i < size; ++i) {
            if(flowerbed[i]==0&&(i==0||flowerbed[i-1]==0)&&(i==size-1||flowerbed[i+1]==0)) {
                flowerbed[i] = 1;
                ++max;
            }
        }
        return  n <= max;
    }
};