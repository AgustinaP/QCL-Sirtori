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


# e2b-p1b-3p-emision from txt
#energias_p1b = np.loadtxt('e2b-p1b-3p-emision.txt')

#### Grafico la emisión de p1b y e2b ####
'''
plt.scatter(energias_p1b[:,0],energias_p1b[:,1],label='p1b')
plt.scatter(energias_p1b[:,0],energias_p1b[:,2],label='e2b')
plt.legend()
plt.xlabel('Campo eléctrico [kV/cm]')
plt.ylabel(r'$\Delta$Energia [eV]')
plt.tick_params(axis='both',direction='in')
plt.savefig('e2b-p1b-3p-emision.pdf',bbox_inches='tight')
plt.show()
'''
### Grafico longitud de onda p1b y e2b ###
'''
plt.scatter(energias_p1b[:,0],hc/energias_p1b[:,1]*1e8,label='p1b')
plt.scatter(energias_p1b[:,0],hc/energias_p1b[:,2]*1e8,label='e2b')
plt.legend()
plt.xlabel('Campo eléctrico [kV/cm]')
plt.ylabel(r'Longitud de onda [nm]')
plt.tick_params(axis='both',direction='in')
plt.savefig('e2b-p1b-3p-longitud.pdf',bbox_inches='tight')
plt.show()
'''

### load pozo ###
with open('pozo.pkl', 'rb') as f:
    z,conduction_band_profile = pickle.load(f)

### Electric field in kV/cm ###
EF_ = np.arange(25, 65, 1)


### Load relevant energies e2b p1b ###

#energias_p1b_e2b = np.array([np.loadtxt('e2b-p1b-3p-'+str(EF_[n])+'.txt') for n in range(len(EF_))])

print("p1b")
### Grafico la emisión de p1b para distintos EF ###
for n in range(len(EF_)):
    with open('e2b-p1b-3p-{}.pickle'.format(EF_[n]), 'rb') as f:
        energias_p1b_e2b = pickle.load(f)
    #print(energias_p1b_e2b[0,:])
    with open('3p-EF'+str(EF_[n])+'-p1b.pickles', 'rb') as f:
        x,dens,energy = pickle.load(f)
    plt.plot((z-z[len(z)//2]),conduction_band_profile-EF_[n]/10000* (z-z[len(z)//2]))
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
    plt.text(10,1.1,'EF = '+str(EF_[n])+' kV/cm\np1b')
    plt.title(r"GaAs/Al$_{{0.33}}$Ga$_{{0.66}}$As")
    plt.tick_params(axis='both',direction='in')
    plt.savefig('3p-EF'+str(EF_[n])+'-p1b.png',bbox_inches='tight')
    plt.clf()

### Grafico la emisión de e2b para distintos EF ###
print("e2b")
for n in range(len(EF_)):
    with open('e2b-p1b-3p-{}.pickle'.format(EF_[n]), 'rb') as f:
        energias_p1b_e2b = pickle.load(f)
    with open('3p-EF'+str(EF_[n])+'-e2b.pickles', 'rb') as f:
        x,dens,energy = pickle.load(f)
    #print(energias_p1b_e2b[0,:,0])
    plt.plot((z-z[len(z)//2]),conduction_band_profile-EF_[n]/10000* (z-z[len(z)//2]))
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
    plt.text(10,1.1,'EF = '+str(EF_[n])+' kV/cm\ne2b')
    plt.title(r"GaAs/Al$_{{0.33}}$Ga$_{{0.66}}$As")
    plt.tick_params(axis='both',direction='in')
    plt.savefig('3p-EF'+str(EF_[n])+'-e2b.png',bbox_inches='tight')
    plt.clf()
    
### GIF ###

images = []
for n in range(len(EF_)):
    images.append(imageio.imread('3p-EF'+str(EF_[n])+'-p1b.png'))
kargs = { 'duration': 0.5 }
imageio.mimsave('3p-EF'+str(EF_[0])+'-'+str(EF_[len(EF_)-1])+'-p1b.gif', images, **kargs)

images = []
for n in range(len(EF_)):
    images.append(imageio.imread('3p-EF'+str(EF_[n])+'-e2b.png'))
imageio.mimsave('3p-EF'+str(EF_[0])+'-'+str(EF_[len(EF_)-1])+'-e2b.gif', images, **kargs)