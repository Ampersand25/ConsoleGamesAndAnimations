#include <cstdio>
#include <windows.h>

int main()
{
    int i, n = 200;
    for(i = 1; i <= n; ++i)
    {
        SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE), i);
        printf("Hello World!\n");
    }
    return 0;
}
