#include <cstdio>
#include <vector>
using namespace std;

int main() {
    int t;
    scanf("%d", &t);
    for (int i = 1; i <= t; i++) {
        int n, m, a, b;
        scanf("%d %d", &n, &m);
        vector<vector<int>> v(501);
        bool check[501] = {0, };
        check[1] = 1;
        while (m--) {
            scanf("%d %d", &a, &b);
            v[a].push_back(b);
            v[b].push_back(a);
            if (a==1) {
                check[b] = 1;
            }
        }
        int result = v[1].size();
        for (a = 0; a < v[1].size(); a++) {
            for (b = 0; b < v[v[1][a]].size(); b++) {
                if (!check[v[v[1][a]][b]]) {
                    result++; 
                    check[v[v[1][a]][b]] = 1;
                }
            }
        }
        printf("#%d %d\n", i, result);
    }
    return 0;
}