# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 10:48:42 2020

@author: Vojtech Svarc, Palacký University Olomouc
"""
import numpy as np
import matplotlib.pyplot as plt

#functions for plotting

def zobr_faze(fi_bez,fi_mer,fi_stab,piezo,nazev_pro_ulozeni):  
    fig,ax = plt.subplots(figsize=(10,2.9))
    ax.set_xlabel('time (hours)',fontsize=velPisma)
    ax.set_ylabel("$\\varphi$ (degree)",fontsize=velPisma)
    pos=2000
    ax.plot(fi_bez[0]/3600,fi_bez[1])
    ax.plot((fi_mer[0]+pos)/3600+fi_bez[0][-1]/3600,fi_mer[1],color=barva_mer)
    ax.plot((fi_stab[0]+pos)/3600++fi_bez[0][-1]/3600,fi_stab[1],color=barva_stab)
    ax2 = ax.twinx()  #osa napeti
    ax2.set_ylabel("$\\varphi$ compensated (degree)",fontsize=velPisma)
    ax2.set_ylim(auto=True)
    ax2.plot((piezo[0]+fi_bez[0][-1]+pos)/3600,piezo[1],color="black") #7 je konverzni koeficient mezi monitorovacim a skutecnym piezo napetim          
    ax.set_ylim(-10,190)
    ax.set_yticks([0, 30, 60, 90, 120, 150, 180])
    plt.show()
    if(save==1):
        fig.savefig(nazev_pro_ulozeni+".pdf",bbox_inches="tight",format="pdf")

def zobr_fft(fft_mer,fft_stab,fft_piezo,nazev_pro_ulozeni):
    fig,ax = plt.subplots(figsize=(4.3,2.9))
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlabel('$f$ $\mathrm{(Hz)}$',fontsize=velPisma)                            
    ax.set_ylabel('spectral power density',fontsize=velPisma)
    norm=np.mean(fft_piezo[1][1:2])
    #ax.plot(fft_bez[0],fft_bez[1]/norm)
    ax.plot(fft_mer[0],fft_mer[1]/norm,color=barva_mer)
    ax.plot(fft_stab[0],fft_stab[1]/norm,color=barva_stab)
    ax.plot(fft_piezo[0],fft_piezo[1]/norm,color="black")
    ax.set_xlim(pow(10,-5),8)
    ax.set_ylim(pow(10,-17.5),pow(10,1))
    plt.show()
    if(save==1):
        fig.savefig(nazev_pro_ulozeni+".pdf",bbox_inches="tight",format="pdf")   
     

def zobr_allan(all_mer,all_stab,all_piezo,all_sum,nazev_pro_ulozeni):
    fig,ax = plt.subplots(figsize=(4.3,2.9))
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlabel('$\\tau\\,(s)$',fontsize=velPisma)                            
    ax.set_ylabel('Allan deviation (deg)',fontsize=velPisma)
    ax.plot(all_mer[0],all_mer[1],color=barva_mer)
    ax.plot(all_stab[0],all_stab[1],color=barva_stab)
    ax.plot(all_piezo[0],all_piezo[1],color="black")
    ax.plot(all_sum[0],all_sum[1],color="gray",linestyle="dashed")
    ax.set_xlim(10,18000)
    plt.show()
    if(save==1):
        fig.savefig(nazev_pro_ulozeni+".pdf",bbox_inches="tight",format="pdf")

#main code_______________________________________________________________________
   

#set global parameters
velPisma=12                 #fontsize
save=0                      #if save=0 figs are not saved. If save=1, all figs are saved            
barva_mer="#d3812dff"       #color of the signal
barva_stab="#960000ff"      #color of the reference


#Fig 4a - stability in the time domain
#load data
Fig4aBlue=np.load("Fig4aBlue.npy")
Fig4aOrange=np.load("Fig4aOrange.npy")
Fig4aRed=np.load("Fig4aRed.npy")
Fig4aBlack=np.load("Fig4aBlack.npy")
#show plot
zobr_faze(Fig4aBlue,Fig4aOrange,Fig4aRed,Fig4aBlack,"Fig4a")
   
#Fig 4b - spectral analysis
#load data
Fig4bOrange=np.load("Fig4bOrange.npy")
Fig4bRed=np.load("Fig4bRed.npy")
Fig4bBlack=np.load("Fig4bBlack.npy")
#show plot
zobr_fft(Fig4bOrange,Fig4bRed,Fig4bBlack,"Fig4b")

#Fig 4c - Allan deviation
Fig4cOrange=np.load("Fig4cOrange.npy")
Fig4cRed=np.load("Fig4cRed.npy")
Fig4cBlack=np.load("Fig4cBlack.npy")
Fig4cGray=np.load("Fig4cGray.npy")
#show plot
zobr_allan(Fig4cOrange,Fig4cRed,Fig4cBlack,Fig4cGray,"Fig4c")

