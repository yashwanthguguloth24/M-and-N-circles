# License
'''
Code by Gugulothu Yashwanth Naik
April 14,2020
Released under GNU GPL
'''

from scipy import signal
import matplotlib.pyplot as plt
from pylab import*

#if using termux
#import subprocess
#import shlex
#end if

#closed loop transfer function
s1 = signal.lti([50,150],[1,6,58,150])
w, mag, phase = signal.bode(s1)



subplot(2,1,1)
plt.semilogx(w, mag,label='original plot of CLTF')
plt.ylabel('Mag(dB)')
plt.title('Magnitude plot')
plt.grid() 


#data points from intersection
x=[2.95,5.18,5.96,6.87,7.91,9.1,10.48,18.42,21.21,24.42,32.37]
y=[1.58,5.34,7.04,7.78,5.10,1.21,-2.49,-15.39,-17.72,-20.91,-26.02]
plt.plot(x,y,'r',label='plot using M circles')
plt.legend()



subplot(2,1,2)
plt.semilogx(w, phase) 
plt.grid()     # Bode phase plot
plt.xlabel('Frequency(rad/s)')
plt.ylabel('Phase(deg)')
plt.title('Phase plot')

#if using termux
#plt.savefig('./figs/ee18btech11017/ee18btech11017.pdf')
#plt.savefig('./figs/ee18btech11017/ee18btech11017.eps')
#subprocess.run(shlex.split("termux-open ./figs/ee18btech11017/ee18btech11017.pdf"))

#else
plt.show()

