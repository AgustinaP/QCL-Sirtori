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


### Electric field in kV/cm ###
EF_ = 44
X1 = 0.33
ancho = np.arange(-20,50, 1)
T = 77


### Load relevant energies e2b p1b ###

#energias_p1b_e2b = np.array([np.loadtxt('e2b-p1b-3p-'+str(EF_[n])+'.txt') for n in range(len(EF_))])

print("p1b")
### Grafico la emisión de p1b para distintos EF ###
for n in range(len(ancho)):
    with open('e2b-p1b-3p-EF{}'.format(EF_)+'-ancho'+str(ancho[n]+100)+'.pickle', 'rb') as f:
        energias_p1b_e2b = pickle.load(f)
    #print(energias_p1b_e2b[0,:])
    with open('3p-EF'+str(EF_)+'-ancho'+str(ancho[n]+100)+'-p1b.pickles', 'rb') as f:
        x,dens,energy = pickle.load(f)
    with open("3p-EF"+str(EF_)+'-ancho'+str(ancho[n]+100)+'-pozo.pickles', 'rb') as f:
        z,conduction_band_profile = pickle.load(f)
    fig, ax = plt.subplots( figsize=(8, 6))
    ax.plot((z-z[len(z)//2]),conduction_band_profile-EF_/10000* (z-z[len(z)//2]))
    ### plot each f0 ###
    for i in range(x.shape[0]):
        color = '0.5'
        if i in energias_p1b_e2b[0,:]:
           color ='r'
        ax.plot(x[i,:]-x[i,x.shape[1]//2],dens[i]+energy[i],color=color)
    plt.xlabel("Distancia [nm]")
    plt.ylabel("Energía [eV]")
    plt.xlim(-40,40)
    plt.ylim(0.5,1.2)
    plt.text(10,1.1,'ancho = '+str(100+ancho[n])+'%')
    plt.title(r"GaAs/Al$_{{0.33}}$Ga$_{{0.66}}$As - EF = {} kV/cm - T = {} K - p1b".format(EF_,T))            
    plt.tick_params(axis='both',direction='in')
    plt.savefig('3p-EF'+str(EF_)+'-ancho'+str(ancho[n]+100)+'-p1b.png',bbox_inches='tight')
    plt.clf()
    plt.close()

### Grafico la emisión de e2b para distintos EF ###
print("e2b")
for n in range(len(ancho)):
    with open('e2b-p1b-3p-EF{}'.format(EF_)+'-ancho'+str(ancho[n]+100)+'.pickle', 'rb') as f:
        energias_p1b_e2b = pickle.load(f)
    #print(energias_p1b_e2b[0,:])
    with open('3p-EF'+str(EF_)+'-ancho'+str(ancho[n]+100)+'-e2b.pickles', 'rb') as f:
        x,dens,energy = pickle.load(f)
    with open("3p-EF"+str(EF_)+'-ancho'+str(ancho[n]+100)+'-pozo.pickles', 'rb') as f:
        z,conduction_band_profile = pickle.load(f)
    fig, ax = plt.subplots( figsize=(8, 6))
    ax.plot((z-z[len(z)//2]),conduction_band_profile-EF_/10000* (z-z[len(z)//2]))
    ### plot each f0 ###
    for i in range(x.shape[0]):
        color = '0.5'
        if i in energias_p1b_e2b[1,:]:
           color ='r'
        ax.plot(x[i,:]-x[i,x.shape[1]//2],dens[i]+energy[i],color=color)
    plt.xlabel("Distancia [nm]")
    plt.ylabel("Energía [eV]")
    plt.xlim(-40,40)
    plt.ylim(0.5,1.2)
    plt.text(10,1.1,'anchos = '+str(100+ancho[n])+'%')
    plt.title(r"GaAs/Al$_{{0.33}}$Ga$_{{0.66}}$As - EF = {} kV/cm - T = {} K - e2b".format(EF_,T))            
    plt.tick_params(axis='both',direction='in')
    plt.savefig('3p-EF'+str(EF_)+'-ancho'+str(ancho[n]+100)+'-e2b.png',bbox_inches='tight')
    plt.clf()
    plt.close()
    
### GIF ###

images = []
for n in range(len(ancho)):
    images.append(imageio.imread('3p-EF'+str(EF_)+'-ancho'+str(ancho[n]+100)+'-p1b.png'))
#kargs = { 'duration': 0.5 }
imageio.mimsave('3p-EF'+str(ancho[0])+'-'+str(ancho[len(ancho)-1])+'-p1b.gif', images)

images = []
for n in range(len(ancho)):
    images.append(imageio.imread('3p-EF'+str(EF_)+'-ancho'+str(ancho[n]+100)+'-e2b.png'))
#kargs = { 'duration': 0.5 }
imageio.mimsave('3p-EF'+str(ancho[0])+'-'+str(ancho[len(ancho)-1])+'-e2b.gif', images)