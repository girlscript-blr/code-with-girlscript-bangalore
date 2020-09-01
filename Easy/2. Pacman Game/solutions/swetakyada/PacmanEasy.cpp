#include <bits/stdc++.h>
#include <conio.h>
#include<cstdlib>
using namespace std;

#define height 11
#define width 51

char Matrix[height][width];
bool gameOver;
int PacmanX, PacmanY;

void setup()
{
    gameOver = false;
    PacmanX = 1;
    PacmanY = 1;
    for(int i = 0; i < height; i++)
    {
        for(int j = 0; j < width; j++)
        {
            if(i==0 || i==height-1)
                Matrix[i][j] = '-';
            else if(j==0 || j==width-1)
                Matrix[i][j] = '|';
            else
            {
                if((i+j)%3==0 && j%5==0)
                    Matrix[i][j] = '|';
                else if(i%2!=0 && (i+j)%3==0)
                    Matrix[i][j] = '-';
                else
                    Matrix[i][j] = ' ';
            }
        }
    }
    Matrix[PacmanX][PacmanY] = '@';
}

void print()
{
    for(int i = 0; i < height; i++)
    {
        for(int j = 0; j < width; j++)
        {
                cout << Matrix[i][j];
        }
        cout << endl;
    }
}

void input()
{
    int ch1,ch2=0;
    ch1 = getch();
    if(ch1 = 0xE0 || ch1==27)
    {
        ch2 = getch();
        switch (ch2)
        {
        case 72:
            if(Matrix[PacmanX-1][PacmanY]=='|' || Matrix[PacmanX-1][PacmanY]=='-')
                break;
            else
            {
                Matrix[PacmanX--][PacmanY] = ' ';
                Matrix[PacmanX][PacmanY] = '@';
                print();
            }
            break;
        case 80:
            if(Matrix[PacmanX+1][PacmanY]=='|' || Matrix[PacmanX+1][PacmanY]=='-')
                break;
            else
            {
                Matrix[PacmanX++][PacmanY] = ' ';
                Matrix[PacmanX][PacmanY] = '@';
                print();
            }
            break;
        case 77:
            if(Matrix[PacmanX][PacmanY+1]=='|' || Matrix[PacmanX][PacmanY+1]=='-')
                break;
            else
            {
                Matrix[PacmanX][PacmanY++] = ' ';
                Matrix[PacmanX][PacmanY] = '@';
                print();
            }
            break;
        case 75:
            if(Matrix[PacmanX][PacmanY-1]=='|' || Matrix[PacmanX][PacmanY-1]=='-')
                break;
            else
            {
                Matrix[PacmanX][PacmanY--] = ' ';
                Matrix[PacmanX][PacmanY] = '@';
                print();
            }
            break;
        case 27:
            gameOver = true;
            break;
        default:
            break;
        }
    }
}

int main()
{
    setup();
    print();
    while(!gameOver)
    {
        input();
    }
    cout << "Game Ended..." << endl;
    return 0;
}