import pylab as pl
import math
class Pendulum :
    def __init__(self,time_step=0.0001,total_time=7, initial_vx=0,initial_vy=2*math.pi):
        
        self.x=[1]
        self.y=[0]
        self.time=total_time
        self.vx=[initial_vx]
        self.vy=[initial_vy]
        self.dt=time_step
        self.r=[1]
        self.theta=[0]
        self.t=[0]
        self.omega=[0]
        
    def run(self):
        _time=0
        while(_time<self.time):
            self.r.append(math.sqrt(self.x[-1]**2+self.y[-1]**2))
            self.omega.append(self.omega[-1]-12*(math.pi**2)*(self.x[-1]*math.sin(self.theta[-1])-self.y[-1]*math.cos(self.theta[-1]))*(self.x[-1]*math.cos(self.theta[-1])+self.y[-1]*math.sin(self.theta[-1]))*self.dt/self.r[-1]**5)
            self.vx.append(self.vx[-1]-4*self.x[-1]*self.dt*(math.pi**2)/self.r[-1]**3)
            self.vy.append(self.vy[-1]-4*self.y[-1]*self.dt*(math.pi**2)/self.r[-1]**3)
            self.x.append(self.x[-1]+self.vx[-1]*self.dt)
            self.y.append(self.y[-1]+self.vy[-1]*self.dt)
            a=self.theta[-1]+self.omega[-1]*self.dt
            if a<math.pi and a>-math.pi:
                self.theta.append(a)
            
            if a>=math.pi:
                b=a-2*math.pi
                self.theta.append(b)
            if a<=-math.pi:
                b=2*math.pi+a
                self.theta.append(b)
            self.t.append(self.t[-1]+self.dt)
            _time+=self.dt
            
    def show_results(self):
        
        pl.plot(self.t,self.omega,label='initialv=2pi')
        pl.legend(loc='upper right',frameon=True)
        pl.xlabel('time(yr)')
        pl.ylabel('omega')
        pl.xlim(0,8)
        pl.ylim(0,15)
        pl.title('Hyperion omega versus time')
               

r= Pendulum()
r.run()

r.show_results()


pl.show()

