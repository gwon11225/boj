#include <iostream>
#include <vector>

using namespace std;

int main() {
    int n, m;
    cin >> n >> m;
    int arr[n];
    vector<int> array;
    int answer = 0;

    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }
    

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            for (int k = 0; k < n; k++) {
                if (i == j || i == k || j == k) continue;
                array.push_back(arr[i] + arr[j] + arr[k]);
            }
        }
    }

    for (int i = 0; i < array.size(); i++) {
        if (array[i] > m) continue;
        if (answer < array[i]) {
            answer = array[i];
        }
    }

    cout << answer << endl;
}