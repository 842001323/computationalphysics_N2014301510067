import math
import pylab as pl
import random
class randomwalk:
    def __init__(self):
        self.x=[]
        self.y=[]
        for i in range(500001):
            self.x.append([])
            self.y.append([])
        for i in range(400):
            self.x[0].append(random.randint(-5,5))
            self.y[0].append(random.randint(-5,5))
        for i in range(500001):
            for j in range(400):
                self.x[i].append(0)
                self.y[i].append(0)
    def run(self):
        for i in range(500001):
            a=random.random(0,1)
            if a>0.5:
                b=random.randint(0,399)
                c=random.random(0,1)
                if c>0.5:
                    self.x[i][b]=self.x[i-1][b]-1
                else:
                    self.x[i][b]=self.x[i-1][b]+1
                if b>0 and b<399:
                    for j in range(0,b):
                        self.x[i][j]=self.x[i-1][j]
                    for j in range(b+1,400):
                        self.x[i][j]=self.x[i-1][j]
                else:
                    if b==0:
                        for j in range(1,400):
                            self.x[i][j]=self.x[i-1][j]
                    else:
                        for j in range(0,399):
                            self.x[i][j]=self.x[i-1][j]
                for j in range(400):
                    self.y[i][j]=self.y[i][j]
            else:
                b=random.randint(0,399)
                c=random.random(0,1)
                if c>0.5:
                    self.y[i][b]=self.y[i-1][b]-1
                else:
                    self.y[i][b]=self.y[i-1][b]+1
                if b>0 and b<399:
                    for j in range(0,b):
                        self.y[i][j]=self.y[i-1][j]
                    for j in range(b+1,400):
                        self.y[i][j]=self.y[i-1][j]
                else:
                    if b==0:
                        for j in range(1,400):
                            self.y[i][j]=self.y[i-1][j]
                    else:
                        for j in range(0,399):
                            self.y[i][j]=self.y[i-1][j]
                for j in range(400):
                    self.x[i][j]=self.x[i][j]
