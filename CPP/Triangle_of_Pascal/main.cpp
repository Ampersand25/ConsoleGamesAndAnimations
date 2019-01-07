#include <iostream>
#include <iomanip>
#include <windows.h>
#define color(k) (SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE), k))

using namespace std;

long long t[101][101];
short n;

int main()
{
    color(15);
    cout << "Dati numarul de linii pentru Triunghiul lui Pascal: ";
    cin >> n;
    t[1][1] = 1;
    Sleep(500);
    color(2);
    cout << endl << setw(8) << 1 << '\n';
    for(short i = 2; i <= n; ++i)
    {
        for(short j = 1; j <= i; ++j)
        {
            Sleep(500);
            color(j % 15 + 1);
            t[i][j] = t[i - 1][j] + t[i - 1][j - 1];
            cout << setw(8) << t[i][j];
        }
        cout << '\n';
    }
    color(15);
    return 0;
}
