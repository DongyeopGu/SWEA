#include <cstdio>
#include <cstring>
#include <algorithm>
#include <queue>
using namespace std;

int map[100][100];
int dis[100][100];
int dx[4] = {0, 0, -1, 1};
int dy[4] = {-1, 1, 0, 0};
int n;
bool border(int x, int y) {
    return (0 <= x && x < n && 0 <= y && y < n);
}
void solv() {
    queue<pair<int, int>> q;
    q.push(make_pair(0,0));
    while (!q.empty()) {
        int x = q.front().first;
        int y = q.front().second;
        q.pop();
        for (int i=0; i<4; i++) {
            int nx = x+dx[i];
            int ny = y+dy[i];
            if (border(nx,ny)) {
                int dist = map[nx][ny] + dis[x][y];
                if (dist < dis[nx][ny]) {
                    q.push(make_pair(nx, ny));
                    dis[nx][ny] = dist;
                }
            }
        }
    }
    return;
}

int main() {
    int test_case;
    scanf("%d", &test_case);
    for (int t=1; t<=test_case; t++) {
        scanf("%d", &n);
        for (int i=0; i<n;i++) {
            for (int j=0;j<n;j++) {
                scanf("%1d", &map[i][j]);
                dis[i][j] = 9999999;
            }
        }
        dis[0][0] = 0;
        solv();
        printf("#%d %d\n", t, dis[n-1][n-1]);
    }
    return 0;
}