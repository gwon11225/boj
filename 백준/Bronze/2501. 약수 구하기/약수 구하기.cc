#include <iostream>

using namespace std;

int main() {
    int n, k;
    int count = 0;
    cin >> n >> k;
    
    for (int i = 1; i <= n; i++) {
        if (n % i == 0) {
            count ++;
            if (count == k) {
                cout << i << endl;
                return 0;
            }
        }
    }
    cout << 0 << endl;
    return 0;
}