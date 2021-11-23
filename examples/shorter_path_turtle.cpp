#include <bits/stdc++.h>

using namespace std;

int main() {
    int n, x, y;
    cin >> n >> x >> y;

    int ans = abs(x - y);
    int ans2 = x < y ? x + n - y : y + n - x;

    cout << min(ans, ans2) << endl;
    return 0;
}