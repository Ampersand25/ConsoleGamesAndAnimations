#include <windows.h>
#include <iostream>
#include <fstream>
#include <iomanip>
#include <vector>
#define len 10

using namespace std;

ifstream in("sweeper.txt");

vector<vector<bool> > matrix;
vector<vector<short> > v;
short n, m, l, c;
bool val, ok[len][len];

bool is_in_i(short position)
{
    return (position >= 0 && position < n);
}

bool is_in_j(short position)
{
    return (position >= 0 && position < m);
}

void Tipar()
{
    cout << setw(3);
    for(short j = 0; j < v[0].size(); ++j)
        cout << j << ' ';
    cout << '\n';
    for(short i = 0; i < v.size(); ++i)
    {
        cout << i << ' ';
        for(short j = 0; j < v[0].size(); ++j)
        {
            if(ok[i][j] && v[i][j] != -1)
            {
                SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE), v[i][j] + 7);
                cout << v[i][j];
                SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE), 15);
            }
            else if(ok[i][j] && v[i][j] == -1)
            {
                SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE), 12);
                cout << (char)254;
                SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE), 15);
            }
            else cout << (char)254;
            cout << ' ';
        }
        cout << '\n';
    }
}

void Tipar_2()
{
    cout << setw(3);
    for(short j = 0; j < v[0].size(); ++j)
        cout << j << ' ';
    cout << '\n';
    for(short i = 0; i < v.size(); ++i)
    {
        cout << i << " ";
        for(short j = 0; j < v[0].size(); ++j)
        {
            if(v[i][j] != -1)
            {
                SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE), v[i][j] + 7);
                cout << v[i][j];
                SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE), 15);
            }
            else if(v[i][j] == -1)
            {
                SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE), 12);
                cout << (char)254;
                SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE), 15);
            }
            cout << ' ';
        }
        cout << '\n';
    }
}

bool game_over()
{
    for(short i = 0; i < v.size(); ++i)
        for(short j = 0; j < v[0].size(); ++j)
            if(!ok[i][j] && v[i][j] != -1)
                return 0;
    return 1;
}

int main()
{
    SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE), 15);
    in >> n >> m;
    for(short i = 0; i < n; ++i)
    {
        vector<bool> row;
        for(short j = 0; j < m; ++j)
        {
            in >> val;
            row.push_back(val);
        }
        matrix.push_back(row);
    }
    short diri[] = {1, 0, -1, 0, 1, -1, 1, -1}, dirj[] = {0, 1, 0, -1, 1, -1, -1, 1};
    for(short i = 0; i < matrix.size(); ++i)
    {
        vector<short> row;
        for(short j = 0; j < matrix[0].size(); ++j)
        {
            short cont = 0;
            for(short k = 0; k < 8; ++k)
                if(is_in_i(i + diri[k]) && is_in_j(j + dirj[k]) && matrix[i + diri[k]][j + dirj[k]])
                    ++cont;
            row.push_back(cont);
        }
        v.push_back(row);
    }
    for(short i = 0; i < matrix.size(); ++i)
        for(short j = 0; j < matrix[0].size(); ++j)
            if(matrix[i][j])
                v[i][j] = -1;
    while(!game_over())
    {
        system("CLS");
        Tipar();
        cout << "\nEnter the index of the line: ";
        cin >> l;
        bool k = 0;
        while(!is_in_i(l))
        {
            if(!k)
                k = 1;
            cout<<"\nInvalid line!\nRe-enter the line: ";
            cin >> l;
        }
        if(k)
            cout << '\n';
        cout << "Enter the index of the column: ";
        cin >> c;
        while(!is_in_j(c))
        {
            cout << "\nInvalid column!\nRe-enter the column: ";
            cin >> c;
        }
        while(ok[l][c])
        {
            cout << "\nPosition entered before!\nRe-enter the index of the line: ";
            cin >> l;
            while(!is_in_i(l))
            {
                cout << "\nInvalid line!\nRe-enter the line: ";
                cin >> l;
            }
            cout << "Re-enter the index of the column: ";
            cin >> c;
            while(!is_in_j(c))
            {
                cout << "\nInvalid column!\nRe-enter the column: ";
                cin >> c;
            }
        }
        ok[l][c] = 1;
        system("CLS");
        if(v[l][c] == - 1)
        {
            Tipar_2();
            cout << "\nGame Over!\n";
            return 0;
        }
        Tipar();
    }
    system("CLS");
    Tipar_2();
    cout << "\nVictory!\n";
    return 0;
}
