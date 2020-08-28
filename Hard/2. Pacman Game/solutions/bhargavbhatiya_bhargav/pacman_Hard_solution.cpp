#include <bits/stdc++.h>
#include <conio.h>
#include <cstdlib>

using namespace std;
char board[10][40];
int flag = 0;
char temp[10][40];

void reset(int &level);

//for moving ghosts...
int ghost_move(int &m, int &n)
{
   int ran;
   ran = rand() % 4 + 1;
   // cout<<endl<<ran<<endl;

   switch (ran)
   {
   case 1:
      if (board[m - 1][n] != '-' && board[m - 1][n] != '|' && board[m - 1][n] != '@' && board[m - 1][n] != '&')
      {
         temp[m - 1][n] = board[m - 1][n];
         board[m][n] = temp[m][n];
         board[m - 1][n] = '&';
         m--;
      }
      else
      {
         ghost_move(m, n);
      }
      break;
   case 2:
      if (board[m + 1][n] != '-' && board[m + 1][n] != '|' && board[m + 1][n] != '@' && board[m + 1][n] != '&')
      {
         temp[m + 1][n] = board[m + 1][n];
         board[m][n] = temp[m][n];
         board[m + 1][n] = '&';
         m++;
      }
      else
      {
         ghost_move(m, n);
      }
      break;
   case 3:
      if (board[m][n - 1] != '|' && board[m][n - 1] != '-' && board[m][n - 1] != '@' && board[m][n - 1] != '&')
      {
         temp[m][n - 1] = board[m][n - 1];
         board[m][n] = temp[m][n];
         board[m][n - 1] = '&';
         n--;
      }
      else
      {
         ghost_move(m, n);
      }
      break;
   case 4:
      if (board[m][n + 1] != '|' && board[m][n + 1] != '-' && board[m][n + 1] != '@' && board[m][n + 1] != '&')
      {
         temp[m][n + 1] = board[m][n + 1];
         board[m][n] = temp[m][n];
         board[m][n + 1] = '&';
         n++;
      }
      else
      {
         ghost_move(m, n);
      }
      break;
   }
   // cout << endl
   //   << board[m][n];
   // if (board[m - 1][n] == '@' || board[m + 1][n] == '@' || board[m][n + 1] == '@' || board[m][n - 1] == '@')
   // {

   //    return 2;
   // }
   if (board[m - 1][n] == '@')
   {
      m--;
      return 2;
   }
   else if (board[m + 1][n] == '@')
   {
      m++;
      return 2;
   }
   else if (board[m][n + 1] == '@')
   {
      n++;
      return 2;
   }
   else if (board[m][n - 1] == '@')
   {
      n--;
      return 2;
   }

   return 3;
}
void set_board(int &score, int &level)
{
   //setting boundary to the board
   for (int i = 1; i <= 10; i++)
   {
      for (int j = 1; j <= 40; j++)
      {
         if (i == 1 || i == 10)
         {
            board[i][j] = '-';
         }
         else if (j == 1 || j == 40)
         {
            board[i][j] = '|';
         }
         else
         {
            board[i][j] = '.';
         }
      }
   }
   board[2][2] = '@';

   //setting vertical walls
   board[2][3] = '|';

   board[2][6] = '|';
   board[3][6] = '|';
   board[4][6] = '|';

   board[2][10] = '|';
   board[3][10] = '|';

   board[8][12] = '|';
   board[7][12] = '|';
   board[6][12] = '|';
   board[5][12] = '|';

   board[6][15] = '|';
   board[7][15] = '|';

   board[9][20] = '|';
   board[8][20] = '|';
   board[7][20] = '|';

   board[3][18] = '|';
   board[4][18] = '|';
   board[5][18] = '|';

   board[2][22] = '|';
   board[3][22] = '|';
   board[4][22] = '|';
   board[5][22] = '|';

   board[6][7] = '|';
   board[7][7] = '|';
   board[8][7] = '|';
   board[9][7] = '|';

   board[4][25] = '|';
   board[5][25] = '|';
   board[6][25] = '|';
   board[7][25] = '|';

   board[8][28] = '|';
   board[9][28] = '|';
   board[7][28] = '|';

   board[3][31] = '|';
   board[4][31] = '|';
   board[5][31] = '|';
   board[6][31] = '|';
   board[7][31] = '|';

   board[2][35] = '|';
   board[3][35] = '|';
   board[4][35] = '|';
   board[7][35] = '|';
   board[8][35] = '|';
   board[9][35] = '|';

   //setting horizontal walls
   board[3][11] = '-';
   board[3][9] = '-';
   board[3][12] = '-';
   board[3][13] = '-';
   board[3][23] = '-';
   board[3][29] = '-';
   board[3][30] = '-';
   board[3][27] = '-';
   board[3][28] = '-';

   board[4][3] = '-';
   board[4][4] = '-';
   board[4][5] = '-';
   board[4][19] = '-';
   board[4][20] = '-';
   board[4][21] = '-';

   board[5][26] = '-';
   board[5][27] = '-';
   board[5][35] = '-';
   board[5][36] = '-';
   board[5][37] = '-';

   board[6][4] = '-';
   board[6][5] = '-';
   board[6][6] = '-';

   board[7][16] = '-';
   board[7][17] = '-';
   board[7][18] = '-';
   board[7][19] = '-';
   board[7][32] = '-';
   board[7][33] = '-';
   board[7][34] = '-';
   board[7][35] = '-';

   board[8][2] = '-';
   board[8][3] = '-';
   board[8][4] = '-';
   board[8][8] = '-';
   board[8][9] = '-';
   board[8][22] = '-';
   board[8][23] = '-';
   board[8][24] = '-';
   board[8][25] = '-';

   //puting initially ghosts on board

   if (level == 1)
   {
      board[4][17] = '&';
   }
   else if (level == 2)
   {
      board[4][17] = '&';
      board[9][21] = '&';
   }
   else if (level == 3)
   {
      board[4][17] = '&';
      board[9][21] = '&';
      board[6][32] = '&';
   }
   temp[4][17] = '.';
   temp[9][21] = '.';
   temp[6][32] = '.';
}

