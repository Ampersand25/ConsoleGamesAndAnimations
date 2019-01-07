#include <iostream>
#include <windows.h>
#include <time.h>
#include <string.h>

using namespace std;
short a[4][4],P1,P2,c1,c2,game;
char n[51],n1[51],n2[51],car;
bool start;
void tipar()
{
    cout<<' '<<1<<' '<<2<<' '<<3<<'\n';
    for(short i=1;i<=3;++i)
    {
        cout<<i;
        for(short j=1;j<=3;++j)
        {
            if(!a[i][j])
                cout<<' ';
            else if(1==a[i][j])
            {
                SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),c1);
                cout<<'X';
                SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),15);
            }
            else{
                SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),c2);
                cout<<'0';
                SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),15);
            }
            if(j<=2)
                cout<<'|';
        }
        cout<<'\n';
        if(i<=2)
            cout<<" -----\n";
    }
}
int main()
{
    for(short i=1;i<=3;++i)
        for(short j=1;j<=3;++j)
            a[i][j]=0;
    bool k=0;
    short ok;
    srand(time(0));
    SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),15);
    cout<<" TIC-TAC-TOE GAME\n";
    cout<<" SUMMARY: Tic-tac-toe (also known as noughts and crosses or Xs and Os ";
    cout<<"is a paper-and-pencil game for two players, X and 0, who take turns marking the spaces in a 3x3 grid. ";
    cout<<"The player who succeeds in placing three of their marks in a horizontal, vertical, or diagonal row wins the game.";
    cout<<endl<<" PRESS ENTER FOR THE GAME:";
    cin.get();
    system("CLS");
    if(!start)
    {
        cout<<"CHOOSE HOW YOU WANT TO PLAY:\n1)WITH ANOTHER PLAYER\n2)WITH THE COMPUTER\nRASPUNS: ";
        cin>>game;
        while(1!=game && 2!=game)
        {
            cout<<"OPTION UNAVAILABLE!\nTRY AGAIN: ";
            cin>>game;
        }
        system("CLS");
        if(1==game)
        {
            cout<<"PLAYER 1 (X) = ";
            cin.get();
            cin.getline(n1,51);
            cout<<"PLAYER 2 (Y) = ";
            cin.get(n2,51);
            cout<<endl<<"THE LIST OF AVAILABLE COLORS FOR THE TWO PLAYERS:\n";
            SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),1);
            cout<<"1-BLUE";
            SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),2);
            cout<<endl<<"2-GREEN";
            SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),3);
            cout<<endl<<"3-CYAN";
            SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),4);
            cout<<endl<<"4-RED";
            SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),5);
            cout<<endl<<"5-MAGENTA";
            SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),6);
            cout<<endl<<"6-BROWN";
            SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),7);
            cout<<endl<<"7-LIGHTGRAY";
            SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),8);
            cout<<endl<<"8-DARKGRAY";
            SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),9);
            cout<<endl<<"9-LIGHTBLUE";
            SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),10);
            cout<<endl<<"10-LIGHTGREEN";
            SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),11);
            cout<<endl<<"11-LIGHTCYAN";
            SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),12);
            cout<<endl<<"12-LIGHTRED";
            SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),13);
            cout<<endl<<"13-LIGHTMAGENTA";
            SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),14);
            cout<<endl<<"14-YELLOW\n";
            SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),15);
            cout<<endl<<n1<<": ";
            cin>>c1;
            while(c1<1 || c1>14)
            {
                cout<<"COLOR INEXISTENT!\n";
                cout<<n1<<": ";
                cin>>c1;
            }
            cout<<n2<<": ";
            cin>>c2;
            while(c2<1 || c2>14)
            {
                cout<<"COLOR INEXISTENT!\n";
                cout<<n2<<": ";
                cin>>c2;
            }
            while(c1==c2)
            {
                cout<<"COLOR ALREADY TAKEN!\n";
                cout<<n2<<": ";
                cin>>c2;
            }
            system("CLS");
        }
        else{
            cout<<"THE LIST OF AVAILABLE COLORS:\n";
            SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),1);
            cout<<"1-BLUE";
            SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),2);
            cout<<endl<<"2-GREEN";
            SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),3);
            cout<<endl<<"3-CYAN";
            SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),4);
            cout<<endl<<"4-RED";
            SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),5);
            cout<<endl<<"5-MAGENTA";
            SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),6);
            cout<<endl<<"6-BROWN";
            SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),7);
            cout<<endl<<"7-LIGHTGRAY";
            SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),8);
            cout<<endl<<"8-DARKGRAY";
            SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),9);
            cout<<endl<<"9-LIGHTBLUE";
            SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),10);
            cout<<endl<<"10-LIGHTGREEN";
            SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),11);
            cout<<endl<<"11-LIGHTCYAN";
            SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),12);
            cout<<endl<<"12-LIGHTRED";
            SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),13);
            cout<<endl<<"13-LIGHTMAGENTA";
            SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),14);
            cout<<endl<<"14-YELLOW\n";
            SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),15);
            cout<<endl<<"CHOOSE THE COLOR YOU WANT FROM THE LIST: ";
            cin>>c1;
            while(c1<1 || c1>14)
            {
                cout<<"COLOR INEXISTENT!\n";
                cout<<"PLAYER: ";
                cin>>c1;
            }
            c2=1+rand()%15;
            while(c1==c2)
                c2=1+rand()%15;
            cout<<"CHOOSE YOUR NICKNAME FOR THIS GAME: ";
            cin.get();
            cin.getline(n,51);
            cout<<"CHOOSE WITH WHAT DO YOU WANT TO PLAY BETWEEN X AND 0: ";
            cin>>car;
            while('0'!=car && 'X'!=toupper(car))
            {
                cout<<"OPTION INEXISTENT!\nTRY AGAIN: ";
                cin>>car;
            }
            system("CLS");
        }
    }
    if(1==game)
    {
        SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),c1);
        cout<<n1<<" = X";
        SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),c2);
        cout<<endl<<n2<<" = 0";
        cout<<"\n\n";
        SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),15);
        tipar();
        cout<<endl<<"CHOOSE WHO TO START THE GAME:\n1)";
        SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),c1);
        cout<<'X';
        SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),15);
        cout<<endl<<"2)";
        SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),c2);
        cout<<'0';
        SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),15);
        cout<<endl<<"3)";
        SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),c1);
        cout<<"RAN";
        SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),c2);
        cout<<"DOM";
        SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),15);
        cout<<'\n';
        short l,c,count,valarray;
        cin>>valarray;
        SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),15);
        while(valarray>3 || valarray<1)
        {
            cout<<"ERROR!\n";
            cin>>valarray;
        }
        if(1==valarray)
            count=1;
        else if(2==valarray)
            count=2;
        else count=rand()%2+1;
        for(short i=1;i<=9;++i)
        {
            cout<<'\n';
            if(count%2)
            {
                SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),c1);
                cout<<n1<<'\n';
            }
            else{
                SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),c2);
                cout<<n2<<'\n';
            }
            cout<<"Enter the line: ";
            cin>>l;
            while(l>3 || l<1)
            {
                cout<<"ERROR!\n";
                cout<<"Re-enter the line: ";
                cin>>l;
            }
            cout<<"Enter the column: ";
            cin>>c;
            while(c>3 || c<1)
            {
                cout<<"ERROR!\n";
                cout<<"Re-enter the column: ";
                cin>>c;
            }
            while(a[l][c])
            {
                cout<<"Position already taken!\n";
                cout<<"Re-enter the line: ";
                cin>>l;
                while(l>3 || l<1)
                {
                    cout<<"ERROR!\n";
                    cout<<"Re-enter the line: ";
                    cin>>l;
                }
                cout<<"Re-enter the column: ";
                cin>>c;
                while(c>3 || c<1)
                {
                    cout<<"ERROR!\n";
                    cout<<"Re-enter the column: ";
                    cin>>c;
                }
            }
            SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),15);
            if(count%2)
                a[l][c]=1;
            else a[l][c]=2;
            system("CLS");
            tipar();
            bool ok=1;
            for(short i=1;i<=3;++i)
                if(a[i][c]!=a[l][c])
                    ok=0;
            if(ok && 1==a[l][c])
            {
                k=1;
                ++P1;
                SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),c1);
                cout<<endl<<n1<<" WINNER!\n";
                break;
            }
            if(ok && 2==a[l][c])
            {
                k=1;
                ++P2;
                SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),c2);
                cout<<endl<<n2<<" WINNER!\n";
                break;
            }
            ok=1;
            for(short i=1;i<=3;++i)
                if(a[l][i]!=a[l][c])
                    ok=0;
            if(ok && 1==a[l][c])
            {
                k=1;
                ++P1;
                SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),c1);
                cout<<endl<<n1<<" WINNER!\n";
                break;
            }
            if(ok && 2==a[l][c])
            {
                k=1;
                ++P2;
                SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),c2);
                cout<<endl<<n2<<" WINNER!\n";
                break;
            }
            if(1==a[l][c] && a[1][1]==a[2][2] && a[2][2]==a[3][3] && a[1][1]==a[l][c])
            {
                k=1;
                ++P1;
                SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),c1);
                cout<<endl<<n1<<" WINNER!\n";
                break;
            }
            if(2==a[l][c] && a[1][1]==a[2][2] && a[2][2]==a[3][3] && a[1][1]==a[l][c])
            {
                k=1;
                ++P2;
                SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),c2);
                cout<<endl<<n2<<" WINNER!\n";
                break;
            }
            if(1==a[l][c] && a[1][3]==a[2][2] && a[2][2]==a[3][1] && a[1][3]==a[l][c])
            {
                k=1;
                ++P1;
                SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),c1);
                cout<<endl<<n1<<" WINNER!\n";
                break;
            }
            if(2==a[l][c] && a[1][3]==a[2][2] && a[2][2]==a[3][1] && a[1][3]==a[l][c])
            {
                k=1;
                ++P2;
                SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),c2);
                cout<<endl<<n2<<" WINNER!\n";
                break;
            }
            ++count;
        }
        SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),15);
        if(!k)
            cout<<"\nTIE!\n";
        cout<<"FINAL SCORE ";
        SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),c1);
        cout<<P1;
        SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),15);
        cout<<':';
        SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),c2);
        cout<<P2;
        SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),15);
        cout<<"\n\n";
        cout<<"PRESS:\n1)-FOR A NEW ROUND\n2)-FOR THE END OF THE GAME\n";
        cin>>ok;
        while(1!=ok && 2!=ok)
        {
            cout<<"OPTION INEXISTENT!\n";
            cout<<"RE-ENTER THE OPTION YOU WANT: ";
            cin>>ok;
        }
        if(1==ok)
        {
            start=1;
            main();
        }
        else{
            system("CLS");
            if(P1==P2)
                cout<<"TIE!";
            else if(P1>P2)
            {
                SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),c1);
                cout<<n1;
                SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),15);
                cout<<" WIN WITH THE OVERALL SCORE OF ";
                SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),c1);
                cout<<P1;
                SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),15);
                cout<<':';
                SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),c2);
                cout<<P2;
                SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),14);
                cout<<endl<<"CONGRATULATIONS!!!\n";
                SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),14);
                cout<<"   ((*))"<<'\n';
                cout<<"  //   \\\\"<<'\n';
                cout<<" ||     ||"<<'\n';
                cout<<"[||  ";
                SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),c1);
                cout<<'X';
                SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),14);
                cout<<"  ||]"<<'\n';
                cout<<" ||     ||"<<'\n';
                cout<<"  \\\\   //"<<'\n';
                cout<<"   || ||"<<'\n';
                cout<<"   || ||"<<'\n';
                cout<<"   || ||"<<'\n';
                cout<<"   -----"<<'\n';
                cout<<"  //   \\\\"<<'\n';
                cout<<" ---------";
            }
            else{
                SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),c2);
                cout<<n2;
                SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),15);
                cout<<" WIN WITH THE OVERALL SCORE OF ";
                SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),c2);
                cout<<P2;
                SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),15);
                cout<<':';
                SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),c1);
                cout<<P1;
                SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),14);
                cout<<endl<<"CONGRATULATIONS!!!\n";
                SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),14);
                cout<<"   ((*))"<<'\n';
                cout<<"  //   \\\\"<<'\n';
                cout<<" ||     ||"<<'\n';
                cout<<"[||  ";
                SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),c2);
                cout<<'0';
                SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),14);
                cout<<"  ||]"<<'\n';
                cout<<" ||     ||"<<'\n';
                cout<<"  \\\\   //"<<'\n';
                cout<<"   || ||"<<'\n';
                cout<<"   || ||"<<'\n';
                cout<<"   || ||"<<'\n';
                cout<<"   -----"<<'\n';
                cout<<"  //   \\\\"<<'\n';
                cout<<" ---------";
            }
            SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),15);
            cout<<'\n';
            return 0;
        }
    }
    else{
        if('X'==toupper(car))
        {
            SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),c1);
            cout<<n<<" = X";
            SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),c2);
            cout<<endl<<"COMPUTER = 0";
            cout<<"\n\n";
            SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),15);
            tipar();
            cout<<endl<<"CHOOSE WHO TO START THE GAME:\n1)";
            SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),c1);
            cout<<'X';
            SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),15);
            cout<<endl<<"2)";
            SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),c2);
            cout<<'0';
            SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),15);
            cout<<endl<<"3)";
            SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),c1);
            cout<<"RAN";
            SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),c2);
            cout<<"DOM";
            SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),15);
            cout<<'\n';
            short l,c,count,valarray;
            cin>>valarray;
            SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),15);
            while(valarray>3 || valarray<1)
            {
                cout<<"ERROR!\n";
                cin>>valarray;
            }
            if(1==valarray)
                count=1;
            else if(2==valarray)
                count=2;
            else count=rand()%2+1;
            for(short i=1;i<=9;++i)
            {
                cout<<'\n';
                if(!(count%2))
                {
                    l=rand()%3+1;
                    c=rand()%3+1;
                    while(a[l][c])
                    {
                        l=rand()%3+1;
                        c=rand()%3+1;
                    }
                }
                else
                {
                    SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),c1);
                    cout<<n<<'\n';
                    cout<<"Enter the line: ";
                    cin>>l;
                    while(l>3 || l<1)
                    {
                        cout<<"ERROR!\n";
                        cout<<"Re-enter the line: ";
                        cin>>l;
                    }
                    cout<<"Enter the column: ";
                    cin>>c;
                    while(c>3 || c<1)
                    {
                        cout<<"ERROR!\n";
                        cout<<"Re-enter the column: ";
                        cin>>c;
                    }
                    while(a[l][c])
                    {
                        cout<<"Position already taken!\n";
                        cout<<"Re-enter the line: ";
                        cin>>l;
                        while(l>3 || l<1)
                        {
                            cout<<"ERROR!\n";
                            cout<<"Re-enter the line: ";
                            cin>>l;
                        }
                        cout<<"Re-enter the column: ";
                        cin>>c;
                        while(c>3 || c<1)
                        {
                            cout<<"ERROR!\n";
                            cout<<"Re-enter the column: ";
                            cin>>c;
                        }
                    }
                }
                SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),15);
                if(count%2)
                    a[l][c]=1;
                else a[l][c]=2;
                system("CLS");
                tipar();
                bool ok=1;
                for(short i=1;i<=3;++i)
                    if(a[i][c]!=a[l][c])
                        ok=0;
                if(ok && 1==a[l][c])
                {
                    k=1;
                    ++P1;
                    SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),c1);
                    cout<<endl<<n<<" WINNER!\n";
                    break;
                }
                if(ok && 2==a[l][c])
                {
                    k=1;
                    ++P2;
                    SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),c2);
                    cout<<endl<<"COMPUTER WINNER!\n";
                    break;
                }
                ok=1;
                for(short i=1;i<=3;++i)
                    if(a[l][i]!=a[l][c])
                        ok=0;
                if(ok && 1==a[l][c])
                {
                    k=1;
                    ++P1;
                    SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),c1);
                    cout<<endl<<n<<" WINNER!\n";
                    break;
                }
                if(ok && 2==a[l][c])
                {
                    k=1;
                    ++P2;
                    SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),c2);
                    cout<<endl<<"COMPUTER WINNER!\n";
                    break;
                }
                if(1==a[l][c] && a[1][1]==a[2][2] && a[2][2]==a[3][3] && a[1][1]==a[l][c])
                {
                    k=1;
                    ++P1;
                    SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),c1);
                    cout<<endl<<n<<" WINNER!\n";
                    break;
                }
                if(2==a[l][c] && a[1][1]==a[2][2] && a[2][2]==a[3][3] && a[1][1]==a[l][c])
                {
                    k=1;
                    ++P2;
                    SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),c2);
                    cout<<endl<<"COMPUTER WINNER!\n";
                    break;
                }
                if(1==a[l][c] && a[1][3]==a[2][2] && a[2][2]==a[3][1] && a[1][3]==a[l][c])
                {
                    k=1;
                    ++P1;
                    SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),c1);
                    cout<<endl<<n<<" WINNER!\n";
                    break;
                }
                if(2==a[l][c] && a[1][3]==a[2][2] && a[2][2]==a[3][1] && a[1][3]==a[l][c])
                {
                    k=1;
                    ++P2;
                    SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),c2);
                    cout<<endl<<"COMPUTER WINNER!\n";
                    break;
                }
                ++count;
            }
            SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),15);
            if(!k)
                cout<<"\nTIE!\n";
            cout<<"FINAL SCORE ";
            SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),c1);
            cout<<P1;
            SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),15);
            cout<<':';
            SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),c2);
            cout<<P2;
            SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),15);
            cout<<"\n\n";
            cout<<"PRESS:\n1)-FOR A NEW ROUND\n2)-FOR THE END OF THE GAME\n";
            cin>>ok;
            while(1!=ok && 2!=ok)
            {
                cout<<"OPTION INEXISTENT!\n";
                cout<<"RE-ENTER THE OPTION YOU WANT: ";
                cin>>ok;
            }
            if(1==ok)
            {
                start=1;
                main();
            }
            else{
                system("CLS");
                if(P1==P2)
                    cout<<"TIE!";
                else if(P1>P2)
                {
                    SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),15);
                    cout<<"YOU WIN WITH THE OVERALL SCORE OF ";
                    SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),c1);
                    cout<<P1;
                    SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),15);
                    cout<<':';
                    SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),c2);
                    cout<<P2;
                    SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),14);
                    cout<<"\nCONGRATULATIONS!!!\n";
                    SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),14);
                    cout<<"   ((*))"<<'\n';
                    cout<<"  //   \\\\"<<'\n';
                    cout<<" ||     ||"<<'\n';
                    cout<<"[||  ";
                    SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),c1);
                    cout<<'X';
                    SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),14);
                    cout<<"  ||]"<<'\n';
                    cout<<" ||     ||"<<'\n';
                    cout<<"  \\\\   //"<<'\n';
                    cout<<"   || ||"<<'\n';
                    cout<<"   || ||"<<'\n';
                    cout<<"   || ||"<<'\n';
                    cout<<"   -----"<<'\n';
                    cout<<"  //   \\\\"<<'\n';
                    cout<<" ---------";
                }
                else{
                    SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),15);
                    cout<<"YOU LOSE WITH THE OVERALL SCORE OF ";
                    SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),c1);
                    cout<<P1;
                    SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),15);
                    cout<<':';
                    SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),c2);
                    cout<<P2;
                    SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),15);
                    cout<<"\nBETTER LUCK NEXT TIME!\n";
                }
                SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),15);
                cout<<'\n';
                return 0;
            }
        }
        else{
            if(!start)
            {
                short aux=c2;
                c2=c1;
                c1=aux;
            }
            SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),c1);
            cout<<"COMPUTER = X";
            SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),c2);
            cout<<endl<<n<<" = 0";
            cout<<"\n\n";
            SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),15);
            tipar();
            cout<<endl<<"CHOOSE WHO TO START THE GAME:\n1)";
            SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),c1);
            cout<<'X';
            SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),15);
            cout<<endl<<"2)";
            SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),c2);
            cout<<'0';
            SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),15);
            cout<<endl<<"3)";
            SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),c1);
            cout<<"RAN";
            SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),c2);
            cout<<"DOM";
            SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),15);
            cout<<'\n';
            short l,c,count,valarray;
            cin>>valarray;
            SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),15);
            while(valarray>3 || valarray<1)
            {
                cout<<"ERROR!\n";
                cin>>valarray;
            }
            if(1==valarray)
                count=1;
            else if(2==valarray)
                count=2;
            else count=rand()%2+1;
            for(short i=1;i<=9;++i)
            {
                cout<<'\n';
                if(count%2)
                {
                    l=rand()%3+1;
                    c=rand()%3+1;
                    while(a[l][c])
                    {
                        l=rand()%3+1;
                        c=rand()%3+1;
                    }
                }
                else
                {
                    SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),c2);
                    cout<<n<<'\n';
                    cout<<"Enter the line: ";
                    cin>>l;
                    while(l>3 || l<1)
                    {
                        cout<<"ERROR!\n";
                        cout<<"Re-enter the line: ";
                        cin>>l;
                    }
                    cout<<"Enter the column: ";
                    cin>>c;
                    while(c>3 || c<1)
                    {
                        cout<<"ERROR!\n";
                        cout<<"Re-enter the column: ";
                        cin>>c;
                    }
                    while(a[l][c])
                    {
                        cout<<"Position already taken!\n";
                        cout<<"Re-enter the line: ";
                        cin>>l;
                        while(l>3 || l<1)
                        {
                            cout<<"ERROR!\n";
                            cout<<"Re-enter the line: ";
                            cin>>l;
                        }
                        cout<<"Re-enter the column: ";
                        cin>>c;
                        while(c>3 || c<1)
                        {
                            cout<<"ERROR!\n";
                            cout<<"Re-enter the column: ";
                            cin>>c;
                        }
                    }
                }
                SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),15);
                if(count%2)
                    a[l][c]=1;
                else a[l][c]=2;
                system("CLS");
                tipar();
                bool ok=1;
                for(short i=1;i<=3;++i)
                    if(a[i][c]!=a[l][c])
                        ok=0;
                if(ok && 2==a[l][c])
                {
                    k=1;
                    ++P2;
                    SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),c2);
                    cout<<endl<<n<<" WINNER!\n";
                    break;
                }
                if(ok && 1==a[l][c])
                {
                    k=1;
                    ++P1;
                    SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),c1);
                    cout<<endl<<"COMPUTER WINNER!\n";
                    break;
                }
                ok=1;
                for(short i=1;i<=3;++i)
                    if(a[l][i]!=a[l][c])
                        ok=0;
                if(ok && 2==a[l][c])
                {
                    k=1;
                    ++P2;
                    SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),c2);
                    cout<<endl<<n<<" WINNER!\n";
                    break;
                }
                if(ok && 1==a[l][c])
                {
                    k=1;
                    ++P1;
                    SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),c1);
                    cout<<endl<<"COMPUTER WINNER!\n";
                    break;
                }
                if(2==a[l][c] && a[1][1]==a[2][2] && a[2][2]==a[3][3] && a[1][1]==a[l][c])
                {
                    k=1;
                    ++P2;
                    SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),c2);
                    cout<<endl<<n<<" WINNER!\n";
                    break;
                }
                if(1==a[l][c] && a[1][1]==a[2][2] && a[2][2]==a[3][3] && a[1][1]==a[l][c])
                {
                    k=1;
                    ++P1;
                    SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),c1);
                    cout<<endl<<"COMPUTER WINNER!\n";
                    break;
                }
                if(2==a[l][c] && a[1][3]==a[2][2] && a[2][2]==a[3][1] && a[1][3]==a[l][c])
                {
                    k=1;
                    ++P2;
                    SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),c2);
                    cout<<endl<<n<<" WINNER!\n";
                    break;
                }
                if(1==a[l][c] && a[1][3]==a[2][2] && a[2][2]==a[3][1] && a[1][3]==a[l][c])
                {
                    k=1;
                    ++P1;
                    SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),c1);
                    cout<<endl<<"COMPUTER WINNER!\n";
                    break;
                }
                ++count;
            }
            SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),15);
            if(!k)
                cout<<"\nTIE!\n";
            cout<<"FINAL SCORE ";
            SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),c1);
            cout<<P1;
            SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),15);
            cout<<':';
            SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),c2);
            cout<<P2;
            SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),15);
            cout<<"\n\n";
            cout<<"PRESS:\n1)-FOR A NEW ROUND\n2)-FOR THE END OF THE GAME\n";
            cin>>ok;
            while(1!=ok && 2!=ok)
            {
                cout<<"OPTION INEXISTENT!\n";
                cout<<"RE-ENTER THE OPTION YOU WANT: ";
                cin>>ok;
            }
            if(1==ok)
            {
                start=1;
                main();
            }
            else{
                system("CLS");
                if(P1==P2)
                    cout<<"TIE!";
                else if(P1<P2)
                {
                    SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),15);
                    cout<<"YOU WIN WITH THE OVERALL SCORE OF ";
                    SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),c2);
                    cout<<P2;
                    SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),15);
                    cout<<':';
                    SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),c1);
                    cout<<P1;
                    SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),14);
                    cout<<"\nCONGRATULATIONS!!!\n";
                    SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),14);
                    cout<<"   ((*))"<<'\n';
                    cout<<"  //   \\\\"<<'\n';
                    cout<<" ||     ||"<<'\n';
                    cout<<"[||  ";
                    SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),c2);
                    cout<<'0';
                    SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),14);
                    cout<<"  ||]"<<'\n';
                    cout<<" ||     ||"<<'\n';
                    cout<<"  \\\\   //"<<'\n';
                    cout<<"   || ||"<<'\n';
                    cout<<"   || ||"<<'\n';
                    cout<<"   || ||"<<'\n';
                    cout<<"   -----"<<'\n';
                    cout<<"  //   \\\\"<<'\n';
                    cout<<" ---------";
                }
                else{
                    SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),15);
                    cout<<"YOU LOSE WITH THE OVERALL SCORE OF ";
                    SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),c2);
                    cout<<P2;
                    SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),15);
                    cout<<':';
                    SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),c1);
                    cout<<P1;
                    SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),15);
                    cout<<"\nBETTER LUCK NEXT TIME!\n";
                }
                SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),15);
                cout<<'\n';
                return 0;
            }
        }
    }
}
