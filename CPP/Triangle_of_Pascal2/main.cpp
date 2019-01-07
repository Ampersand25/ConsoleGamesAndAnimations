#include <iostream>
#include <iomanip>
#include <windows.h>
#define chr ((char)219)
#define color(c) (SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE), c))

using namespace std;

long long t[101][101];
short n, k;

void Introducere()
{
    cout << setw(58) << "TRIUNGHIUL LUI PASCAL";
    cout << "\n\n  Definitie: Triunghiul lui Pascal este un aranjament geometric al coeficientilor binomiali, ";
    cout << "numit astfel in onoarea matematicianului francez Blaise Pascal. ";
    cout << "Inaltimea si laturile triunghiului contin cifra 1, iar fiecare numar de pe o linie n reprezinta suma celor 2 numere de pe linia superioara n-1.";
    cout << "\n  Dati numarul de linii pentru Triunghiul lui Pascal: ";
}

void Legenda()
{
    color(15);
    cout << "\n  LEGENDA: \n";
    color(2);
    cout << chr << " - numarul 1 \n";
    color(3);
    cout << chr << " - numerele naturale \n";
    color(4);
    cout << chr << " - numerele triunghiulare \n";
    color(5);
    cout << chr << " - numerele tetraede \n";
    color(6);
    cout << chr << " - numerele pentatope \n";
}

void Proprietati()
{
    color(15);
    cout << "\n  Proprietati: \n";
    cout << "-Formula binomului\nFie formula: (X+Y)^n = a(0) X^n Y^0 + a(1) X^(n-1) Y^1 + a(2) X^(n-2) Y^2 + ... + a(n) Y^n X^0. ";
    cout << "Atunci coeficientii a(i) reprezinta numerele aflate pe linia n a Triunghiului lui Pascal.";
    cout << "\n-Sirul lui Fibonacci\nSuma elementelor de pe cea de a n diagonala reprezinta cel de-al n-lea element din Sirul lui Fibonacci.";
    cout << "\n-Alte proprietati\nSuma elementelor de pe a n-a linie este egala cu 2^n;\nGrupand elementele de pe diagonalele locale, se poate obtine Triunghiul lui Sierpinsky. \n";
}

int main()
{
    short n;
    color(15);
    Introducere();
    cin >> n;
    k = n + 1;
    t[1][1] = 1;
    Sleep(500);
    color(2);
    cout << '\n' << setw(k) << 1 << '\n';
    --k;
    for(short i = 2; i <= n; ++i)
    {
        for(short j = 1; j <= i; ++j)
        {
            Sleep(500);
            color(j % 15 + 1);
            t[i][j] = t[i - 1][j] + t[i - 1][j - 1];
            if(j == 1)
            {
                cout << setw(k) << t[i][1];
                --k;
            }
            else cout << setw(6) << t[i][j];
        }
        cout << '\n';
    }
    Legenda();
    Proprietati();
    return 0;
}
