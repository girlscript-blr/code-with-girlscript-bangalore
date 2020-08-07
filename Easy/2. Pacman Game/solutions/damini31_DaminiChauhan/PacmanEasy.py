# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 12:56:13 2020

@author: daminichauhan1997
"""
def check_size(grid):
    r=len(grid)
    c=len(grid[0])
    
    if(r>=10 and c>=40):
        return True
    else:
        return False
    
def pacman_position(r,c):
    for i in range(r):
        for j in range(c):
            if(grid[i][j]== "@"):
                return i,j
                break;
                
def check_move_W(a,b,grid):
    try:
        if(grid[a-1][b]==" "):
            return True
        else:
            return False
    except(ValueError):
        print("\nInvalid move")

def move_W(a,b,grid):
    try:
        grid[a-1][b]="@"
        grid[a][b]=" "
    
    except(ValueError):
        print("Invalid move")
        
def check_move_S(a,b,grid):
    try:
        if(grid[a+1][b]==" "):
            return True
        else:
            return False
    except(ValueError):
        print("\nInvalid move")

def move_S(a,b,grid):
    try:
        grid[a+1][b]="@"
        grid[a][b]=" "
    
    except(ValueError):
        print("Invalid move")
        
def check_move_A(a,b,grid):
    try:
        if(grid[a][b-1]==" "):
            return True
        else:
            return False
    except(ValueError):
        print("\nInvalid move")

def move_A(a,b,grid):
    try:
        grid[a][b-1]="@"
        grid[a][b]=" "
    
    except(ValueError):
        print("Invalid move")
        
def check_move_D(a,b,grid):
    try:
        if(grid[a][b+1]==" "):
            return True
        else:
            return False
    except(ValueError):
        print("\nInvalid move")

def move_D(a,b,grid):
    try:
        grid[a][b+1]="@"
        grid[a][b]=" "
    
    except(ValueError):
        print("Invalid move")
        
print("\n----------------------------Welcome to Pacman--------------------------------")
grid=[['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-'],
      ['|','@','|',' ',' ',' ',' ','|',' ','|',' ',' ',' ',' ',' ',' ',' ','|',' ',' ',' ',' ',' ',' ','|',' ','|',' ','|',' ',' ','|',' ','|',' ',' ',' ','|',' ','|'],
      ['|',' ','|',' ',' ',' ',' ','|',' ','-','-','|',' ',' ',' ',' ',' ','|',' ','|','-','-','-',' ','|',' ','|',' ','|',' ',' ','|',' ','|',' ',' ',' ','|',' ','|'],
      ['|',' ','|','-','-','-','-','|',' ',' ',' ','|',' ',' ',' ',' ',' ','|',' ','|',' ',' ','|',' ','|',' ','|',' ',' ','-','-','-',' ','|',' ',' ',' ','|',' ','|'],
      ['|',' ',' ',' ',' ',' ',' ',' ',' ','|',' ','|','-','-','-','-','-','-',' ','|',' ',' ','|',' ','|',' ','|',' ',' ',' ',' ',' ',' ','-','-','-','-','|',' ','|'],
      ['|',' ','|','-','-','-','-','|',' ','|',' ',' ',' ',' ',' ',' ',' ',' ',' ','|','-','-','|',' ','|','-','-',' ',' ','-','-','-',' ',' ',' ',' ',' ','|',' ','|'],
      ['|',' ','|',' ',' ',' ',' ','|',' ','|',' ','|','-','-','-','-','-','-',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','|',' ','-','-','-',' ','|',' ','|'],
      ['|',' ','|',' ',' ',' ',' ','|',' ','|',' ','|',' ',' ',' ',' ',' ','|',' ',' ',' ',' ',' ',' ',' ',' ',' ','|',' ',' ',' ','|',' ','|',' ','|',' ',' ',' ','|'],
      ['|',' ','|',' ',' ',' ',' ','|',' ','|',' ','|',' ',' ',' ',' ',' ','|',' ','|','-','-','|',' ','|','-','-','|',' ',' ',' ','|',' ','|',' ','|',' ','|',' ','|'],
      ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-']]



if(check_size(grid)==True):
  r=len(grid)
  c=len(grid[0])

  def p_grid(r,c,grid):
   for i in range(r):
      for j in range(c):
        print(grid[i][j],end=" ")
      print("\n") 

  p_grid(r,c,grid)
  print("\nLet the game begin.......................................")

  print("\n*************Rules***************")
  print("\n Press W to move up.")
  print("\n Press S to move down.")
  print("\n Press A to move left.")
  print("\n Press D to move right.")
  print("\nPress 0 to exit.")

  move="No"
  while(move!="0"):
    move=input("Which direction do you wish to move in?Press 0 to exit.")
    if(move=='W'):
        a,b=pacman_position(r, c)
        if(check_move_W(a,b,grid)== True):
            move_W(a,b,grid)
            p_grid(r,c,grid)
            
        else:
         print("Invalid move")
    
    elif(move=='S'):
        a,b=pacman_position(r, c)
        if(check_move_S(a,b,grid)== True):
            move_S(a,b,grid)
            p_grid(r,c,grid)
            
        else:
         print("Invalid move")

    elif(move=='A'):
        a,b=pacman_position(r, c)
        if(check_move_A(a,b,grid)== True):
            move_A(a,b,grid)
            p_grid(r,c,grid)
            
        else:
         print("Invalid move")    
    
    elif(move=='D'):
        a,b=pacman_position(r, c)
        if(check_move_D(a,b,grid)== True):
            move_D(a,b,grid)
            p_grid(r,c,grid)
            
        else:
         print("Invalid move")
         
    elif(move=="0"):
       print("Exiting the game.................................")
       break;
    
    else:
       print("\nPlease enter the correct key.")
       print("\n*************Rules***************")
       print("\n Press W to move up.")
       print("\n Press S to move down.")
       print("\n Press A to move left.")
       print("\n Press D to move right.")
       print("\nPress 0 to exit.")
       
  print("***********************Thanks for playing*******************************")

else:
  print("The grid size is not acceptable.Number of rows should be atleast 10 and number of columns should be atleast 40.")            
  print("The grid entered by you has {} rows and {} columns".format(len(grid),len(grid[0])))          
           






















