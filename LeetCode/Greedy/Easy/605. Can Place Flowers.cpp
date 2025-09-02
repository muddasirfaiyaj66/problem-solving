#include <bits/stdc++.h>
using namespace std;

bool canPlaceFlowers(vector<int> &flowerbed, int n){
    flowerbed.insert(flowerbed.begin(), 0);
    flowerbed.insert(flowerbed.end(), 0);

    for (int i = 1; i  < flowerbed.size()-1; i++){
        if (flowerbed[i - 1] == 0 && flowerbed[i] == 0 && flowerbed[i + 1] == 0)
        {
            flowerbed[i] = 1;
            n--;
        }
    }
    return n <= 0;
};

int main()
{
    vector<int> flowerbed = {0, 0, 1,0,0};
    int n = 2;
    cout << canPlaceFlowers(flowerbed, n) << endl;
    return 0;
}