/*
Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome.

 

Example 1:

Input: s = "abccccdd"
Output: 7
Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.
Example 2:

Input: s = "a"
Output: 1
Explanation: The longest palindrome that can be built is "a", whose length is 1.
 

Constraints:

1 <= s.length <= 2000
s consists of lowercase and/or uppercase English letters only.
*/


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