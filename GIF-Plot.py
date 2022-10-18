#from turtle import color
import pkg_resources
import pickle

pkg_resources.require('pythera==0.3.1')
import pythera
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rcParams
import imageio
import os


rcParams['font.family'] = 'serif'
rcParams['font.sans-serif'] = ['DejaVu Sans']
rcParams['font.size'] = 14
hc = 4.135667696e-15*3e8 #eV m

### load pozo ###
with open('pozo.pkl', 'rb') as f:
    z,conduction_band_profile = pickle.load(f)

### Electric field in kV/cm ###
EF_ = 44
TEMPERATURE = np.arange(5, 120, 5)

print("p1b")
### Grafico la emisión de p1b para distintos T ###
for n in range(len(TEMPERATURE)):
    with open('e2b-p1b-3p-{}'.format(EF_)+'-T'+str(TEMPERATURE[n])+'.pickle', 'rb') as f:
        energias_p1b_e2b = pickle.load(f)
    #print(energias_p1b_e2b[0,:])
    with open('3p-EF'+str(EF_)+'-T'+str(TEMPERATURE[n])+'-p1b.pickles', 'rb') as f:
        x,dens,energy = pickle.load(f)
    plt.plot((z-z[len(z)//2]),conduction_band_profile-EF_/10000* (z-z[len(z)//2]))
    ### plot each f0 ###
    for i in range(x.shape[0]):
        color = '0.5'
        if i in energias_p1b_e2b[0,:]:
           color ='r'
        plt.plot(x[i,:]-x[i,x.shape[1]//2],dens[i]+energy[i],color=color)
    plt.xlabel("Distancia [nm]")
    plt.ylabel("Energía [eV]")
    plt.xlim(-40,40)
    plt.ylim(0.5,1.2)
    plt.text(10,1.1,'T = '+str(TEMPERATURE[n])+' K\np1b')
    plt.title(r"GaAs/Al$_{{0.33}}$Ga$_{{0.66}}$As")
    plt.tick_params(axis='both',direction='in')
    plt.savefig('3p-EF'+str(EF_)+'-T'+str(TEMPERATURE[n])+'-p1b.png',bbox_inches='tight')
    #close
    plt.clf()
    

### Grafico la emisión de e2b para distintos EF ###
print("e2b")
for n in range(len(TEMPERATURE)):
    with open('e2b-p1b-3p-{}'.format(EF_)+'-T'+str(TEMPERATURE[n])+'.pickle', 'rb') as f:
        energias_p1b_e2b = pickle.load(f)
    with open('3p-EF'+str(EF_)+'-T'+str(TEMPERATURE[n])+'-e2b.pickles', 'rb') as f:
        x,dens,energy = pickle.load(f)
    #print(energias_p1b_e2b[0,:,0])
    plt.plot((z-z[len(z)//2]),conduction_band_profile-EF_/10000* (z-z[len(z)//2]))
    ### plot each f0 ###
    for i in range(x.shape[0]):
        color = '0.5'
        if i in energias_p1b_e2b[1,:]:
           color ='r'
        plt.plot(x[i,:]-x[i,x.shape[1]//2],dens[i]+energy[i],color=color)
    plt.xlabel("Distancia [nm]")
    plt.ylabel("Energía [eV]")
    plt.xlim(-40,40)
    plt.ylim(0.5,1.2)
    plt.text(10,1.1,'T = '+str(TEMPERATURE[n])+' K\ne2b')
    plt.title(r"GaAs/Al$_{{0.33}}$Ga$_{{0.66}}$As")
    plt.tick_params(axis='both',direction='in')
    plt.savefig('3p-EF'+str(EF_)+str(TEMPERATURE[n])+'-e2b.png',bbox_inches='tight')
    plt.clf()
    
### GIF T variation ###

images = []
for n in range(len(TEMPERATURE)):
    images.append(imageio.imread('3p-EF'+str(EF_)+'-T'+str(TEMPERATURE[n])+'-p1b.png'))
kargs = { 'duration': 0.5 }
imageio.mimsave('3p-EF'+str(EF_)+'T'+str(TEMPERATURE[0])+'-'+str(TEMPERATURE[len(TEMPERATURE)-1])+'-p1b.gif', images,**kargs)




images = []

for n in range(len(TEMPERATURE)):
    images.append(imageio.imread('3p-EF'+str(EF_)+str(TEMPERATURE[n])+'-e2b.png'))
kargs = { 'duration': 0.5 }
imageio.mimsave('3p-EF'+str(EF_)+'T'+str(TEMPERATURE[0])+'-'+str(TEMPERATURE[len(TEMPERATURE)-1])+'-e2b.gif', images,**kargs)
