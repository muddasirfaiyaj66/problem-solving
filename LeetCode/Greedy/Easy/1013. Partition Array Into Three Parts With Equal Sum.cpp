/*

Given an array of integers arr, return true if we can partition the array into three non-empty parts with equal sums.

Formally, we can partition the array if we can find indexes i + 1 < j with (arr[0] + arr[1] + ... + arr[i] == arr[i + 1] + arr[i + 2] + ... + arr[j - 1] == arr[j] + arr[j + 1] + ... + arr[arr.length - 1])



Example 1:

Input: arr = [0,2,1,-6,6,-7,9,1,2,0,1]
Output: true
Explanation: 0 + 2 + 1 = -6 + 6 - 7 + 9 + 1 = 2 + 0 + 1
Example 2:

Input: arr = [0,2,1,-6,6,7,9,-1,2,0,1]
Output: false
Example 3:

Input: arr = [3,3,6,5,-2,2,5,1,-9,4]
Output: true
Explanation: 3 + 3 = 6 = 5 - 2 + 2 + 5 + 1 - 9 + 4


Constraints:

3 <= arr.length <= 5 * 104
-104 <= arr[i] <= 104
*/

#include <bits/stdc++.h>
using namespace std;

bool canThreePartsEqualSum(vector<int> &arr)
{
    int total = 0;
    for (int i : arr)
        total += i;

    if (total % 3 != 0)
        return false;

    int target = total / 3;
    int currentSum = 0;
    int firstPartEnd = -1, secondPartEnd = -1;

    
    for (int i = 0; i < arr.size() - 2; i++){ 
        currentSum += arr[i];
        if (currentSum == target){
            firstPartEnd = i;
            break;
        }
    }

    if (firstPartEnd == -1)
        return false;

    
    currentSum = 0;
    for (int i = firstPartEnd + 1; i < arr.size() - 1; i++){ 
        currentSum += arr[i];
        if (currentSum == target){
            secondPartEnd = i;
            break;
        }
    }

    if (secondPartEnd == -1)
        return false;

   
    currentSum = 0;
    for (int i = secondPartEnd + 1; i < arr.size(); i++)
    {
        currentSum += arr[i];
    }

    return currentSum == target;
}

int main()
{
    vector<int> arr = {0, 2, 1, -6, 6, -7, 9, 1, 2, 0, 1};
    cout << canThreePartsEqualSum(arr) << endl; // Output: 1 (true)

    arr = {0, 2, 1, -6, 6, 7, 9, -1, 2, 0, 1};
    cout << canThreePartsEqualSum(arr) << endl; // Output: 0 (false)

    arr = {-7, 57, -76, 5, 51, -57, 27, 83, 68, 39, -38, 43, -79, 42, -79, 72, -58, -29, -34, 23, 20, -67, -67, 74, 10, -90, -91, 41, 22, -12, -75, -3, 51, 13, 9, 58, 72, -3, 48, -28, 78, 15, 13, 22, -68, 62, 33, -18, 21, -2, 56, 41, 27, -33, -35, -36, -6, -73, -9, -45, -16, 4, 51, -54, -92, 79, -92, -12, -9, 39, 1, -60, 78, 16, -77, -45, 26, -43, 44, -21, -27, 74, -68, -58, 22, 52, 100, 37, 48, 99, 98, -34, 36, 25, -85, 83, 99, -64, -37, 20, 0, 13, 85, 18, 98, -91, 86, -94, -92, -42, -82, 89, 67, -13, 43, 11, 75, 67, -38, -79, -3, -24, 83, -1, 74, -93, 26, -69, 92, 40, -32, -89, -100, -36, 80, 9, 92, 79, -83, 90, -8, -77, 1, -60, 100, 63, 87, -51, -33, 17, 24, -73, -81, -86, 52, 59, 10, -84, -71, -12, 24, -53, -14, -44, -48, -91, -57, -82, -5, 48, -56, -92, 83, -64, -17, -46, 65, -15, 87, -61, -29, 79, -53, -81, -58, 70, 70, -12, -71, 68, -57, -44, -18, -94, -84, 7, -51, 18, 44, 96, 24, 8, 61, 36, -83, -93, 38, 82, 25, 4, 37, 93, -5, 24, -9, -31, 15, -73, -91, -36, 41, 56, -17, 3, -94, -26, 96, 5, -21, -20, 60, -53, 26, 2, -97, 41, -72, -29, -83, 32, 35, -29, 82, -38, -15, 81, -10, 50, 22, 26, 30, -31, 74, -74, 47, 66, 53, 35, -58, -68, 47, -21, 78, 12, -88, 1, 12, 53, 94, 1, -43, -36, 67, 6, -89, 44, -86, -22, 48, -12, 72, -90, -7, -92, 30, -17};
    cout << canThreePartsEqualSum(arr) << endl; // Output: 1 (true)
}