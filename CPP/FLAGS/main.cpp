/*SetConsoleTextAttribute colors:
0   BLACK
1   BLUE
2   GREEN
3   CYAN
4   RED
5   MAGENTA
6   BROWN
7   LIGHTGRAY
8   DARKGRAY
9   LIGHTBLUE
10  LIGHTGREEN
11  LIGHTCYAN
12  LIGHTRED
13  LIGHTMAGENTA
14  YELLOW
15  WHITE
*/
#include <iostream>
#include <windows.h>
#include <iomanip>

using namespace std;

int main()
{
    SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),15);
    cout<<setw(62)<<"LISTA STATELOR DIN EUROPA: "<<'\n';
    cout<<endl<<"1) Anglia: \n";
    for(int i=1;i<=6;++i)
    {
        if(i==3 || i==4)
            SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),12);
        else SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),15);
        for(int j=1;j<=21;++j)
        {
            if(j==11 || j==12 || j==10)
                SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),12);
            else if(j!=11 && j!=12 && i!=4 && i!=3 && j!=10)
                SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),15);
            cout<<(char)219;
        }
        cout<<'\n';
    }
    SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),15);
    cout<<endl<<"2) Armenia: \n";
    for(int i=1;i<=6;++i)
    {
        if(i==1 || i==2)
            SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),4);
        else if(i==3 || i==4)
            SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),1);
        else SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),6);
        for(int j=1;j<=21;++j)
            cout<<(char)219;
        cout<<'\n';
    }
    SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),15);
    cout<<endl<<"3) Azerbaidjan: \n";
    for(int i=1;i<=6;++i)
    {
        if(i==1 || i==2)
            SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),11);
        else if(i==3 || i==4)
            SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),12);
        else SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),10);
        for(int j=1;j<=21;++j)
            cout<<(char)219;
        cout<<'\n';
    }
    SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),15);
    cout<<endl<<"4) Austria: \n";
    for(int i=1;i<=6;++i)
    {
        if(i==1 || i==2 || i==5 || i==6)
            SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),12);
        else SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),15);
        for(int j=1;j<=21;++j)
            cout<<(char)219;
        cout<<'\n';
    }
    SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),15);
    cout<<endl<<"5) Belarus: \n";
    for(int i=1;i<=6;++i)
    {
        if(i==1 || i==2 || i==3 || i==4)
            SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),4);
        else SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),2);
        for(int j=1;j<=21;++j)
            cout<<(char)219;
        cout<<'\n';
    }
    SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),15);
    cout<<endl<<"6) Bulgaria: \n";
    for(int i=1;i<=6;++i)
    {
        if(i==1 || i==2)
            SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),15);
        else if(i==3 || i==4)
            SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),10);
        else SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),12);
        for(int j=1;j<=21;++j)
            cout<<(char)219;
        cout<<'\n';
    }
    SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),15);
    cout<<endl<<"7) Cipru: \n";
    for(int i=1;i<=6;++i)
    {
        SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),15);
        for(int j=1;j<=21;++j)
            cout<<(char)219;
        cout<<'\n';
    }
    SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),15);
    cout<<endl<<"8) Croatia: \n";
    for(int i=1;i<=6;++i)
    {
        if(i==1 || i==2)
            SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),12);
        else if(i==3 || i==4)
            SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),15);
        else SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),9);
        for(int j=1;j<=21;++j)
            cout<<(char)219;
        cout<<'\n';
    }
    SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),15);
    cout<<endl<<"9) Danemarca: \n";
    for(int i=1;i<=6;++i)
    {
        if(i==1 || i==2 || i==5 || i==6)
            SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),12);
        else SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),15);
        for(int j=1;j<=21;++j)
        {
            if(j==7 || j==8 || j==6)
                SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),15);
            else if(j!=7 && j!=8 && j!=6 && i!=3 && i!=4)
                SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),12);
            cout<<(char)219;
        }
        cout<<'\n';
    }
    SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),15);
    cout<<endl<<"10) Elvetia: \n";
    for(int i=1;i<=6;++i)
    {
        for(int j=1;j<=21;++j)
        {
            if((i==3 || i==4) && (j>=6 && j<=15))
                SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),15);
            else if((i==2 || i==5) && (j>=9 && j<=12))
                SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),15);
            else SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),12);
            cout<<(char)219;
        }
        cout<<'\n';
    }
    SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),15);
    cout<<endl<<"11) Finlanda: \n";
    for(int i=1;i<=6;++i)
    {
        if(i==1 || i==2 || i==5 || i==6)
            SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),15);
        else SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),1);
        for(int j=1;j<=21;++j)
        {
            if(j==7 || j==8 || j==6)
                SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),1);
            else if(j!=7 && j!=8 && j!=6 && i!=3 && i!=4)
                SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),15);
            cout<<(char)219;
        }
        cout<<'\n';
    }
    SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),15);
    cout<<endl<<"12) Franta: \n";
    for(int i=1;i<=6;++i)
    {
        for(int j=1;j<=21;++j)
        {
            if(j>=1 && j<=7)
                SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),1);
            else if(j>=8 && j<15)
                SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),15);
            else SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),12);
            cout<<(char)219;
        }
        cout<<'\n';
    }
    SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),15);
    cout<<endl<<"13) Grecia: \n";
    for(int i=1;i<=5;++i)
    {
        if(i==3)
            SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),15);
        else SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),9);
        for(int j=1;j<=21;++j)
        {
            if(j>=1 && j<=8)
            {
                if(j==4 || j==5)
                    SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),15);
                else if(i==3)
                    SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),15);
                else SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),9);
            }
            else
                if(i==1 || i==3 || i==5)
                    SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),9);
                else SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),15);
            cout<<(char)219;
        }
        cout<<'\n';
    }
    for(int i=4;i<=5;++i)
    {
        if(i==5)
            SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),9);
        else SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),15);
        for(int j=1;j<=21;++j)
            cout<<(char)219;
        cout<<'\n';
    }
    SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),15);
    cout<<endl<<"14) Insulele Feroe: \n";
    for(int i=1;i<=6;++i)
    {
        if(i==1 || i==2 || i==5 || i==6)
            SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),15);
        else SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),12);
        for(int j=1;j<=21;++j)
        {
            if(j==7 || j==8 || j==6)
                SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),12);
            else if(j!=7 && j!=8 && j!=6 && i!=3 && i!=4)
                SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),15);
            cout<<(char)219;
        }
        cout<<'\n';
    }
    SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),15);
    cout<<endl<<"15) Islanda: \n";
    for(int i=1;i<=6;++i)
    {
        if(i==1 || i==2 || i==5 || i==6)
            SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),9);
        else SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),12);
        for(int j=1;j<=21;++j)
        {
            if(j==7 || j==8 || j==6)
                SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),12);
            else if(j!=7 && j!=8 && j!=6 && i!=3 && i!=4)
                SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),9);
            cout<<(char)219;
        }
        cout<<'\n';
    }
    SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),15);
    cout<<endl<<"16) Italia: \n";
    for(int i=1;i<=6;++i)
    {
        for(int j=1;j<=21;++j)
        {
            if(j>=1 && j<=7)
                SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),10);
            else if(j>=8 && j<15)
                SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),15);
            else SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),12);
            cout<<(char)219;
        }
        cout<<'\n';
    }
    SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),15);
    cout<<endl<<"17) Kazahstan: \n";
    for(int i=1;i<=6;++i)
    {
        SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),11);
        for(int j=1;j<=21;++j)
            cout<<(char)219;
        cout<<'\n';
    }
    SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),15);
    cout<<endl<<"18) Lituania: \n";
    for(int i=1;i<=6;++i)
    {
        if(i==1 || i==2)
            SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),14);
        else if(i==3 || i==4)
            SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),2);
        else SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),4);
        for(int j=1;j<=21;++j)
            cout<<(char)219;
        cout<<'\n';
    }
    SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),15);
    cout<<endl<<"19) Letonia: \n";
    for(int i=1;i<=6;++i)
    {
        if(i==1 || i==2 || i==5 || i==6)
            SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),4);
        else SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),15);
        for(int j=1;j<=21;++j)
            cout<<(char)219;
        cout<<'\n';
    }
    SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),15);
    cout<<endl<<"20) Liechtenstein: \n";
    for(int i=1;i<=6;++i)
    {
        if(i>=1 && i<=3)
            SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),1);
        else SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),4);
        for(int j=1;j<=21;++j)
            cout<<(char)219;
        cout<<'\n';
    }
    SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),15);
    cout<<endl<<"21) Luxemburg: \n";
    for(int i=1;i<=6;++i)
    {
        if(i==1 || i==2)
            SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),12);
        else if(i==3 || i==4)
            SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),15);
        else SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),11);
        for(int j=1;j<=21;++j)
            cout<<(char)219;
        cout<<'\n';
    }
    SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),15);
    cout<<endl<<"22) Monaco: \n";
    for(int i=1;i<=6;++i)
    {
        if(i==1 || i==2 || i==3)
            SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),12);
        else SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),15);
        for(int j=1;j<=21;++j)
            cout<<(char)219;
        cout<<'\n';
    }
    SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),15);
    cout<<endl<<"23) Madeira: \n";
    for(int i=1;i<=6;++i)
    {
        for(int j=1;j<=21;++j)
        {
            if(j>=1 && j<=7)
                SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),9);
            else if(j>=8 && j<15)
                SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),14);
            else SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),9);
            cout<<(char)219;
        }
        cout<<'\n';
    }
    SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),15);
    cout<<endl<<"24) Malta: \n";
    for(int i=1;i<=6;++i)
    {
        for(int j=1;j<=21;++j)
        {
            if(j<=10)
                SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),15);
            else SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),12);
            cout<<(char)219;
        }
        cout<<'\n';
    }
    SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),15);
    cout<<endl<<"25) Muntenegru: \n";
    for(int i=1;i<=6;++i)
    {
        SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),12);
        for(int j=1;j<=21;++j)
        {
            if(i==1 || j==1 || i==6 || j==21 || j==20 || j==2)
                SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),14);
            else SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),12);
            cout<<(char)219;
        }
        cout<<'\n';
    }
    SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),15);
    cout<<endl<<"26) Finlanda: \n";
    for(int i=1;i<=6;++i)
    {
        if(i==1 || i==2 || i==5 || i==6)
            SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),12);
        else SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),1);
        for(int j=1;j<=21;++j)
        {
            if(j==7 || j==8 || j==6)
                SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),1);
            else if(j!=7 && j!=8 && j!=6 && i!=3 && i!=4)
                SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),12);
            cout<<(char)219;
        }
        cout<<'\n';
    }
    SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),15);
    cout<<endl<<"27) Olanda: \n";
    for(int i=1;i<=6;++i)
    {
        if(i==1 || i==2)
            SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),4);
        else if(i==3 || i==4)
            SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),15);
        else SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),1);
        for(int j=1;j<=21;++j)
            cout<<(char)219;
        cout<<'\n';
    }
    SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),15);
    cout<<endl<<"28) Osetia de Sud: \n";
    for(int i=1;i<=6;++i)
    {
        if(i==1 || i==2)
            SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),15);
        else if(i==3 || i==4)
            SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),12);
        else SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),14);
        for(int j=1;j<=21;++j)
            cout<<(char)219;
        cout<<'\n';
    }
    SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),15);
    cout<<endl<<"29) Polonia: \n";
    for(int i=1;i<=6;++i)
    {
        if(i==1 || i==2 || i==3)
            SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),15);
        else SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),12);
        for(int j=1;j<=21;++j)
            cout<<(char)219;
        cout<<'\n';
    }
    SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),15);
    cout<<endl<<"30) Portugalia: \n";
    for(int i=1;i<=6;++i)
    {
        for(int j=1;j<=21;++j)
        {
            if(j<=8)
                SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),2);
            else SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),12);
            cout<<(char)219;
        }
        cout<<'\n';
    }
    SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),15);
    cout<<endl<<"31) Romania: \n";
    for(int i=1;i<=6;++i)
    {
        for(int j=1;j<=21;++j)
        {
            if(j>=1 && j<=7)
                SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),1);
            else if(j>=8 && j<15)
                SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),14);
            else SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),12);
            cout<<(char)219;
        }
        cout<<'\n';
    }
    SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),15);
    cout<<endl<<"32) Republica Moldoveneasca Nistreana: \n";
    for(int i=1;i<=6;++i)
    {
        if(i==1 || i==2 || i==5 || i==6)
            SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),12);
        else SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),3);
        for(int j=1;j<=21;++j)
            cout<<(char)219;
        cout<<'\n';
    }
    SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),15);
    cout<<endl<<"33) Rusia: \n";
    for(int i=1;i<=6;++i)
    {
        if(i==1 || i==2)
            SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),15);
        else if(i==3 || i==4)
            SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),9);
        else SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),12);
        for(int j=1;j<=21;++j)
            cout<<(char)219;
        cout<<'\n';
    }
    SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),15);
    cout<<endl<<"34) Serbia: \n";
    for(int i=1;i<=6;++i)
    {
        if(i==1 || i==2)
            SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),4);
        else if(i==3 || i==4)
            SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),1);
        else SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),15);
        for(int j=1;j<=21;++j)
            cout<<(char)219;
        cout<<'\n';
    }
    SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),15);
    cout<<endl<<"35) San Marino: \n";
    for(int i=1;i<=6;++i)
    {
        if(i>=1 && i<=3)
            SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),15);
        else SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),11);
        for(int j=1;j<=21;++j)
            cout<<(char)219;
        cout<<'\n';
    }
    SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),15);
    cout<<endl<<"36) Suedia: \n";
    for(int i=1;i<=6;++i)
    {
        if(i==1 || i==2 || i==5 || i==6)
            SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),9);
        else SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),14);
        for(int j=1;j<=21;++j)
        {
            if(j==7 || j==8 || j==6)
                SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),14);
            else if(j!=7 && j!=8 && j!=6 && i!=3 && i!=4)
                SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),9);
            cout<<(char)219;
        }
        cout<<'\n';
    }
    SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),15);
    cout<<endl<<"37) Tara Galilor: \n";
    for(int i=1;i<=6;++i)
    {
        if(i>=1 && i<=3)
            SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),15);
        else SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),10);
        for(int j=1;j<=21;++j)
            cout<<(char)219;
        cout<<'\n';
    }
    SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),15);
    cout<<endl<<"38) Turcia: \n";
    for(int i=1;i<=6;++i)
    {
        SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),12);
        for(int j=1;j<=21;++j)
            cout<<(char)219;
        cout<<'\n';
    }
    SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),15);
    cout<<endl<<"39) Ucraina: \n";
    for(int i=1;i<=6;++i)
    {
        if(i>=1 && i<=3)
            SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),9);
        else SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),14);
        for(int j=1;j<=21;++j)
            cout<<(char)219;
        cout<<'\n';
    }
    SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),15);
    cout<<endl<<"40) Ungaria: \n";
    for(int i=1;i<=6;++i)
    {
        if(i==1 || i==2)
            SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),12);
        else if(i==3 || i==4)
            SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),15);
        else SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),2);
        for(int j=1;j<=21;++j)
            cout<<(char)219;
        cout<<'\n';
    }
    SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),15);
    cout<<endl<<"41) Vatican: \n";
    for(int i=1;i<=6;++i)
    {
        for(int j=1;j<=21;++j)
        {
            if(j<=10)
                SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),14);
            else SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),15);
            cout<<(char)219;
        }
        cout<<'\n';
    }
    SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),15);
    cout<<endl<<"42) Voivodina: \n";
    for(int i=1;i<=6;++i)
    {
        if(i==1)
            SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),12);
        else if(i==6)
            SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),15);
        else SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),1);
        for(int j=1;j<=21;++j)
            cout<<(char)219;
        cout<<'\n';
    }
    SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),15);
    return 0;
}
