# License
'''
Code by Gugulothu Yashwanth Naik
April 14,2020
Released under GNU GPL
'''


#Plots M and N circles with Nquist pot
import control
import matplotlib.pyplot as plt
import numpy as np
from pylab import*

#if using termux
#import subprocess
#import shlex
#end if

#M circle
def Circle_M(M):
	theta = np.linspace(0, 2*np.pi, 100)
	x=(M**2/(1-M**2))+((abs(M/(1-M**2)))*(np.cos(theta)))
	y=(abs(M/(1-M**2)))*(np.sin(theta))
	return x,y
	
#N circle	
def Circle_N(N):
	theta = np.linspace(0, 2*np.pi, 50)
	x=(-0.5)+(np.sqrt(0.25+(1/4*(N**2))))*np.cos(theta)
	y=(1/2*N)+(np.sqrt(0.25+(1/4*(N**2))))*np.sin(theta)
	return x,y



#plot of M circle and Nquist
subplot(2,1,1)
x,y=Circle_M(0.05)
plt.plot(x,y,label='M=0.15')

x,y=Circle_M(0.17)
plt.plot(x,y,label='M=0.17')


x,y=Circle_M(0.5)
plt.plot(x,y,label='M=0.5')

x,y=Circle_M(0.75)
plt.plot(x,y,label='M=0.75')

plt.axvline(x=-0.5,label='M=1')

x,y=Circle_M(1.15)
plt.plot(x,y,label='M=1.15')

x,y=Circle_M(1.35)
plt.plot(x,y,label='M=1.35')

x,y=Circle_M(1.85)
plt.plot(x,y,label='M=1.85')

x,y=Circle_M(2.25)
plt.plot(x,y,label='M=2.25')

x,y=Circle_M(2.75)
plt.plot(x,y,label='M=2.75')
num = [50,150]
den = [1,6,8,0]
G = control.tf(num,den) 
control.nyquist(G,label='Nyquist plot')
plt.grid(True)
plt.title('M Circles and Nquist plot')
plt.xlim(-4,4)
plt.xlabel('Real')
plt.ylim(-4,4)
plt.ylabel('Imaginary')
plt.legend(loc='best',prop={'size':11})





#plot of N circle and nquist
subplot(2,1,2)
x,y=Circle_N(-5)
plt.plot(x,y,label='N=-5')

x,y=Circle_N(-4)
plt.plot(x,y,label='N=-4')

x,y=Circle_N(-3)
plt.plot(x,y,label='N=-3')

x,y=Circle_N(-2)
plt.plot(x,y,label='N=-2')

x,y=Circle_N(-1)
plt.plot(x,y,label='N=-1')

x,y=Circle_N(1)
plt.plot(x,y,label='N=1')

x,y=Circle_N(2)
plt.plot(x,y,label='N=2')

x,y=Circle_N(3)
plt.plot(x,y,label='N=3')

x,y=Circle_N(4)
plt.plot(x,y,label='N=4')

x,y=Circle_N(5)
plt.plot(x,y,label='N=5')
num = [50,150]
den = [1,6,8,0]
G = control.tf(num,den) 
control.nyquist(G,label='Nyquist plot')
plt.grid(True)
plt.title('N Circles and Nquist plot')
plt.xlim(-4,4)
plt.xlabel('Real')
plt.ylim(-4,4)
plt.ylabel('Imaginary')
plt.legend(loc='best',prop={'size':11})

#if using termux
#plt.savefig('./figs/ee18btech11017/ee18btech11017.pdf')
#plt.savefig('./figs/ee18btech11017/ee18btech11017.eps')
#subprocess.run(shlex.split("termux-open ./figs/ee18btech11017/ee18btech11017.pdf"))

#else
plt.show()



