#include <iostream>
#include <climits>
#include <stdlib.h>
#include <windows.h>
#define sleep Sleep(5)

int main()
{
    for(int i = 1; i <= INT_MAX; ++i)
    {
        std::cout << char(254);
        sleep;
        system("color 01");
        sleep;
        system("color 02");
        sleep;
        system("color 03");
        sleep;
        system("color 04");
        sleep;
        system("color 05");
        sleep;
        system("color 06");
        sleep;
        system("color 07");
        sleep;
        system("color 08");
        sleep;
        system("color 09");
        sleep;
        system("color 0A");
        sleep;
        system("color 0B");
        sleep;
        system("color 0C");
        sleep;
        system("color 0D");
        sleep;
        system("color 0E");
        sleep;
        system("color 0F");
    }
    return 0;
}
