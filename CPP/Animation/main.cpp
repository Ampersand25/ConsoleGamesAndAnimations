//Animation for problem "Spiral" from Timus
//Link to the problem: http://acm.timus.ru/problem.aspx?space=1&num=1224

#include <iostream>
#include <stdlib.h>
#include <windows.h>
#include <assert.h>
#include <cmath>
#define len 10001
#define inf 0x3f3f3f3f
#define is_in(ii, jj) (ii >= 1 && ii <= N && jj >= 1 && jj <= M ? true : false)
#define conv(k) (k >= 3 ? 0 : (k + 1))

using namespace std;

int N, M;
bool a[len][len];
short b[len][len], dir[]={1, 2, 3, 4}, k;

bool is_full()
{
    for(int i = 1; i <= N; ++i)
        for(int j = 1; j <= M; ++j)
            if(!a[i][j])
                return false;
    return true;
}

void Tipar()
{
    for(int i = 1; i <= N; ++i)
    {
        for(int j = 1; j <= M; ++j)
            if(!b[i][j])
                cout << ' ';
            else cout << '*';
        cout << '\n';
    }
}

int main()
{
    cin >> N;
    assert(N >= 1);
    cin >> M;
    assert(M >= 1);
    int count = 0, i, j;
    i = j = 1;
    do{
        a[i][j] = 1;
        if(dir[k] == 1 || dir[k] == 3)
            b[i][j] = 1;
        else b[i][j] = 2;
        if(dir[k] == 1)
            if(is_in(i, j + 1) && !a[i][j + 1])
                ++j;
            else{
                k = conv(k);
                ++count;
                ++i;
            }
        else if(dir[k] == 2)
            if(is_in(i + 1, j) && !a[i + 1][j])
                ++i;
            else{
                k = conv(k);
                ++count;
                --j;
            }
        else if(dir[k] == 3)
            if(is_in(i, j - 1) && !a[i][j - 1])
                --j;
            else{
                k = conv(k);
                ++count;
                --i;
            }
        else
            if(is_in(i - 1, j) && !a[i - 1][j])
                --i;
            else{
                k = conv(k);
                ++count;
                ++j;
            }
        system("CLS");
        Tipar();
        Sleep(500);
    }while(!is_full());
    cout << "The number of the turns is equal to " << count - 1;
    return 0;
}
