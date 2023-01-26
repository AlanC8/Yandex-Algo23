#include <bits/stdc++.h>
using namespace std;
int main(){
    // int n;
    // cin >> n;
    int arr[] = {75, 42, 5, 6};
    // for(int i = 0; i < n; i++){
    //     cin >> arr[i];
    // }
    int size = sizeof(arr) / sizeof(int);
    for(int i = 0; i < size; i++){
        for(int j = i+1; j < size; j++){
            if(arr[i] > arr[j]){
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }
    }
    int med;
    int num;
    if(size % 2 != 0){
        med = size / 2;
        num = arr[med];
    } else {
        med = size / 2;
        num = (arr[med - 1] + arr[med] )/ 2;
    }
    for(auto i : arr){
        cout << i << " ";
    }
    cout << endl;
    cout << size << " " << num  << " " << med;
    return 0;
}