void print(int &m, int &n, int &ghost1_row, int &ghost1_column, int &ghost2_row, int &ghost2_column, int &ghost3_row, int &ghost3_column, int &level, int &score)
{

   //printing board
   board[9][40] = '|';
   board[10][1] = '-';
   board[10][2] = '-';
   board[10][3] = '-';
   cout << "```````````````level:" << level << "```````````````````" << endl;
   for (int i = 1; i <= 10; i++)
   {
      for (int j = 1; j <= 40; j++)
      {
         cout << board[i][j];
      }
      cout << endl;
   }
   cout << endl
        << "point score: " << score << endl;
   //for next level...
   if ((score == 1100 && level == 1) || (score == 1095 && level == 2) || (score == 1090 && level == 3))
   {
      cout << ""
           << "``````````````CONGRATULATIONS YOU WON!!```````````````" << endl;
      level++;
      reset(level);
      return;
   }

   //moving pacman...with arrow keys...
   int ch1, ch2 = 0;
   ch1 = getch();
   if (ch1 == 0xE0)
   {
      flag = 0;
      ch2 = getch();
      switch (ch2)
      {
      case 72: //upper arrow key
         if (board[m - 1][n] != '-' && board[m - 1][n] != '|' && board[m - 1][n] != '&')
         {
            board[m][n] = ' ';
            if (board[m - 1][n] == '.')
            {
               score += 5;
            }
            m--;
         }
         else if (board[m - 1][n] == '&')
         {
            flag = 2;
            goto dead;
         }
         else if (board[m - 1][n] == '|' || board[m - 1][n] == '-')
         {
         }
         else
         {
            flag = 1;
            goto dead;
         }
         break;
      case 80: //down arrow key
         if (board[m + 1][n] != '-' && board[m + 1][n] != '|' && board[m + 1][n] != '&')
         {
            board[m][n] = ' ';
            if (board[m + 1][n] == '.')
            {
               score += 5;
            }
            m++;
         }
         else if (board[m + 1][n] == '&')
         {
            flag = 2;
            goto dead;
         }
         else if (board[m + 1][n] == '|' || board[m + 1][n] == '-')
         {
         }
         else
         {
            flag = 1;
            goto dead;
         }
         break;
      case 75: //left arrow key...
         if (board[m][n - 1] != '|' && board[m][n - 1] != '-' && board[m][n - 1] != '&')
         {
            board[m][n] = ' ';
            if (board[m][n - 1] == '.')
            {
               score += 5;
            }
            n--;
         }
         else if (board[m][n - 1] == '&')
         {
            flag = 2;
            goto dead;
         }
         else if (board[m][n - 1] == '|' || board[m][n - 1] == '-')
         {
         }
         else
         {
            flag = 1;
            goto dead;
         }
         break;
      case 77: //right arrow key
         if (board[m][n + 1] != '|' && board[m][n + 1] != '-' && board[m][n + 1] != '&')
         {
            board[m][n] = ' ';
            if (board[m][n + 1] == '.')
            {
               score += 5;
            }
            n++;
         }
         else if (board[m][n + 1] == '&')
         {
            flag = 2;
            goto dead;
         }
         else if (board[m][n + 1] == '|' || board[m][n + 1] == '-')
         {
         }
         else
         {
            flag = 1;
            goto dead;
         }
         break;
      }
      board[m][n] = '@';

      //moving ghosts
      int ch;
      if (level == 1)
      {
         ch = ghost_move(ghost1_row, ghost1_column);
         if (ch == 2)
         {
            flag = 2;
            goto dead;
         }
      }
      else if (level == 2)
      {
         ch = ghost_move(ghost1_row, ghost1_column);
         if (ch == 2)
         {
            flag = 2;
            goto dead;
         }
         ch = ghost_move(ghost2_row, ghost2_column);
         if (ch == 2)
         {
            flag = 2;
            goto dead;
         }
      }
      else if (level == 3)
      {
         ch = ghost_move(ghost1_row, ghost1_column);
         if (ch == 2)
         {
            flag = 2;
            goto dead;
         }
         ch = ghost_move(ghost2_row, ghost2_column);
         if (ch == 2)
         {
            flag = 2;
            goto dead;
         }
         ch = ghost_move(ghost3_row, ghost3_column);
         if (ch == 2)
         {
            flag = 2;
            goto dead;
         }
      }

   dead: //when pacman collide with wall or ghost

      if (flag == 2)
      {
         //printing board
         board[9][40] = '|';
         board[10][1] = '-';
         board[10][2] = '-';
         board[10][3] = '-';
         cout << "```````````````level:" << level << "```````````````````" << endl;
         for (int i = 1; i <= 10; i++)
         {
            for (int j = 1; j <= 40; j++)
            {
               cout << board[i][j];
            }
            cout << endl;
         }
         cout << endl
              << "point score: " << score << endl;

         // cout << endl
         //   << board[ghost1_row][ghost1_column] << endl;
         cout << endl
              << "```SORRY,You collide with ghost!! U lost the game!!```" << endl;
         return;
      }
      // else if (flag == 1)
      // {
      //    //printing board
      //    cout << "```````````````level:" << level << "```````````````````" << endl;
      //    for (int i = 1; i <= 10; i++)
      //    {
      //       for (int j = 1; j <= 40; j++)
      //       {
      //          cout << board[i][j];
      //       }
      //       cout << endl;
      //    }
      //    cout << endl
      //         << "point score: " << score<<endl;

      //    cout << endl
      //         << "```SORRY, YOU CAN't MOVE!! U lost the game!!```" << endl;
      //    return;
      // }

      //if U not lost game, continue...
      if (flag == 0)
      {
         return print(m, n, ghost1_row, ghost1_column, ghost2_row, ghost2_column, ghost3_row, ghost3_column, level, score);
      }
   }
}

//when level is changed, resetting all values(ghost,packman,score)....
void reset(int &level)
{
   int score = 0;
   int m = 2, n = 2;

   int ghost1_row = 4, ghost1_column = 17, ghost2_row = 9, ghost2_column = 21, ghost3_row = 6, ghost3_column = 32;
   set_board(score, level);

   print(m, n, ghost1_row, ghost1_column, ghost2_row, ghost2_column, ghost3_row, ghost3_column, level, score);
}

int main(int argc, char const *argv[])
{
   int level = 1;

   int score = 0;
   int m = 2, n = 2;

   int ghost1_row = 4, ghost1_column = 17, ghost2_row = 9, ghost2_column = 21, ghost3_row = 6, ghost3_column = 32;
   set_board(score, level);

   print(m, n, ghost1_row, ghost1_column, ghost2_row, ghost2_column, ghost3_row, ghost3_column, level, score);

   return 0;
}
