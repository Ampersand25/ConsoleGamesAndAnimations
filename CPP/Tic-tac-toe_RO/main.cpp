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
    cout<<" JOCUL X SI 0\n";
    cout<<" PREZENTARE: X si O (engleza tic-tac-toe) este un joc pentru doi jucatori, X respectiv 0, ";
    cout<<"care marcheaza pe rand cate o casuta dintr-un tabel cu 3 linii si 3 coloane. ";
    cout<<"Jucatorul care reuseste primul sa marcheze 3 casute adiacente pe orizontala, verticala sau diagonala castiga jocul.";
    cout<<endl<<" PENTRU A TRECE LA JOCUL PROPRIU-ZIS APASATI ENTER:";
    cin.get();
    system("CLS");
    if(!start)
    {
        cout<<"ALEGETI CUM DORITI SA JUCATI ACEST JOC:\n1)CU UN ALT JUCATOR\n2)CU CALCULATORUL\nRASPUNS: ";
        cin>>game;
        while(1!=game && 2!=game)
        {
            cout<<"OPTIUNE INDISPONIBILA!\nREINCERCATI: ";
            cin>>game;
        }
        system("CLS");
        if(1==game)
        {
            cout<<"JUCATORUL 1 (X) = ";
            cin.get();
            cin.getline(n1,51);
            cout<<"JUCATORUL 2 (Y) = ";
            cin.get(n2,51);
            cout<<endl<<"LISTA DE CULORI DISPONIBILE PENTRU CEI DOI JUCATORI:\n";
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
                cout<<"CULOARE INEXISTENTA!\n";
                cout<<n1<<": ";
                cin>>c1;
            }
            cout<<n2<<": ";
            cin>>c2;
            while(c2<1 || c2>14)
            {
                cout<<"CULOARE INEXISTENTA!\n";
                cout<<n2<<": ";
                cin>>c2;
            }
            while(c1==c2)
            {
                cout<<"CULOARE DEJA LUATA!\n";
                cout<<n2<<": ";
                cin>>c2;
            }
            system("CLS");
        }
        else{
            cout<<"LISTA DE CULORI DISPONIBILE:\n";
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
            cout<<endl<<"SELECTATI CULOAREA DORITA DIN LISTA DE MAI SUS: ";
            cin>>c1;
            while(c1<1 || c1>14)
            {
                cout<<"CULOARE INEXISTENTA!\n";
                cout<<"JUCATOR: ";
                cin>>c1;
            }
            c2=1+rand()%15;
            while(c1==c2)
                c2=1+rand()%15;
            cout<<"INTRODUCETI NUMELE PE CARE DORITI SA IL AVETI IN JOC: ";
            cin.get();
            cin.getline(n,51);
            cout<<"ALEGETI CU CE DORITI SA JUCATI DINTRE X SI 0: ";
            cin>>car;
            while('0'!=car && 'X'!=toupper(car))
            {
                cout<<"OPTIUNE INEXISTENTA!\nINCERCATI DIN NOU: ";
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
        cout<<endl<<"ALEGETI CINE SA INCEAPA JOCUL:\n1)";
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
            cout<<"EROARE!\n";
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
            cout<<"Introduceti linia: ";
            cin>>l;
            while(l>3 || l<1)
            {
                cout<<"EROARE!\n";
                cout<<"Reintroduceti linia: ";
                cin>>l;
            }
            cout<<"Introduceti coloana: ";
            cin>>c;
            while(c>3 || c<1)
            {
                cout<<"EROARE!\n";
                cout<<"Reintroduceti coloana: ";
                cin>>c;
            }
            while(a[l][c])
            {
                cout<<"Pozitie ocupata!\n";
                cout<<"Reintroduceti linia: ";
                cin>>l;
                while(l>3 || l<1)
                {
                    cout<<"EROARE!\n";
                    cout<<"Reintroduceti linia: ";
                    cin>>l;
                }
                cout<<"Reintroduceti coloana: ";
                cin>>c;
                while(c>3 || c<1)
                {
                    cout<<"EROARE!\n";
                    cout<<"Reintroduceti coloana: ";
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
                cout<<endl<<n1<<" CASTIGATOR!\n";
                break;
            }
            if(ok && 2==a[l][c])
            {
                k=1;
                ++P2;
                SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),c2);
                cout<<endl<<n2<<" CASTIGATOR!\n";
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
                cout<<endl<<n1<<" CASTIGATOR!\n";
                break;
            }
            if(ok && 2==a[l][c])
            {
                k=1;
                ++P2;
                SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),c2);
                cout<<endl<<n2<<" CASTIGATOR!\n";
                break;
            }
            if(1==a[l][c] && a[1][1]==a[2][2] && a[2][2]==a[3][3] && a[1][1]==a[l][c])
            {
                k=1;
                ++P1;
                SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),c1);
                cout<<endl<<n1<<" CASTIGATOR!\n";
                break;
            }
            if(2==a[l][c] && a[1][1]==a[2][2] && a[2][2]==a[3][3] && a[1][1]==a[l][c])
            {
                k=1;
                ++P2;
                SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),c2);
                cout<<endl<<n2<<" CASTIGATOR!\n";
                break;
            }
            if(1==a[l][c] && a[1][3]==a[2][2] && a[2][2]==a[3][1] && a[1][3]==a[l][c])
            {
                k=1;
                ++P1;
                SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),c1);
                cout<<endl<<n1<<" CASTIGATOR!\n";
                break;
            }
            if(2==a[l][c] && a[1][3]==a[2][2] && a[2][2]==a[3][1] && a[1][3]==a[l][c])
            {
                k=1;
                ++P2;
                SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),c2);
                cout<<endl<<n2<<" CASTIGATOR!\n";
                break;
            }
            ++count;
        }
        SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),15);
        if(!k)
            cout<<"\nEGALITATE!\n";
        cout<<"SCOR TOTAL ";
        SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),c1);
        cout<<P1;
        SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),15);
        cout<<':';
        SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),c2);
        cout<<P2;
        SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),15);
        cout<<"\n\n";
        cout<<"APASATI:\n1)-PENTRU O NOUA RUNDA\n2)-PENTRU A INCHEIA JOCUL\n";
        cin>>ok;
        while(1!=ok && 2!=ok)
        {
            cout<<"OPTIUNE INEXISTENTA!\n";
            cout<<"REINTRODUCETI OPTIUNEA DORITA: ";
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
                cout<<"EGALITATE!";
            else if(P1>P2)
            {
                SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),c1);
                cout<<n1;
                SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),15);
                cout<<" CASTIGA CU SCORUL GENERAL DE ";
                SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),c1);
                cout<<P1;
                SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),15);
                cout<<':';
                SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),c2);
                cout<<P2;
                SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),14);
                cout<<endl<<"FELICITARI!!!\n";
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
                cout<<" CASTIGA CU SCORUL GENERAL DE ";
                SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),c2);
                cout<<P2;
                SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),15);
                cout<<':';
                SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),c1);
                cout<<P1;
                SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),14);
                cout<<endl<<"FELICITARI!!!\n";
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
            cout<<endl<<"ALEGETI CINE SA INCEAPA JOCUL:\n1)";
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
                cout<<"EROARE!\n";
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
                    cout<<"Introduceti linia: ";
                    cin>>l;
                    while(l>3 || l<1)
                    {
                        cout<<"EROARE!\n";
                        cout<<"Reintroduceti linia: ";
                        cin>>l;
                    }
                    cout<<"Introduceti coloana: ";
                    cin>>c;
                    while(c>3 || c<1)
                    {
                        cout<<"EROARE!\n";
                        cout<<"Reintroduceti coloana: ";
                        cin>>c;
                    }
                    while(a[l][c])
                    {
                        cout<<"Pozitie ocupata!\n";
                        cout<<"Reintroduceti linia: ";
                        cin>>l;
                        while(l>3 || l<1)
                        {
                            cout<<"EROARE!\n";
                            cout<<"Reintroduceti linia: ";
                            cin>>l;
                        }
                        cout<<"Reintroduceti coloana: ";
                        cin>>c;
                        while(c>3 || c<1)
                        {
                            cout<<"EROARE!\n";
                            cout<<"Reintroduceti coloana: ";
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
                    cout<<endl<<n<<" CASTIGATOR!\n";
                    break;
                }
                if(ok && 2==a[l][c])
                {
                    k=1;
                    ++P2;
                    SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),c2);
                    cout<<endl<<"COMPUTER CASTIGATOR!\n";
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
                    cout<<endl<<n<<" CASTIGATOR!\n";
                    break;
                }
                if(ok && 2==a[l][c])
                {
                    k=1;
                    ++P2;
                    SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),c2);
                    cout<<endl<<"COMPUTER CASTIGATOR!\n";
                    break;
                }
                if(1==a[l][c] && a[1][1]==a[2][2] && a[2][2]==a[3][3] && a[1][1]==a[l][c])
                {
                    k=1;
                    ++P1;
                    SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),c1);
                    cout<<endl<<n<<" CASTIGATOR!\n";
                    break;
                }
                if(2==a[l][c] && a[1][1]==a[2][2] && a[2][2]==a[3][3] && a[1][1]==a[l][c])
                {
                    k=1;
                    ++P2;
                    SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),c2);
                    cout<<endl<<"COMPUTER CASTIGATOR!\n";
                    break;
                }
                if(1==a[l][c] && a[1][3]==a[2][2] && a[2][2]==a[3][1] && a[1][3]==a[l][c])
                {
                    k=1;
                    ++P1;
                    SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),c1);
                    cout<<endl<<n<<" CASTIGATOR!\n";
                    break;
                }
                if(2==a[l][c] && a[1][3]==a[2][2] && a[2][2]==a[3][1] && a[1][3]==a[l][c])
                {
                    k=1;
                    ++P2;
                    SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),c2);
                    cout<<endl<<"COMPUTER CASTIGATOR!\n";
                    break;
                }
                ++count;
            }
            SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),15);
            if(!k)
                cout<<"\nEGALITATE!\n";
            cout<<"SCOR TOTAL ";
            SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),c1);
            cout<<P1;
            SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),15);
            cout<<':';
            SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),c2);
            cout<<P2;
            SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),15);
            cout<<"\n\n";
            cout<<"APASATI:\n1)-PENTRU O NOUA RUNDA\n2)-PENTRU A INCHEIA JOCUL\n";
            cin>>ok;
            while(1!=ok && 2!=ok)
            {
                cout<<"OPTIUNE INEXISTENRA!\n";
                cout<<"REINTRODUCETI OPTIUNEA DORITA: ";
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
                    cout<<"EGALITATE!";
                else if(P1>P2)
                {
                    SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),15);
                    cout<<"ATI CASTIGAT CU SCORUL GENERAL DE ";
                    SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),c1);
                    cout<<P1;
                    SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),15);
                    cout<<':';
                    SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),c2);
                    cout<<P2;
                    SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),14);
                    cout<<"\nFELICITARI!!!\n";
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
                    cout<<"ATI PIERDUT CU SCORUL GENERAL DE ";
                    SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),c1);
                    cout<<P1;
                    SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),15);
                    cout<<':';
                    SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),c2);
                    cout<<P2;
                    SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),15);
                    cout<<"\nMULT SUCCES DATA URMATOARE!\n";
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
            cout<<endl<<"ALEGETI CINE SA INCEAPA JOCUL:\n1)";
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
                cout<<"EROARE!\n";
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
                    cout<<"Introduceti linia: ";
                    cin>>l;
                    while(l>3 || l<1)
                    {
                        cout<<"EROARE!\n";
                        cout<<"Reintroduceti linia: ";
                        cin>>l;
                    }
                    cout<<"Introduceti coloana: ";
                    cin>>c;
                    while(c>3 || c<1)
                    {
                        cout<<"EROARE!\n";
                        cout<<"Reintroduceti coloana: ";
                        cin>>c;
                    }
                    while(a[l][c])
                    {
                        cout<<"Pozitie ocupata!\n";
                        cout<<"Reintroduceti linia: ";
                        cin>>l;
                        while(l>3 || l<1)
                        {
                            cout<<"EROARE!\n";
                            cout<<"Reintroduceti linia: ";
                            cin>>l;
                        }
                        cout<<"Reintroduceti coloana: ";
                        cin>>c;
                        while(c>3 || c<1)
                        {
                            cout<<"EROARE!\n";
                            cout<<"Reintroduceti coloana: ";
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
                    cout<<endl<<n<<" CASTIGATOR!\n";
                    break;
                }
                if(ok && 1==a[l][c])
                {
                    k=1;
                    ++P1;
                    SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),c1);
                    cout<<endl<<"COMPUTER CASTIGATOR!\n";
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
                    cout<<endl<<n<<" CASTIGATOR!\n";
                    break;
                }
                if(ok && 1==a[l][c])
                {
                    k=1;
                    ++P1;
                    SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),c1);
                    cout<<endl<<"COMPUTER CASTIGATOR!\n";
                    break;
                }
                if(2==a[l][c] && a[1][1]==a[2][2] && a[2][2]==a[3][3] && a[1][1]==a[l][c])
                {
                    k=1;
                    ++P2;
                    SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),c2);
                    cout<<endl<<n<<" CASTIGATOR!\n";
                    break;
                }
                if(1==a[l][c] && a[1][1]==a[2][2] && a[2][2]==a[3][3] && a[1][1]==a[l][c])
                {
                    k=1;
                    ++P1;
                    SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),c1);
                    cout<<endl<<"COMPUTER CASTIGATOR!\n";
                    break;
                }
                if(2==a[l][c] && a[1][3]==a[2][2] && a[2][2]==a[3][1] && a[1][3]==a[l][c])
                {
                    k=1;
                    ++P2;
                    SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),c2);
                    cout<<endl<<n<<" CASTIGATOR!\n";
                    break;
                }
                if(1==a[l][c] && a[1][3]==a[2][2] && a[2][2]==a[3][1] && a[1][3]==a[l][c])
                {
                    k=1;
                    ++P1;
                    SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),c1);
                    cout<<endl<<"COMPUTER CASTIGATOR!\n";
                    break;
                }
                ++count;
            }
            SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),15);
            if(!k)
                cout<<"\nEGALITATE!\n";
            cout<<"SCOR TOTAL ";
            SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),c1);
            cout<<P1;
            SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),15);
            cout<<':';
            SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),c2);
            cout<<P2;
            SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),15);
            cout<<"\n\n";
            cout<<"APASATI:\n1)-PENTRU O NOUA RUNDA\n2)-PENTRU A INCHEIA JOCUL\n";
            cin>>ok;
            while(1!=ok && 2!=ok)
            {
                cout<<"OPTIUNE INEXISTENRA!\n";
                cout<<"REINTRODUCETI OPTIUNEA DORITA: ";
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
                    cout<<"EGALITATE!";
                else if(P1<P2)
                {
                    SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),15);
                    cout<<"ATI CASTIGAT CU SCORUL GENERAL DE ";
                    SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),c2);
                    cout<<P2;
                    SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),15);
                    cout<<':';
                    SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),c1);
                    cout<<P1;
                    SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),14);
                    cout<<"\nFELICITARI!!!\n";
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
                    cout<<"ATI PIERDUT CU SCORUL GENERAL DE ";
                    SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),c2);
                    cout<<P2;
                    SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),15);
                    cout<<':';
                    SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),c1);
                    cout<<P1;
                    SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),15);
                    cout<<"\nMULT SUCCES DATA URMATOARE!\n";
                }
                SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),15);
                cout<<'\n';
                return 0;
            }
        }
    }
}
