# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 17:50:08 2021

@author: Administrator
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation,FFMpegWriter 
import seaborn as sns  

def create_geometric_series(start,number,factor):
    number_list = np.arange(number)
    return_list = [start*factor**(i) for i in number_list]
    return return_list

x = 30
xlist = np.linspace(-x,x,100)
t = 0.1
#tlist = np.linspace(0.001,t,20)
tlist = [0.001,0.0011,0.0014,0.002,0.0025,0.003,0.004,0.01,0.02,0.04]
num = len(tlist)
lambda671 = 671e-9
boffset = 10
def cir_el(r):
    a,b = 0.0,boffset
    theta = np.arange(0,2*np.pi,0.01)
    rx = a + r * np.cos(theta)
    ry = b + r * np.sin(theta)
    return rx,ry

oemga = 1/np.sqrt(lambda671 * tlist[0])
y = 1/2 * oemga**2*xlist**2 /1e9
theta = np.arange(0,2*np.pi,0.01)
r = 0.1
rx = 0 + r * np.cos(theta)
ry = boffset + r * np.sin(theta)

oemga = 1/np.sqrt(lambda671 * tlist[0])
y = 1/2 * oemga**2*xlist**2 /1e9

sns.set_style("whitegrid") 


fig, ax = plt.subplots()
fig.set_tight_layout(True)


ax.scatter(0, 0,s = 30000,c = "r")
ax.xaxis.set_major_locator(plt.NullLocator())
ax.yaxis.set_major_locator(plt.NullLocator())
ax.plot(xlist, y,'b-')
ax.plot(rx, ry,'r.')
#a = ax.scatter(x[0], y[0],s = 100,c = "g")
frames=np.arange(0, 100)

def update(i):
    ax.cla()
    i = - i - 1
    rx,ry = cir_el(frames[i]*0.05 + 0.05)
    rx = rx*5
    plt.ylim((0 ,30))
    plt.xlim((-30, 30))
    ax.xaxis.set_major_locator(plt.NullLocator())
    ax.yaxis.set_major_locator(plt.NullLocator())
    oemga = 1/np.sqrt(lambda671)*(frames[i]*0.001+0.001)
    y = 1/2 * oemga**2*xlist**2
    ax.plot(xlist, y,'b-')
    rx_step = rx[0::round(len(rx)/20)]
    ry_step = ry[0::round(len(ry)/20)]
    ax.plot(rx_step, ry_step,'r',linestyle = 'dashed')
    ax.fill_between(rx,ry,facecolor = 'red',alpha = 0.5)

    return ax

anim = FuncAnimation(fig, update,frames , interval=100)
writer = FFMpegWriter()
anim.save('Liatom2.gif', writer='imagemagick', fps=30)
