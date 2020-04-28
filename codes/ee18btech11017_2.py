# License
'''
Code by Gugulothu Yashwanth Naik
April 14,2020
Released under GNU GPL
'''
import numpy as np
import matplotlib.pyplot as plt
import control
import math

#if using termux
#import subprocess
#import shlex
#end if



#M circle
def Circle(M):
	theta = np.linspace(0, 2*np.pi,400)
	x=np.around((M**2/(1-M**2))+((abs(M/(1-M**2)))*(np.cos(theta))),decimals=2)
	y=np.around((abs(M/(1-M**2)))*(np.sin(theta)),decimals=2)
	C=abs(M/(1-M**2))
	return x,y


#nquist 
num = [50,150]
den = [1,6,8,0]

G = control.tf(num,den) 
niq=np.around(control.nyquist(G,Plot=0),decimals=2) #rounding

#magnitude M
mag=np.empty(0)
#frequency
freq=np.empty(0)


#computation
m=np.arange(0.05,8.05,0.05)
for M in m:
	if (M!=1):
		for i in range (len(niq[0])):
			for j in range (len(Circle(M)[0])):
				if (niq[0][i]== Circle(M)[0][j] and niq[1][i]== Circle(M)[1][j]):
					mag=np.append(mag,M)
					freq=np.append(freq,niq[2][i])
		            

#intersection of M at different frequencies
print('The values of M are ',mag)
print('corresponding frequencies',freq)


#N circle
def Circle(N):
	theta = np.linspace(0, 2*np.pi, 100)
	x=np.around((-0.5)+(np.sqrt(0.25+(1/4*(N**2))))*np.cos(theta),decimals=2)
	y=np.around((1/2*N)+(np.sqrt(0.25+(1/4*(N**2))))*np.sin(theta),decimals=2)
	return x,y


#computation	
mag=np.empty(0)
freq=np.empty(0)

m=np.arange(-2,2,0.01)
for N in m:
	if N!=1:
		for i in range (len(niq[0])):
			for j in range (len(Circle(N)[0])):
				if (niq[0][i]== Circle(N)[0][j] and niq[1][i]== Circle(N)[1][j]):
					mag=np.append(mag,N)
					freq=np.append(freq,niq[2][i])
					
p=np.zeros(len(mag))					
for i in range (len(mag)):
	p[i]=math.degrees(math.atan(mag[i]))

#intersection of N at different frequencies	
print('The phase in degrees',p)
print('corresponding frequencies',freq)		









