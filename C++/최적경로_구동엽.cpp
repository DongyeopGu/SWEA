// //순열

#include <iostream>
#include <algorithm>

using namespace std;

struct po {
    int x, y;
};
 
int t, n;
int visit[12];
po a[12];

int main() {
    scanf("%d", &t);
    for (int test_case = 1; test_case <= t; test_case++) {
        scanf("%d", &n);
        int result = 987654321;
        scanf("%d %d", &a[0].x, &a[0].y);
        scanf("%d %d", &a[n+1].x, &a[n+1].y);
        for (int i=1;i<=n;i++) {
            scanf("%d %d", &a[i].x, &a[i].y);
            visit[i] = i;
        }
        visit[n+1] = n+1;
        do {
            int sum = 0;
            for (int i = 1; i <= n + 1; ++i) 
                sum += abs(a[visit[i]].x - a[visit[i - 1]].x) + abs(a[visit[i]].y - a[visit[i - 1]].y);
            result = min(result, sum);
        } while (next_permutation(visit+1,visit+1+n));
        printf("#%d %d\n", test_case, result);
    }
    return 0;
}

// DP
// //순열

// #include <iostream>
// #include <algorithm>

// using namespace std;

// struct po {
//     int x, y;
// };
 
// int t, n;
// int visit[12];
// po a[12];

// int main() {
//     scanf("%d", &t);
//     for (int test_case = 1; test_case <= t; test_case++) {
//         scanf("%d", &n);
//         int result = 987654321;
//         scanf("%d %d", &a[0].x, &a[0].y);
//         scanf("%d %d", &a[n+1].x, &a[n+1].y);
//         for (int i=1;i<=n;i++) {
//             scanf("%d %d", &a[i].x, &a[i].y);
//             visit[i] = i;
//         }
//         visit[n+1] = n+1;
//         do {
//             int sum = 0;
//             for (int i = 1; i <= n + 1; ++i) 
//                 sum += abs(a[visit[i]].x - a[visit[i - 1]].x) + abs(a[visit[i]].y - a[visit[i - 1]].y);
//             result = min(result, sum);
//         } while (next_permutation(visit+1,visit+1+n));
//         printf("#%d %d\n", test_case, result);
//     }
//     return 0;
// }

// DP
#include <stdio.h>

using namespace std;

int t, n;
int x[12], y[12];
int dp[1 << 12][12];

int main() {
    scanf("%d", &t);
    for (int test_case = 1; test_case <= t; test_case++) {
        scanf("%d", &n);
        n += 2;
        for (int i = 0; i < n; i++) {
            scanf("%d %d", &x[i], &y[i]);
        }
        for (int i = 0; i < (1 << n); i++) { 
            for (int j = 0; j < n; j++) { 
                dp[i][j] = -1;
            }
        }
        dp[1][0] = 0;
        for (int i=0; i < (1<<n); i++) {
            for (int j=0; j < n; j++) {
                if ((1 << j)&i) {
                    if (dp[i][j] == -1) {
                        continue;
                    }
                    for (int k = 0; k < n; k++) {
                        if (((1 << k)&i) == 0) {
                            int dx = x[j] - x[k];
                            int dy = y[j] - y[k];
                            if (dx < 0) dx = -dx;
                            if (dy < 0) dy = -dy;
                            int w = dx + dy;
                            int &upd = dp[i | (1 << k)][k];
                            if (upd == -1 || upd > dp[i][j] + w) upd = dp[i][j] + w;
                        }
                    }
                }

            }
        }

        printf("#%d %d\n", test_case, dp[(1 << n) - 1][1]);
    }
    return 0;
}