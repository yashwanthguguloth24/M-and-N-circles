# License
'''
Code by Gugulothu Yashwanth Naik
April 30,2020
Released under GNU GPL
'''


import control
import math
import numpy as np


#if using termux
#import subprocess
#import shlex
#end if

def Circle_M(M):
	theta = np.linspace(0, 2*np.pi,400000)
	x = np.around((M**2/(1-M**2))+((abs(M/(1-M**2)))*(np.cos(theta))),decimals=2)
	y = np.around((abs(M/(1-M**2)))*(np.sin(theta)),decimals=2)			# Rounding Off
	x = np.expand_dims(x,axis=1)
	y = np.expand_dims(y,axis=1)
	Z = np.append(x,y,axis=1)
	return Z
	
def Circle_N(n):
  theta = np.linspace(0, 2*np.pi, 40000)
  x0 = -0.5
  y0 = 1/(2*n)
  r = np.sqrt((1/4) + (1/(4*n**2)))
  x = np.around(x0 + r*np.cos(theta),decimals=3)
  y = np.around(y0 + r*np.sin(theta),decimals=3)  #rounding off
  x = np.expand_dims(x,axis=1)
  y = np.expand_dims(y,axis=1)
  Z = np.append(x,y,axis=1)
  return Z
  
  
#Defining intersection function
def Intersection(A):
	nrows, ncols = A.shape
	dtype={'names':['f{}'.format(i) for i in range(ncols)],
		   'formats':ncols * [A.dtype]}
	
	return A.view(dtype)


#M circle intersection
num = [50,150]
den = [1,6,8,0]


G = control.tf(num,den)
w = np.logspace(-3,3,1000)
Real,Imag,Freq = np.around(control.nyquist(G,w),decimals=2) 			# Rounding Off
NyQ_Data = np.append(np.expand_dims(Real,axis=1), np.expand_dims(Imag,axis=1), axis=1)

M = list(np.arange(0.01,5,0.3))

#finds intersection points and return M and frequency
def Extract(M,NyQ_Data,Freq):
	Output = []
	for m in M:
		Circle_Data = list(Intersection(Circle_M(m)))
		ND = list(Intersection(NyQ_Data))
		Int = np.intersect1d(Circle_Data,ND)
		for p in Int:
			ind = ND.index(p)
			f = Freq[ind]
			Output.append([m,f])
			
	return Output

print ('The values of M,f are',Extract(np.around(M,decimals=2),NyQ_Data,Freq))	#prints(M,frequency)
	



#N circle intersection

w = np.linspace(0.1,100,10000)
Real,Imag,Freq = np.around(control.nyquist(G,w),decimals=3) 			# Rounding Off
NyQ_Data = np.append(np.expand_dims(Real,axis=1), np.expand_dims(Imag,axis=1), axis=1)


#finds intersection points and return N and frequency	
N = list(np.arange(-5,5,0.3))
def Extract1(N,NyQ_Data,Freq):
	Output = []
	for n in N:
		Circle_Data = list(Intersection(Circle_N(n)))
		ND = list(Intersection(NyQ_Data))
		Int = np.intersect1d(Circle_Data,ND)
		for p in Int:
			ind = ND.index(p)
			f = Freq[ind]
			Output.append([n,f])
			
	return Output
	
print ('The values of N,f are',Extract1(np.round(N,decimals=2),NyQ_Data,Freq))	#prints(N,frequency)
	









