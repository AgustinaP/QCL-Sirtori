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

EF_ = 44
X1 = 0.33
ancho = np.arange(-20,50,1)
T = 77

### Grafico delta E (energias_p1b_e2b[1,2]-energias_p1b_e2b[1,1])  de p1b para distintos EF ###

for n in range(len(ancho)):
    with open('e2b-p1b-3p-EF{}'.format(EF_)+'-ancho'+str(ancho[n]+100)+'.pickle', 'rb') as f:
        energias_p1b_e2b = pickle.load(f)
    with open('3p-EF'+str(EF_)+'-ancho'+str(ancho[n]+100)+'-p1b.pickles', 'rb') as f:
        x,dens,energy = pickle.load(f)
    plt.scatter(ancho[n]/100,energy[int(energias_p1b_e2b[0,2])]-energy[int(energias_p1b_e2b[0,1])],color='r')
    #plt.scatter(EF_[n],energy[int(energias_p1b_e2b[0,2])]-energy[int(energias_p1b_e2b[0,1])],'o')
plt.xlabel("Aumento de ancho [%]")
plt.ylabel(r"$\Delta E$ [eV]")
plt.title(r"GaAs/Al$_{{0.33}}$Ga$_{{0.66}}$As - EF = {} kV/cm - T = {} K - e2b".format(EF_,T))            
plt.tick_params(axis='both',direction='in')
plt.savefig('3p-EF'+str(ancho[0])+'-'+str(ancho[len(ancho)-1])+'-p1b-deltaE.png',bbox_inches='tight')
plt.show()

### Grafico delta E (energias_p1b_e2b[1,2]-energias_p1b_e2b[1,1])  de e2b para distintos EF ###
for n in range(len(ancho)):
    with open('e2b-p1b-3p-EF{}'.format(EF_)+'-ancho'+str(ancho[n]+100)+'.pickle', 'rb') as f:
        energias_p1b_e2b = pickle.load(f)
    with open('3p-EF'+str(EF_)+'-ancho'+str(ancho[n]+100)+'-p1b.pickles', 'rb') as f:
        x,dens,energy = pickle.load(f)
    plt.scatter(ancho[n],energy[int(energias_p1b_e2b[1,2])]-energy[int(energias_p1b_e2b[1,1])],color='r')
    #plt.scatter(EF_[n],energy[int(energias_p1b_e2b[1,2])]-energy[int(energias_p1b_e2b[1,1])],'o')
plt.xlabel("Aumento de ancho [%]")
plt.ylabel(r"$\Delta E$ [eV]")
plt.title(r"GaAs/Al$_{{0.33}}$Ga$_{{0.66}}$As - EF = {} kV/cm - T = {} K - e2b".format(EF_,T))            
plt.tick_params(axis='both',direction='in')
plt.savefig('3p-EF'+str(ancho[0])+'-'+str(ancho[len(ancho)-1])+'-e2b-deltaE.png',bbox_inches='tight')
plt.show()


### Grafico delta E en función de longitud de onda para distintos EF p1b ###
for n in range(len(ancho)):
    with open('e2b-p1b-3p-EF{}'.format(EF_)+'-ancho'+str(ancho[n]+100)+'.pickle', 'rb') as f:
        energias_p1b_e2b = pickle.load(f)
    with open('3p-EF'+str(EF_)+'-ancho'+str(ancho[n]+100)+'-p1b.pickles', 'rb') as f:
        x,dens,energy = pickle.load(f)
    plt.scatter(ancho[n],hc/(energy[int(energias_p1b_e2b[0,2])]-energy[int(energias_p1b_e2b[0,1])])*1e6,color='r')
plt.ylabel(r"$\lambda$ [nm]")
plt.xlabel("Aumento de ancho [%]")
plt.title(r"GaAs/Al$_{{0.33}}$Ga$_{{0.66}}$As - EF = {} kV/cm - T = {} K - e2b".format(EF_,T))            
plt.title(r"GaAs/Al$_{{0.33}}$Ga$_{{0.66}}$As - p1b")
plt.tick_params(axis='both',direction='in')
plt.savefig('3p-EF'+str(ancho[0])+'-'+str(ancho[len(ancho)-1])+'-p1b-deltaE-lambda.png',bbox_inches='tight')
plt.show()

### Grafico delta E en función de longitud de onda para distintos EF e2b ###
for n in range(len(ancho)):
    with open('e2b-p1b-3p-EF{}'.format(EF_)+'-ancho'+str(ancho[n]+100)+'.pickle', 'rb') as f:
        energias_p1b_e2b = pickle.load(f)
    with open('3p-EF'+str(EF_)+'-ancho'+str(ancho[n]+100)+'-p1b.pickles', 'rb') as f:
        x,dens,energy = pickle.load(f)
    plt.scatter(ancho[n],hc/(energy[int(energias_p1b_e2b[1,2])]-energy[int(energias_p1b_e2b[1,1])])*1e6,color='r')
plt.ylabel(r"$\lambda$ [nm]")
plt.xlabel("Aumento de ancho [%]")
plt.title(r"GaAs/Al$_{{0.33}}$Ga$_{{0.66}}$As - EF = {} kV/cm - T = {} K - e2b".format(EF_,T))            
plt.tick_params(axis='both',direction='in')
plt.savefig('3p-EF'+str(ancho[0])+'-'+str(ancho[len(ancho)-1])+'-e2b-deltaE-lambda.png',bbox_inches='tight')
plt.show()
