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

### Electric field in kV/cm ###
EF_ = 44
periodos = np.arange(1, 30, 2)


### Load relevant energies e2b p1b ###

#energias_p1b_e2b = np.array([np.loadtxt('e2b-p1b-3p-'+str(EF_[n])+'.txt') for n in range(len(EF_))])

print("p1b")
### Grafico la emisión de p1b para distintos EF ###
for n in range(len(periodos)):
    with open(f'e2b-p1b-{periodos[n]}p-EF{EF_}.pickle', 'rb') as f:
        energias_p1b_e2b = pickle.load(f)
    #print(energias_p1b_e2b[0,:])
    with open(str(periodos[n])+"p-EF"+str(EF_)+'-p1b.pickles', 'rb') as f:
        x,dens,energy = pickle.load(f)
    with open('pozo.pkl', 'rb') as f:
        z,conduction_band_profile = pickle.load(f)
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
    plt.ylim(0.5,1.3)
    plt.text(10,1.2,'# periodos = '+str(periodos[n]))
    plt.title(r"GaAs/Al$_{{0.33}}$Ga$_{{0.66}}$As")
    plt.tick_params(axis='both',direction='in')
    plt.savefig(str(periodos[n])+'p-EF'+str(EF_)+'-p1b.png',bbox_inches='tight')
    plt.clf()

### Grafico la emisión de e2b para distintos EF ###
print("e2b")
for n in range(len(periodos)):
    with open(f'e2b-p1b-{periodos[n]}p-EF{EF_}.pickle', 'rb') as f:
        energias_p1b_e2b = pickle.load(f)
    #print(energias_p1b_e2b[0,:])
    with open(str(periodos[n])+"p-EF"+str(EF_)+'-e2b.pickles', 'rb') as f:
        x,dens,energy = pickle.load(f)
    with open('pozo.pkl', 'rb') as f:
        z,conduction_band_profile = pickle.load(f)
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
    plt.ylim(0.5,1.3)
    plt.text(10,1.2,'#periodos = '+str(periodos[n]))
    plt.title(r"GaAs/Al$_{{0.33}}$Ga$_{{0.66}}$As")
    plt.tick_params(axis='both',direction='in')
    plt.savefig(str(periodos[n])+'p-EF'+str(EF_)+'-e2b.png',bbox_inches='tight')
    plt.clf()
    
### GIF ###

images = []
for n in range(len(periodos)):
    images.append(imageio.imread(str(periodos[n])+'p-EF'+str(EF_)+'-p1b.png'))
kargs = { 'duration': 0.5 }
imageio.mimsave('3p-EF'+str(periodos[0])+'-'+str(periodos[len(periodos)-1])+'-p1b.gif', images, **kargs)

images = []
for n in range(len(periodos)):
    images.append(imageio.imread(str(periodos[n])+'p-EF'+str(EF_)+'-e2b.png'))
imageio.mimsave('3p-EF'+str(periodos[0])+'-'+str(periodos[len(periodos)-1])+'-e2b.gif', images, **kargs)
