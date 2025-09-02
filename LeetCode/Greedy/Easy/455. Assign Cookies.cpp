#include<bits/stdc++.h>
using namespace std;


int findContentChildren(vector<int>& g, vector<int>& s) {

    sort(g.begin(),g.end());
    sort(s.begin(),s.end());

    int ans =0 , i = 0;
    for (int j=0; j<s.size() ;j++){
        if(i<g.size() && g[i]<= s[j]){
            ans++;
            i++;
        } 
    }

    return ans;
}


int main(){
    vector<int> g = {1,2,3};
    vector<int> s = {1,4,8};
    cout << findContentChildren(g, s) << endl;
    return 0;
}
