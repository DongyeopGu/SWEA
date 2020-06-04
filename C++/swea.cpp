#include <stdio.h>
#include <algorithm>
#include <string.h>
#include <string>

using namespace std;

int change, result;
char arr[6];
string str;
bool visit[1000000][11];

void sol(int cnt) {
    if (cnt == change) {
        result = max(result, stoi(str));
        return;
    }

    for (int i = 0; i < str.size(); i++) {
        for (int j = i; j < str.size(); j++) {
            if (i==j) { continue; }
            swap(str[i], str[j]);
            if (visit[stoi(str)][cnt+1] == false) {
                visit[stoi(str)][cnt+1] = true;
                sol(cnt + 1);
            }
            swap(str[i], str[j]);

        }
    }
}

int main() {
    int t;
    scanf("%d", &t);
    for (int test_case = 1; test_case <= t; test_case++) {
        scanf("%s", arr);
        str = arr;
        scanf("%d", &change);
        result = 0;
        memset(visit, false, sizeof(visit));
        sol(0);
        printf("#%d %d\n", test_case, result);
    }
    return 0;
}