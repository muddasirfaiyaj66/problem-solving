#include<bits/stdc++.h>
using namespace std;

bool validPalindrome(string s) {
    int l = 0, r = s.size()-1;

    while(l<r){
        if(s[l] != s[r]){
           int  l1=l,r1 = r-1, l2 = l+1, r2=r;

           while(l1<r1 && s[l1] == s[r1]){
               l1++;
               r1--;
           }
           while(l2<r2 && s[l2] == s[r2]){
               l2++;
               r2--;
           }
              return l1>=r1 || l2>=r2;
        }
        l++;
        r--;

    }
    return true;
        
}

int  main() {
    string s = "acv";
    cout << validPalindrome(s) << endl;
    return 0;
}

