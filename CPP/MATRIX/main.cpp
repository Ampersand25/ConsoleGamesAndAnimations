#include <iostream>
#include <stdlib.h>
#include <time.h>

int main()
{
	srand(time(NULL));
	system("color 02");
	while(true)
		std::cout << rand() % 2;
	return 0;
}
