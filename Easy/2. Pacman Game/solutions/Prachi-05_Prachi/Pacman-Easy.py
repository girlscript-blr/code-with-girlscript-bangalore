# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 19:03:33 2020

@author: Prachi
"""


from pynput.keyboard import Key, Listener
from os import system, name 
#from time import sleep 




class Pacman:

    maze = list(list())
    pacmanx = 1
    pacmany = 1
    
    def __init__(self,maze,pacmanx,pacmany):
        self.maze = maze
        self.pacmanx = pacmanx
        self.pacmany = pacmany
        self.maze[self.pacmanx][self.pacmany]='@'
        
	# for windows 
    def clear(self):
    	if name == 'nt': 
    		_ = system('cls') 
    
    	# for mac and linux(here, os.name is 'posix') 
    	else: 
    		_ = system('clear') 

    def dispMaze(self):        
        self.clear()
        for i in maze:
            for j in i:
                print(j,end='')
            print()
        


    def move(self,x,y):
        if(aself.maze[self.pacmanx+x][self.pacmany+y]!='|' and self.maze[self.pacmanx+x][self.pacmany+y]!='-'):        
                
            self.maze[self.pacmanx][self.pacmany]=' '
            self.pacmanx += x
            self.pacmany += y
            self.maze[self.pacmanx][self.pacmany]='@'
            self.dispMaze()
            
    
    def play(self):
        while True:    
            def on_press(key):
                try:
                    if key == Key.up:
                        self.move(-1,0)
                    elif key == Key.down:
                        self.move(1,0)
                    elif key == Key.right:
                        self.move(0,1)
                    elif key == Key.left:
                        self.move(0,-1)
                    elif (key.char == ('w') or key.char == ('W')):
                        self.move(-1,0)
                    elif (key.char == ('s') or key.char == ('S')):
                        self.move(1,0)
                    elif (key.char == ('d') or key.char == ('D')):
                        self.move(0,1)
                    elif (key.char == ('a') or key.char == ('A')):
                        self.move(0,-1)
                except AttributeError:
                    pass
                
            def on_release(key):
                if key == Key.esc:
                    # Stop listener
                    print("Exiting program...")
                    exit()
            
            # Collect events until released
            with Listener(
                    on_press=on_press,
                    on_release=on_release) as listener:
                listener.join()
        
maze = [['-']*40,
        ['|',' ',' ',' ',' ',' ',' ',' ',' ','|',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','|',' ',' ',' ',' ',' ',' ',' ',' ',' ','|'],
        ['|',' ',' ','|','-','-',' ',' ',' ','|',' ',' ','|','-','-',' ',' ','-','-','-','-','-','-',' ','-','-','|',' ',' ','|',' ',' ',' ',' ',' ',' ',' ',' ',' ','|'],
        ['|',' ',' ','|',' ',' ',' ',' ',' ','|',' ',' ','|',' ',' ',' ',' ',' ',' ',' ','|',' ',' ',' ',' ',' ','|',' ',' ','|',' ',' ',' ',' ',' ',' ',' ',' ',' ','|'],
        ['|',' ',' ',' ',' ',' ',' ','|','-','|',' ',' ','|',' ','|','-','-','-',' ','|',' ','|','-','-','|',' ',' ',' ',' ','|','-','|',' ',' ',' ',' ',' ',' ',' ','|'],
        ['|','-','-','-','-',' ',' ',' ',' ','|',' ',' ','|',' ','|',' ',' ',' ',' ','|',' ','|',' ',' ','|',' ','|',' ',' ',' ',' ','|',' ',' ',' ','-','-','-','-','|'],
        ['|',' ',' ',' ',' ',' ',' ',' ',' ','|','-','-','|',' ','|',' ',' ',' ',' ',' ',' ',' ',' ',' ','|',' ','|','-','-',' ',' ','|',' ',' ',' ',' ',' ',' ',' ','|'],
        ['|',' ',' ',' ',' ','-','-','|',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','-','-','-','-','-',' ',' ',' ','|',' ',' ',' ',' ','|','-','-','-','-',' ',' ',' ','|'],
        ['|',' ',' ',' ',' ',' ',' ','|',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','|',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','|'],
        ['-']*40]

pacmanx = 1
pacmany = 1

obj = Pacman(maze,pacmanx,pacmany)
obj.dispMaze()
obj.play()