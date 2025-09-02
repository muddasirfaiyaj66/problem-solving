#include <bits/stdc++.h>
using namespace std;
class Solution
{
public:
    int longestPalindrome(string s)
    {
        int n = s.length(), res = 0;
        unordered_map<char, int> freq;
        for (auto c : s)
            freq[c]++;

        bool isOdd = false;

        for (auto [c, fr] : freq)
        {

            if (fr % 2 == 0)
                res += fr;
            else
            {
                res += fr - 1;
                isOdd = true;
            }
        }
        return (isOdd) ? res + 1 : res;
    }
};

int main()
{
    Solution s;
    cout << s.longestPalindrome("abccccdd") << endl;
    return 0;
}