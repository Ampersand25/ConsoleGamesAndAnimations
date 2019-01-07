#include <iostream>
#include <stdlib.h>
#include <windows.h>
#include <iomanip>
#include <time.h>

using namespace std;

int main()
{
    system("CLS");
    SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE), 10);
    srand(time(NULL));
    short nr = rand() % 100 + 1, n, k = 1;
    cout << "Think about a number from 1 to 100 and write it: ";
    cin >> n;
    while(n < 1 || n > 100)
    {
        cout << "The number entered is not in the range of [1,100]!\nRe-enter another number: ";
        cin >> n;
        ++k;
        if(k == 3)
        {
            cout << "You entered wrong numbers too many times!" << '\n';
            return 0;
        }
    }
    short count = 0;
    while(n != nr)
    {
        cout << (n > nr ? "Too much!" : "Too little!");
        cout << endl << "Try again: ";
        cin >> n;
        while(n < 1 || n > 100)
        {
            cout << "The number entered is not in the range of [1,100]!\nRe-enter another number: ";
            cin >> n;
            ++k;
            if(k == 3)
            {
                cout << "You entered wrong numbers too many times!" << '\n';
                return 0;
            }
        }
        ++count;
    }
    system("CLS");
    cout << "Congratulations you guessed the number " << nr << " of " << count + 1 << " attempts!" << '\n';
    short a;
    cout << "Press\n1)for a new round\n2)for the end of the game\nAnswer: ";
    cin >> a;
    while(a != 1 && a != 2)
    {
        cout << "Option unavailable!\nRe-enter one of the options above: ";
        cin >> a;
    }
    if(a == 1)
        main();
    return 0;
}
