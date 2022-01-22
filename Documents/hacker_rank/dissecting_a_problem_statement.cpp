#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int n;
    int val;
    cin>>n;
    int max = 0;
    for (auto i =0 ; i < n; i ++){
        cin>>val;
        if(val > max){
            max = val;
        }
    }
    cout<<max;
    return 0;

}
