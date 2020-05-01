# License
'''
Code by Gugulothu Yashwanth Naik
April 30,2020
Released under GNU GPL
'''


import numpy as np
import matplotlib.pyplot as plt
from pylab import*

#if using termux
#import subprocess
#import shlex
#end if


subplot(2,1,1)
x=[5.08,5.67,6.34,6.88,6.98,7.08,7.58,7.9,8.02,9.86,11.17,14.33,57.91]
y=[5.15,6.8,7.64,7.64,7.64,7.64,6.48,5.15,5.15,-0.81,-4.29,-10.17,-40]
plt.plot(x,y)
plt.xlim(5,60)
plt.ylabel('Mag(dB)')
plt.title('Magnitude plot')
plt.grid() 

subplot(2,1,2)
x=[5.425,6.045,6.314,6.404,6.524,6.634,6.724,7.323,7.503,7.713,7.833,7.993,8.243,8.642,9.432,11.68,28.335,34.569,46.019]
y=[-38.65,-54.46,-63.4,-66.5,-70.97,-75.25,-78.6,-101.5,-106.85,-114.4,-117.7,-122,-127.5,-135,-145,-158.19,-174.28,-174.28,-174.28]
plt.plot(x,y)
plt.xlim(5,47)
plt.xlabel('frequency(rad/s)')
plt.ylabel('Phase(deg)')
plt.title('Phase plot')
plt.grid() 

#if using termux
#plt.savefig('./figs/ee18btech11017/ee18btech11017_fig2.pdf')
#plt.savefig('./figs/ee18btech11017/ee18btech11017_fig2.eps')
#subprocess.run(shlex.split("termux-open ./figs/ee18btech11017/ee18btech11017_fig2.pdf"))

#else

plt.show()
