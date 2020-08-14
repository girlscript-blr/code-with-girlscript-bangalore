#include <iostream>
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
    char ch;
    cin >> ch;
    switch (ch)
    {
    case 'W':
    case 'w':
        if(Matrix[PacmanX-1][PacmanY]=='|' || Matrix[PacmanX-1][PacmanY]=='-')
            gameOver = true;
        else
        {
            Matrix[PacmanX--][PacmanY] = ' ';
            Matrix[PacmanX][PacmanY] = '@';
            print();
        }
        break;
    case 'S':
    case 's':
        if(Matrix[PacmanX+1][PacmanY]=='|' || Matrix[PacmanX+1][PacmanY]=='-')
            gameOver = true;
        else
        {
            Matrix[PacmanX++][PacmanY] = ' ';
            Matrix[PacmanX][PacmanY] = '@';
            print();
        }
        break;
    case 'D':
    case 'd':
        if(Matrix[PacmanX][PacmanY+1]=='|' || Matrix[PacmanX][PacmanY+1]=='-')
            gameOver = true;
        else
        {
            Matrix[PacmanX][PacmanY++] = ' ';
            Matrix[PacmanX][PacmanY] = '@';
            print();
        }
        break;
    case 'A':
    case 'a':
        if(Matrix[PacmanX][PacmanY-1]=='|' || Matrix[PacmanX][PacmanY-1]=='-')
            gameOver = true;
        else
        {
            Matrix[PacmanX][PacmanY--] = ' ';
            Matrix[PacmanX][PacmanY] = '@';
            print();
        }
        break;
    default:
        cout << "Invalid Input" << endl;
        gameOver = true;
        break;
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
    cout << "Game Over" << endl;
    return 0;
}