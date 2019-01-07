#include <iostream>
#include <iomanip>

using namespace std;

int main()
{
	int n, k, i, j, s, poz;
	cout << "Introduceti numarul de niveluri ale piramidei: ";
	cin >> n;
	k = n * 4 - 3;
	s = 1;
	cout << "\nPiramida A este:\n\n";
	for(i = 1; i <= n; i++)
	{
		poz = 1;
		cout << setw(k);
		for(j = 1; j <= s; j++)
		{
			if(poz == 1 || poz == s)
				cout << 1 << setw(4);
			else
				cout << i << setw(4);
			poz++;
		}
		cout << endl;
		k -= 4;
		s += 2;
	}
	k = 1;
	s = n * 2 - 1;
	cout << "\nPiramida B este:\n\n";
	for(i = n; i >= 1; i--)
	{
		poz = 1;
		cout << setw(k);
		for(j = 1; j <= s; j++)
		{
			if(poz == 1 || poz == s)
				cout << 1 << setw(4);
			else
				cout << i << setw(4);
			poz++;
		}
		cout << endl;
		k += 4;
		s -= 2;
	}
}
