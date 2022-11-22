# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 16:02:38 2016

@author: Vojtech Svarc, Palacký University Olomouc
"""

import numpy as np
import matplotlib.pyplot as plt
dataFig5a=np.load("data_Fig5a.npy") #dataset for Fig 5a in format [time (s), transmittance, reflectance]"
dataFig5b=np.load("data_Fig5b.npy") #dataset for Fig 5a in format [time (min), transmittance, reflectance]"

#global graph settings
m=0.42
x_dimension=4.3
y_dimension=2.9
markersize=0.7
barva1="#101050"      #color for T
barva2="#c00000"      #color for R
fsize=11                #fontsize         

#Fig 5a
fig,axes = plt.subplots(figsize=(x_dimension,y_dimension))
axes.set_xlim(0,27)
axes.set_ylim(-0.03,1.03) 
plt.xticks(np.linspace(0,27,10))
popisek_x=('time (min)')                   
popisek_y=('relative intensity') 
axes.set_xlabel(popisek_x,fontsize=fsize)
axes.set_ylabel(popisek_y,fontsize=fsize)                           
axes.plot(dataFig5a[0]/60,dataFig5a[1],linewidth=0.5*m,linestyle="",color=barva1,marker=".",markersize=markersize)    
axes.plot(dataFig5a[0]/60,dataFig5a[2],linewidth=0.5*m,linestyle="",color=barva2,marker=".",markersize=markersize)                                                                       
#fig.savefig("Fig5a.pdf",bbox_inches="tight")

#Fig 5b
fig,axes = plt.subplots(figsize=(x_dimension*15/27,y_dimension))
axes.set_xlim(0,15)
axes.set_ylim(-0.02,1.05)
axes.set_xlabel('time (min) ',fontsize=fsize)
axes.set_ylabel('norm. counts',fontsize=fsize)
axes.set_xticks([0, 3, 6, 9, 12 ,15 ])                           
axes.plot(dataFig5b[0],dataFig5b[1],linewidth=0.5*m,linestyle="",color=barva1,marker=".",markersize=markersize)    
axes.plot(dataFig5b[0],dataFig5b[2],linewidth=0.5*m,linestyle="",color=barva2,marker=".",markersize=markersize)
#fig.savefig("Fig5b.pdf",bbox_inches="tight")