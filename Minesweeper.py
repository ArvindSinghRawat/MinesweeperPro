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
        max = int((self.n*self.n*self.per)/100)
        while max >= 0:
            i = random.randint(0,self.n-1)
            j = random.randint(0,self.n-1)
            if self.show[i,j] == -1:
                self.hide[i,j] = -1
                max -= 1
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
                    else:
                        if j-1 != -1:
                            self.increms(i,j-1)
                        if j+1 != self.n:
                            self.increms(i,j+1)
                    if i+1 != self.n :
                        self.increms(i+1,j)
                        if j-1 != -1: # if NOT Bottom Right Corner
                            self.increms(i+1,j-1)
                        if j+1 != self.n:  # if NOT Bottom Left Corner
                            self.increms(i+1,j+1)      
    def countMines(self):
        cnt=0
        for i in range(self.n):
            for j in range(self.n):
                if self.hide[i,j] == -1:
                    cnt += 1
        print("Count = "+str(cnt))
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
    def copyLeft(self,i,j):
        if j>=0:
            if self.show[i,j] == -1:
                self.show[i,j] = self.hide[i,j]
                if self.hide[i,j] == 0:
                    self.copyLeft(i,j-1)
                    self.copyUp(i-1,j)
                    self.copyDown(i+1,j)
                else:
                    if i > 0:
                        self.show[i-1,j] = self.hide[i-1,j]
                        if self.hide[i-1,j] == 0:
                            self.copyUp(i-2,j)
                            self.copyLeft(i-1,j-1)
                            self.copyRight(i-1,j+1)
                    if i < self.n-1:
                        self.show[i+1,j] = self.hide[i+1,j]
                        if self.hide[i+1,j] == 0:
                            self.copyDown(i+2,j)
                            self.copyLeft(i+1,j-1)
                            self.copyRight(i+1,j+1)
    def copyRight(self,i,j):
        if j<self.n:
            if self.show[i,j] == -1:
                self.show[i,j] = self.hide[i,j]
                if self.hide[i,j] == 0:
                    self.copyRight(i,j+1)
                    self.copyUp(i-1,j)
                    self.copyDown(i+1,j)
                else:
                    if i > 0:
                        self.show[i-1,j] = self.hide[i-1,j]
                        if self.hide[i-1,j] == 0:
                            self.copyUp(i-2,j)
                            self.copyLeft(i-1,j-1)
                            self.copyRight(i-1,j+1)
                    if i < self.n-1:
                        self.show[i+1,j] = self.hide[i+1,j]
                        if self.hide[i+1,j] == 0:
                            self.copyDown(i+2,j)
                            self.copyLeft(i+1,j-1)
                            self.copyRight(i+1,j+1)
    def copyUp(self,i,j):
        if i>=0:
            if self.show[i,j] == -1:
                self.show[i,j] = self.hide[i,j]
                if self.hide[i,j] == 0:
                    self.copyUp(i-1,j)
                    self.copyLeft(i,j-1)
                    self.copyRight(i,j+1)
                else:
                    if j > 0:
                        self.show[i,j-1] = self.hide[i,j-1]
                        if self.hide[i,j-1] == 0:
                            self.copyDown(i+1,j-1)
                            self.copyLeft(i,j-2)
                            self.copyUp(i-1,j-1)
                    if j < self.n-1 :
                        self.show[i,j+1] = self.hide[i,j+1]
                        if self.hide[i,j+1] == 0:
                            self.copyDown(i+1,j+1)
                            self.copyRight(i,j+2)
                            self.copyUp(i-1,j+1)
    def copyDown(self,i,j):
        if i<self.n:
            if self.show[i,j] == -1:
                self.show[i,j] = self.hide[i,j]
                if self.hide[i,j] == 0:
                    self.copyDown(i+1,j)
                    self.copyLeft(i,j-1)
                    self.copyRight(i,j+1)
                else:
                    if j > 0: 
                        self.show[i,j-1] = self.hide[i,j-1]
                        if self.hide[i,j-1] == 0:
                            self.copyDown(i+1,j-1)
                            self.copyLeft(i,j-2)
                            self.copyUp(i-1,j-1)
                    if j < self.n-1:
                        self.show[i,j+1] = self.hide[i,j+1]
                        if self.hide[i,j+1] == 0:
                            self.copyDown(i+1,j+1)
                            self.copyRight(i,j+2)
                            self.copyUp(i-1,j+1)
    def changeNeighbour(self,i,j):
        self.copyUp(i-1,j)
        self.copyDown(i+1,j)
        self.copyRight(i,j+1)
        self.copyLeft(i,j-1)            
    def playChance(self):
        self.countMines()
        try:
            i = int(input("Enter the row ( 0 - "+str(self.n)+" ) : "))
            if i<0 or i>=self.n:
                    raise NameError("Out of Bounds")
        except ValueError:
            print("Wrong Value Entered ")
            try:
                i = int(input("Enter the row ( 0 - "+str(self.n-1)+" ) : "))
                if i<0 or i>=self.n:
                    raise NameError("Out of Bounds")
            except ValueError:
                print("Wrong Value Entered ")
                print("Exiting Program")
                sys.exit()
            except NameError:
                print("Wrong Value Entered ")
                print("Exiting Program")
                sys.exit()
        except NameError:
            print("Enter Value Between 0 - "+str(self.n-1))
            try:
                i = int(input("Enter the row ( 0 - "+str(self.n-1)+" ) : "))
                if i<0 or i>=self.n:
                    raise NameError("Out of Bounds")
            except ValueError:
                print("Wrong Value Entered ")
                print("Exiting Program")
                sys.exit()
            except NameError:
                print("Wrong Value Entered ")
                print("Exiting Program")
                sys.exit()                
        try:
            j = int(input("Enter the column ( 0 - "+str(self.n-1)+" ) : "))
            if j<0 or j>=self.n:
                    raise NameError("Out of Bounds")
        except ValueError:
            print("Wrong Value Entered ")
            try:
                j = int(input("Enter the column ( 0 - "+str(self.n-1)+" ) : "))
                if j<0 or j>=self.n:
                    raise NameError("Out of Bounds")
            except ValueError:
                print("Wrong Value Entered ")
                print("Exiting Program")
                sys.exit()
            except NameError:
                print("Wrong Value Entered ")
                print("Exiting Program")
                sys.exit()
        except NameError:
            print("Enter Value Between 0 - "+str(self.n-1))
            try:
                j = int(input("Enter the column ( 0 - "+str(self.n-1)+" ) : "))
                if j<0 or j>=self.n:
                    raise NameError("Out of Bounds")
            except ValueError:
                print("Wrong Value Entered ")
                print("Exiting Program")
                sys.exit()
            except NameError:
                print("Wrong Value Entered ")
                print("Exiting Program")
                sys.exit()
        if self.show[i,j] != -1:
            print("Already Open")
            self.playChance()
        else:
            if self.checkWin() == True:
                print("Congrats you have Completed...")
                self.showMines()
            else:
                if self.hide[i,j] != -1:
                    if self.hide[i,j] == 0 :
                        self.changeNeighbour(i,j)
                    self.show[i,j]=self.hide[i,j]
                    sleep(1)
                    clear()
                    self.showArea()
                    self.showMines()
                    self.playChance()
                else:
                    self.showMines()
                    print("Game Over")
a = Minesweeper(12,15)