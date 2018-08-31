from os import system, name
from time import sleep
import numpy as np
import sys
import random

def clear():
    if name == 'nt':
        _ = system('cls')
    else :
        _ = system('clear')
class Minesweeper:
    def __init__(self,n,per):
           self.n = n
           self.per = per
           self.show = np.zeros((n,n))
           for i in range(0,n):
               for j in range(0,n):
                   self.show[i,j] = -1
           self.hide = np.zeros((n,n))
           self.placeMines()
           self.proxims()
           self.playChance()
    def checkWin(self):
        for i in range(0,self.n):
            for j in range(0,self.n):
                if self.show[i,j] == -1:
                  if self.hide[i,j] != -1:
                      return False
        return True
    def placeMines(self):
        for i in range(int((self.n*self.n*self.per)/100)):
            i = random.randint(0,self.n-1)
            j = random.randint(0,self.n-1)
            self.hide[i,j] = -1
    def increms(self,i,j):
        if self.hide[i,j] != -1:
            self.hide[i,j]+=1
    def proxims(self):
        for i in range(self.n):
            for j in range(self.n):
                if self.hide[i,j] == -1:
                    if i-1 != -1:
                        self.increms(i-1,j)
                        if j-1 != -1: # if NOT Top Right Corner
                            self.increms(i-1,j-1)
                            self.increms(i,j-1)
                        if j+1 != self.n:  # if NOT Top Left Corner
                            self.increms(i-1,j+1)
                            self.increms(i,j+1)
                    if i+1 != self.n :
                        self.increms(i+1,j)
                        if j-1 != -1: # if NOT Bottom Right Corner
                            self.increms(i+1,j-1)
                        if j+1 != self.n:  # if NOT Bottom Left Corner
                            self.increms(i+1,j+1)                          
    def showMines(self):
        print(self.hide)
    def showArea(self):
           for i in range(0,self.n):
               for j in range(0,self.n):
                   if self.show[i,j] == -1 :
                       print(" < . > \t",end='')
                   else:
                       print(" < "+str(int(self.show[i,j]))+" > \t",end='')
               print()
    def playChance(self):
        try:
            i = int(input("Enter the row ( 0 - "+str(self.n)+" ) : "))
        except ValueError:
            print("Wrong Value Entered ")
            try:
                i = int(input("Enter the row ( 0 - "+str(self.n)+" ) : "))
                if i<0 or i>=self.n:
                    raise NameError("Out of Bounds")
            except ValueError:
                print("Wrong Value Entered ")
                print("Exiting Program")
            except NameError:
                sys.exit()
        try:
            j = int(input("Enter the column ( 0 - "+str(self.n)+" ) : "))
        except ValueError:
            print("Wrong Value Entered ")
            try:
                j = int(input("Enter the column ( 0 - "+str(self.n)+" ) : "))
                if j<0 or j>=self.n:
                    raise NameError("Out of Bounds")
            except ValueError:
                print("Wrong Value Entered ")
                print("Exiting Program")
            except NameError:
                sys.exit()
        if self.show[i,j] != -1:
            print("Already Open")
            if self.checkWin() == True:
                print("Congrats you have Completed...")
                self.showMines()
            else:
                self.playChance()
        else:
            if self.hide[i,j] != -1:
                mink = self.n
                maxk = 0
                for s in range(i,self.n):
                    if self.hide[s,j] != 0:
                        break;
                    for k in range(j,self.n):
                        if self.hide[s,k] == 0 and mink > k:
                            self.show[s,k] = self.hide[s,k]
                        else:
                            if mink > k:
                                mink = k
                            break
                    for k in range(0,j):
                        g = j-k
                        if self.hide[s,g] == 0 and maxk < g:
                            self.show[s,g] = self.hide[s,g]
                        else:
                            if maxk < g:
                                maxk = g
                            break
                mink = self.n
                maxk = 0
                for s in range(0,i):
                    h = i-s
                    if self.hide[h,j]!=0:
                        break;
                    for k in range(j,self.n):
                        if self.hide[h,k] == 0 and mink > k:
                            self.show[h,k] = self.hide[h,k]
                        else:
                            if mink > k:
                                mink = k
                            break
                    for k in range(0,j):
                        g = j-k
                        if self.hide[h,g] == 0 and maxk < g:
                            self.show[h,g] = self.hide[h,g]
                        else:
                            if maxk < g:
                                maxk = g
                            break                        
                self.show[i,j]=(self.hide[i,j])
                sleep(1)
                clear()
                self.showArea()
                self.showMines()
                self.playChance()
            else:
                self.showMines()
                print("Game Over")
a = Minesweeper(10,10)