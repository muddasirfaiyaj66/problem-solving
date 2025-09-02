#include<bits/stdc++.h>
using namespace std;
vector<int> diStringMatch(string s) {
    vector<int> ans(s.size()+1);
    int l =0, r=s.size(), idx=0;

    for(int i=0; i<s.size(); i++){
        if(s[i]=='I') ans[idx++]=l++;
        else ans[idx++]=r--;
    }
    if(s[s.size()-1] == 'I') ans[idx]=l;
    else ans[idx]=r;

    return ans;
        
}
int main(){
    string s = "IDID";
    vector<int> result = diStringMatch(s);
    for(int i : result) {
        cout << i << " ";
    }
    return 0;
}