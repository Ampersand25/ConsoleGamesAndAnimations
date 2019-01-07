#include <time.h>
#include <iomanip>
#include <iostream>
#include <stdlib.h>
#include <string.h>
#include <windows.h>

using namespace std;

char a[] = "abcdefghijklmnopqrstuvwxyz";

int main()
{
    system("CLS");
    SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE), 10);
    srand(time(0));
    short nr = rand() % strlen(a) + 1, k = 1;
    char l;
    cout << "Think about a letter from a to z and write it: ";
    cin >> l;
    l = tolower(l);
    while(!strchr(a, l))
    {
        cout << "The symbol entered is not a valid one!\nRe-enter another one: ";
        cin >> l;
        l = tolower(l);
        ++k;
        if(k == 3)
        {
            cout << "You entered wrong characters too many times!" << '\n';
            return 0;
        }
    }
    short count = 0;
    while(l != a[nr])
    {
        cout << (l > a[nr] ? "Too right!" : "Too left!");
        cout << endl << "Try again: ";
        cin >> l;
        l = tolower(l);
        while(!strchr(a, l))
        {
            cout << "The symbol entered is not a valid one!\nRe-enter another one: ";
            cin >> l;
            l = tolower(l);
            ++k;
            if(k == 3)
            {
                cout << "You entered wrong characters too many times!" << '\n';
                return 0;
            }
        }
        ++count;
    }
    system("CLS");
    cout << "Congratulations you guessed the letter " << a[nr] << " of " << count + 1 << " attempts!" << '\n';
    short t;
    cout << "Press\n1)for a new round\n2)for the end of the game\nAnswer: ";
    cin >> t;
    while(t != 1 && t != 2)
    {
        cout << "Option unavailable!\nRe-enter one of the options above: ";
        cin >> t;
    }
    if(t == 1)
        main();
    return 0;
}
