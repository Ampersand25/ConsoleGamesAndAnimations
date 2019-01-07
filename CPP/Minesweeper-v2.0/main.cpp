#include <windows.h>
#include <iostream>
#include <iomanip>
#include <time.h>
#include <vector>

using namespace std;

vector<vector<bool> > matrix;
vector<vector<short> > v;
short n, m, op, l, c;
bool ok[10][10];

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
    for(short j = 0; j < m; ++j)
        cout << j << ' ';
    cout << '\n';
    for(short i = 0; i < n; ++i)
    {
        cout << i << ' ';
        for(short j = 0; j < m; ++j)
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
    for(short j = 0; j < m; ++j)
        cout << j << ' ';
    cout << '\n';
    for(short i = 0; i < n; ++i)
    {
        cout << i << " ";
        for(short j = 0; j < m; ++j)
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
    for(short i = 0; i < n; ++i)
        for(short j = 0; j < m; ++j)
            if(!ok[i][j] && v[i][j] != -1)
                return 0;
    return 1;
}

int main()
{
    SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),15);
    cout << "Choose: \n1)if you want the size of the matrix to be determined MANUALLY\nOR\n2)if you want the size of matrix to be determined RANDOMLY";
    cout << "\nYour choice is: ";
    cin >> op;
    while(op != 1 && op != 2)
    {
        cout << "Option unavailable!\nPlease re-enter your choice: ";
        cin >> op;
    }
    if(op == 1)
    {
        system("CLS");
        cout << "Enter the number of lines: ";
        cin >> n;
        while(n <= 0 || n > 9)
        {
            cout << "For a smooth experience choose a number between 1 and 10: ";
            cin >> n;
        }
        cout << "Enter the number of columns: ";
        cin >> m;
        while(m <= 0 || m > 9)
        {
            cout << "For a smooth experience choose a number between 1 and 10: ";
            cin >> m;
        }
    }
    else{
        srand(time(NULL));
        n = rand() % 8 + 3;
        m = rand() % 8 + 3;
    }
    for(short i = 0; i < n; ++i)
    {
        vector<bool> row;
        for(short j = 0; j < m; ++j)
            row.push_back(rand() % 2);
        matrix.push_back(row);
    }
    for(short i = 0; i < n; ++i)
    {
        for(short j = 0; j < m; ++j)
            cout << matrix[i][j] << ' ';
        cout << '\n';
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
            cout << "\nInvalid line!\nRe-enter the line: ";
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
        if(v[l][c] == -1)
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
