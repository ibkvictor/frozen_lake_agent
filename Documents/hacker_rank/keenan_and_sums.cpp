#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */ 
    int n, m;
    cin>>m>>n;
    vector<int> vect (n);
    for(int i = 0; i < n; i++){
        cin>>vect[i];
    }
    sort(vect.begin(), vect.end());
    for(auto& a: vect){
        m += a;
        if (m < 0){
            m = 0;
        }
    }
    cout<<m;
    return 0;
}

