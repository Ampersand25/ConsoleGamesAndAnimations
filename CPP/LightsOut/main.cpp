/*
Source (inspiration):
https://codefights.com/challenge/ZvY5zvHJAuTw3BDkC

Helpful links:
https://en.wikipedia.org/wiki/Lights_Out_(game)
http://www.logicgamesonline.com/lightsout/
*/

#include <windows.h>
#include <iostream>
#include <stdlib.h>
#include <assert.h>
#include <iomanip>
#include <fstream>
#define len 5
#define car char(219)
#define fin "level.txt"
#define gray SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE), 8)
#define white SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE), 15)

using namespace std;

ifstream in(fin);

bool matrix[len][len];
short answer, t, count, diri[] = {0, 1, 0, -1}, dirj[] = {1, 0, -1, 0};

void Read()
{
    for(short i = 0; i < 5; ++i)
        for(short j = 0; j < 5; ++j)
            in >> matrix[i][j];
    in >> t;
}

void Type()
{
    cout << '\n';
    for(short i = 0; i < 5; ++i)
    {
        for(short j = 0; j < 5; ++j)
        {
            matrix[i][j] ? gray : white;
            cout << setw(3) << car << car << car << car << car << car;
        }
        cout << '\n';
        for(short j = 0; j < 5; ++j)
        {
            matrix[i][j] ? gray : white;
            cout << setw(3) << car << car << car << car << car << car;
        }
        cout << '\n';
        for(short j = 0; j < 5; ++j)
        {
            matrix[i][j] ? gray : white;
            cout << setw(3) << car << car << car << car << car << car;
        }
        cout << "\n\n";
    }
    white;
    cout << "  Target: " << t << " Moves: " << count << "\n\n";
}

bool End_Game()
{
    for(short i = 0; i < 5; ++i)
        for(short j = 0; j < 5; ++j)
            if(matrix[i][j])
                return false;
    return true;
}

void Conversion(short ii, short jj)
{
    matrix[ii][jj] = (!matrix[ii][jj] ? 1 : 0);
}

bool Is_In(short ii, short jj)
{
    return (ii >= 0 && ii < 5 && jj >= 0 && jj < 5);
}

void Action(short ii, short jj)
{
    Conversion(ii, jj);
    for(short k = 0; k < 4; ++k)
        if(Is_In(ii + diri[k], jj + dirj[k]))
            Conversion(ii + diri[k], jj + dirj[k]);
}

int main()
{
    white;
    cout << "Welcome to 5x5 Lights";
    gray;
    cout << "Out";
    white;
    cout << "!\nPress:\n1)for the instructions\n2)for the actual game\nYour choice: ";
    cin >> answer;
    while(answer != 1 && answer != 2)
    {
        cout << "Error!\nYour choice: ";
        cin >> answer;
    }
    system("CLS");
    if(answer == 1)
    {
        cout << "The game consists of a 5 by 5 grid of lights.\nWhen the game starts, a random number or a stored pattern of these lights is switched on.";
        cout << "\nLightsOut is based on a deceptively simple concept.\nPressing any of the lights will toggle it and the four adjacent lights.";
        cout << "\nThe goal is to turn out all the lights, ideally with the minimum number of moves.";
        cout << "\nFor more details, including methods of solving or the game in browser, see the attached links.";
        cout << "\nLet's proceed to the gameplay!\n";
        system("pause");
    }
    system("CLS");
    Read();
    Type();
    do{
        short l, c;
        cout << "  -line: ";
        cin >> l;
        while(l < 1 || l > 5)
        {
            cout << "   Error!\n  -line: ";
            cin >> l;
        }
        cout << "  -column: ";
        cin >> c;
        while(c < 1 || c > 5)
        {
            cout << "   Error!\n  -column: ";
            cin >> c;
        }
        Action(l - 1, c - 1);
        ++count;
        if(!(count % 20))
        {
            cout << "\n  You should maybe try another level from the list or create one.\n  If you want to give up enter 1): ";
            cin >> answer;
            if(answer == 1)
            {
                cout << "  Better luck next time! :D\n  ";
                system("pause");
                system("CLS");
                return 0;
            }
        }
        system("CLS");
        Type();
    }while(!End_Game());
    cout << "  Congratulations! You solve the puzzle in " << count << " moves!\n\n  ";
    system("pause");
    system("CLS");
    return 0;
}
