# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 11:03:41 2021

@author: HCI
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation,FFMpegWriter

plt.rcParams['font.family']=['SimHei']

boffset = 3
rxscale = 1
ryscale = 1

gif_xy = 1
gif_x_lim = 5
gif_y_lim = 10
ion_crystal_width = 2
ion_line_space = 0.5
def create_geometric_series(start,number,factor):
    number_list = np.arange(number)
    return_list = [start*factor**(i) for i in number_list]
    return return_list

def cir_el(r):
    a,b = 0.0,0.0
    theta = np.arange(0,2*np.pi,0.01)
    rx = a + r * np.cos(theta)
    ry = b + r * np.sin(theta)
    rx,ry = rx/rxscale,ry/ryscale
    return rx,ry

def per_array(xarray,yarray,scale_x,scale_y):
    scale_x = scale_x
    scale_y = scale_y
    scale_x_ar = np.random.rand(len(xarray))*scale_x + xarray
    scale_y_ar = np.random.rand(len(yarray))*scale_y + yarray
    return scale_x_ar,scale_y_ar
def creat_r(t):
    return 

def creat_r_re(t):
    return 
# sns.set_style("whitegrid")
#creat a canvas
fig = plt.figure()
ax = fig.add_subplot(1,1,1)

frames=np.arange(0, 200) # Set a time scale with a pixel units
time_scale = len(frames) # the frame number of video file with a gif format . 
t_list = np.linspace(0,0.01,time_scale+1) # the time serise of Li atom evalution.
switch_time = np.arange(0,10,1)
switch_start_time = 30
time_line = 0
back_time = 0
def update(i):
    global time_line
    global back_time
    """clear canvas"""
    ax.cla()
    ax.set_ylim((0,gif_y_lim))
    ax.set_xlim((-gif_x_lim,gif_x_lim))
    
    x_cool1 = np.linspace(-ion_crystal_width,ion_crystal_width,10)
    x_cool1,ycool1 = per_array(x_cool1,np.zeros(len(x_cool1))+5,0.1,0.1)
    
    x_cool2 = np.linspace(-ion_crystal_width+0.2,2-0.2,9)
    x_cool2,ycool2 = per_array(x_cool2,np.zeros(len(x_cool2)) + ion_line_space + 5,0.1,0.1)
    
    x_cool3 = np.linspace(-ion_crystal_width+0.2,2-0.2,9)
    x_cool3,ycool3 = per_array(x_cool3,np.zeros(len(x_cool3)) - ion_line_space + 5,0.1,0.1)
    
    x_cool4 = np.linspace(-ion_crystal_width+0.4,2-0.4,7)
    x_cool4,ycool4 = per_array(x_cool4,np.zeros(len(x_cool4)) + 2*ion_line_space + 5,0.1,0.1)
    
    x_cool5 = np.linspace(-ion_crystal_width+0.4,2-0.4,7)
    x_cool5,ycool5 = per_array(x_cool5,np.zeros(len(x_cool5)) - 2*ion_line_space + 5,0.1,0.1)

    x_cool6 = np.linspace(-ion_crystal_width+0.6,2-0.6,5)
    x_cool6,ycool6 = per_array(x_cool6,np.zeros(len(x_cool6)) + 3*ion_line_space + 5,0.1,0.1)
    
    x_cool7 = np.linspace(-ion_crystal_width+0.6,2-0.6,5)
    x_cool7,ycool7 = per_array(x_cool7,np.zeros(len(x_cool7)) - 3*ion_line_space + 5,0.1,0.1)
    
    ax.scatter(x_cool1,ycool1,color = "blue")
    ax.scatter(x_cool2,ycool2,color = "blue")
    ax.scatter(x_cool3,ycool3,color = "blue")
    ax.scatter(x_cool4,ycool4,color = "blue")
    ax.scatter(x_cool5,ycool5,color = "blue")
    ax.scatter(x_cool6,ycool6,color = "blue")
    ax.scatter(x_cool7,ycool7,color = "blue")
    para_x = np.linspace(-gif_x_lim+1,gif_x_lim-1,100)
    para_y = 5/8*para_x**2 + 2
    if i in switch_time + switch_start_time:
        para_y2 = para_y
        para_y2[65::]  = para_y2[65]
    else:
        para_y2 = para_y
    if i > switch_start_time:
        position = np.linspace(-2,2,len(frames) - 20)
        position_re = position[::-1]
        if (time_line + switch_start_time) < len(position_re):
            ax.scatter(position_re[time_line%len(position_re)],gif_y_lim/2+np.random.rand(1)-0.5,s=80,color = "g")
            time_line = time_line + 1
            ax.scatter(position_re[(time_line+3)%len(position_re)],gif_y_lim/2+np.random.rand(1)-0.5,s=80,color = "g")
        else:
            x_back = np.linspace(position_re[time_line%len(position_re)],0,10)
            y_back = gif_y_lim/2+np.random.rand(1)-0.5
            if back_time > len(x_back)-1:
                ax.scatter(-0.1*np.random.rand(1),gif_y_lim/2+np.random.rand(1)*0.5-0.5,s=80,color = "g")
                ax.scatter(0.1*np.random.rand(1),gif_y_lim/2+np.random.rand(1)*0.5-0.5,s=80,color = "g")
            else:
                ax.scatter(x_back[back_time],y_back,s=80,color = "g")
                ax.scatter(x_back[back_time],y_back,s=80,color = "g")
                back_time += 1
    else:
        ax.scatter(gif_x_lim -1 +np.random.rand(1)*0.5,5,s=80,color = "g")
        ax.scatter(gif_x_lim+np.random.rand(1)*0.5-1.5,5,s=80,color = "g")
    x = np.linspace(-gif_x_lim-1,gif_x_lim+1,20)/1
    y = -0.04 * x**2 - 0.05 *x
    y2 = 0.04 * x**2 + 0.05 *x
    thetda = 1/4 * np.pi
    # x1 = x*np.cos(thetda) - y*np.sin(thetda)
    y1 = x*np.sin(thetda) + y*np.cos(thetda) + gif_y_lim/2 - 1
    
    # x2 = x*np.cos(thetda) - y2*np.sin(thetda)
    y22 = x*np.sin(thetda) + y2*np.cos(thetda) + gif_y_lim/2 + 1
    # ax.plot(x1,y1)
    # ax.plot(x2,y22)
    x_green = np.linspace(-gif_x_lim,gif_x_lim,20)
    g_high = 0.02 * x_green**2  + 5.5
    g_low = -0.02 * x_green**2  + 4.5
    ax.fill_between(x,g_high,g_low,color = 'green',alpha = 0.2)
    ax.fill_between(x,y1,y22,color = 'purple',alpha = 0.2)
    ax.plot(para_x,para_y2,color = 'red',alpha = 1)
    
    # para_x_2 = np.linspace(-gif_x_lim,gif_x_lim,100)
    # para_y_2 = 4*para_x**2 + 2
    # ax.plot(para_x_2[56::],para_y_2[56::],'.',color = 'red',alpha = 1)
    # ax.plot(para_x_2[0:55],para_y_2[0:55],'-',color = 'red',alpha = 1)
    """文字与箭头标注"""
    arrow_fontsize = 16
    ax.spines['right'].set_color('none')
    ax.spines['left'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.spines['bottom'].set_color('none')
    ax.xaxis.set_major_locator(plt.NullLocator())
    ax.yaxis.set_major_locator(plt.NullLocator())
    ax.text(-gif_x_lim,1,"313 nm",color = 'purple',fontsize = 16,fontweight = "bold")
    ax.text(-gif_x_lim,5,"548.5 nm",color = 'green',fontsize = 16,fontweight = "bold")
    ax.arrow(0, 1, 0, 1,width=0.2,color = 'blue')
    ax.text(-0.5,0,"$\mathregular{Be^+}$ 离子",color = 'red',fontsize = arrow_fontsize,fontweight = "bold")
    ax.arrow(gif_x_lim, 4, -1, 0,width=0.2,color ="green")
    ax.text(gif_x_lim-1.5,3,"$\mathregular{Li^+}$ 离子",color = 'green',fontsize = arrow_fontsize,fontweight = "bold")
    ax.grid(False)
    ax.arrow(3, 1, -1, 2,width=0.1,color = 'red')
    ax.text(3,1,"离子阱",color = 'black',fontsize = arrow_fontsize,fontweight = "bold")
    
    ax.text(0,9,"示意图",color = 'black',fontsize = 20,fontweight = "bold",ha = "center")
    return ax

# creat a anim file
anim = FuncAnimation(fig, update,frames , interval=100)
writer = FFMpegWriter()
# save the file with gif format, where the fps parameter set the number of frame percent second.
anim.save('sd_chinese.gif', writer='imagemagick', fps=10)