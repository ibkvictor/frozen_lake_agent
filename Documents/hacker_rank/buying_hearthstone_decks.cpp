#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <limits>
using namespace std; 

int solve(vector<int>& vec, int n, int k, int res = 0, int prev = 0){
    int res_val =  - (std::numeric_limits<int>::max());
    for(auto& a: vec){
        int val;
        if(a <= n - res){
            val = solve(vec, n, k, res + a, a);
            if (val > res_val){
                res_val = val;
            }
        }
    }
    if (res_val != - (std::numeric_limits<int>::max())){
        return res_val + res;
    }
    else{
        return prev;
    }
}

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */ 
    int n, k;
    cin>>n>>k;
    vector<int> vec (k, 0);
    for(auto& a : vec){
        cin>>a;
    }
    cout<<solve(vec, n, k)<<endl;
    return 0;
}

