import math
import pylab as pl
import random
class randomwalk:
    def __init__(self,t=30):
        self.dt=0.5
        self.x=[]
        self.y=[]
        self.tt=t
        for i in range(100):
            self.x.append([])
            self.y.append([])
        for i in range(101):
            self.x[0].append(i-50)
            self.y[0].append(0)
        self.y[0][50]=1
    def run(self):
        a=self.tt*2+1
        for i in range(1,a):
            self.x[i].append(-50)
            self.y[i].append((self.y[i-1][1])*0.5)
            for j in range(1,100):
                self.x[i].append(j-50)
                self.y[i].append((self.y[i-1][j-1]+self.y[i-1][j+1])*0.5)
            self.x[i].append(50)
            self.y[i].append((self.y[i-1][-2])*0.5)
    def result(self):
        ax1=pl.subplot(321)
        ax2=pl.subplot(322)
        ax3=pl.subplot(323)
        ax4=pl.subplot(324)
        ax5=pl.subplot(325)
        ax6=pl.subplot(326)
        pl.sca(ax1)
        pl.plot(self.x[0],self.y[0],label='t=0')
        pl.title('Diffusion in one dimension',fontsize=14)
        pl.xlabel('x',fontsize=14)
        pl.xlim(-50,50)
        pl.ylabel('density',fontsize=14)
        pl.legend(fontsize=14,loc='best')
        pl.sca(ax3)
        pl.plot(self.x[0],self.y[5],label='t=2.5')
        pl.title('Diffusion in one dimension',fontsize=14)
        pl.xlabel('x',fontsize=14)
        pl.xlim(-50,50)
        pl.ylabel('density',fontsize=14)
        pl.legend(fontsize=14,loc='best')
        pl.sca(ax5)
        pl.plot(self.x[0],self.y[10],label='t=5')
        pl.title('Diffusion in one dimension',fontsize=14)
        pl.xlabel('x',fontsize=14)
        pl.xlim(-50,50)
        pl.ylabel('density',fontsize=14)
        pl.legend(fontsize=14,loc='best')
        pl.sca(ax2)
        pl.plot(self.x[0],self.y[15],label='t=7.5')
        pl.title('Diffusion in one dimension',fontsize=14)
        pl.xlabel('x',fontsize=14)
        pl.xlim(-50,50)
        pl.ylabel('density',fontsize=14)
        pl.legend(fontsize=14,loc='best')
        pl.sca(ax4)
        pl.plot(self.x[0],self.y[30],label='t=15')
        pl.title('Diffusion in one dimension',fontsize=14)
        pl.xlabel('x',fontsize=14)
        pl.xlim(-50,50)
        pl.ylabel('density',fontsize=14)
        pl.legend(fontsize=14,loc='best')
        pl.sca(ax6)
        pl.plot(self.x[0],self.y[40],label='t=20')
        pl.title('Diffusion in one dimension',fontsize=14)
        pl.xlabel('x',fontsize=14)
        pl.xlim(-50,50)
        pl.ylabel('density',fontsize=14)
        pl.legend(fontsize=14,loc='best')
b =randomwalk()
b.run()
b.result()
pl.show()
