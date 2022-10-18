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
T = np.arange(5,120,5)

### Grafico delta E (energias_p1b_e2b[1,2]-energias_p1b_e2b[1,1])  de p1b para distintos T ###

for n in range(len(T)):
    with open('e2b-p1b-3p-{}-T'.format(EF_)+str(T[n])+'.pickle', 'rb') as f:
        energias_p1b_e2b = pickle.load(f)
    with open('3p-EF'+str(EF_)+'-T'+str(T[n])+'-p1b.pickles', 'rb') as f:
        x,dens,energy = pickle.load(f)
    plt.scatter(T[n],energy[int(energias_p1b_e2b[0,2])]-energy[int(energias_p1b_e2b[0,1])],color='r')
    #plt.scatter(EF_[n],energy[int(energias_p1b_e2b[0,2])]-energy[int(energias_p1b_e2b[0,1])],'o')
plt.xlabel("Temperatura [K]")
plt.ylabel(r"$\Delta E$ [eV]")
plt.title(r"GaAs/Al$_{{0.33}}$Ga$_{{0.66}}$As - p1b")
plt.tick_params(axis='both',direction='in')
plt.savefig('3p-EF'+str(T[0])+'-'+str(T[len(T)-1])+'-p1b-deltaE.png',bbox_inches='tight')
plt.show()

### Grafico delta E (energias_p1b_e2b[1,2]-energias_p1b_e2b[1,1])  de e2b para distintos T ###
for n in range(len(T)):
    with open('e2b-p1b-3p-{}-T'.format(EF_)+str(T[n])+'.pickle', 'rb') as f:
        energias_p1b_e2b = pickle.load(f)
    with open('3p-EF'+str(EF_)+'-T'+str(T[n])+'-e2b.pickles', 'rb') as f:
        x,dens,energy = pickle.load(f)
    plt.scatter(T[n],energy[int(energias_p1b_e2b[1,2])]-energy[int(energias_p1b_e2b[1,1])],color='r')
    #plt.scatter(EF_[n],energy[int(energias_p1b_e2b[0,2])]-energy[int(energias_p1b_e2b[0,1])],'o')
plt.xlabel("Temperatura [K]")
plt.ylabel(r"$\Delta E$ [eV]")
plt.title(r"GaAs/Al$_{{0.33}}$Ga$_{{0.66}}$As - e2b")
plt.tick_params(axis='both',direction='in')
plt.savefig('3p-EF'+str(T[0])+'-'+str(T[len(T)-1])+'-e2b-deltaE.png',bbox_inches='tight')
plt.show()


### Grafico delta E en función de longitud de onda para distintos EF p1b ###
for n in range(len(T)):
    with open('e2b-p1b-3p-{}-T'.format(EF_)+str(T[n])+'.pickle', 'rb') as f:
        energias_p1b_e2b = pickle.load(f)
    with open('3p-EF'+str(EF_)+'-T'+str(T[n])+'-p1b.pickles', 'rb') as f:
        x,dens,energy = pickle.load(f)
    plt.scatter(T[n],hc/(energy[int(energias_p1b_e2b[0,2])]-energy[int(energias_p1b_e2b[0,1])])*1e6,color='r')
plt.ylabel(r"$\lambda$ [nm]")
plt.xlabel("Temperatura [K]")
plt.title(r"GaAs/Al$_{{0.33}}$Ga$_{{0.66}}$As - p1b")
plt.tick_params(axis='both',direction='in')
plt.savefig('3p-EF'+str(T[0])+'-'+str(T[len(T)-1])+'-p1b-deltaE-lambda.png',bbox_inches='tight')
plt.show()

### Grafico delta E en función de longitud de onda para distintos EF e2b ###
for n in range(len(T)):
    with open('e2b-p1b-3p-{}-T'.format(EF_)+str(T[n])+'.pickle', 'rb') as f:
        energias_p1b_e2b = pickle.load(f)
    with open('3p-EF'+str(EF_)+'-T'+str(T[n])+'-e2b.pickles', 'rb') as f:
        x,dens,energy = pickle.load(f)
    plt.scatter(T[n],hc/(energy[int(energias_p1b_e2b[1,2])]-energy[int(energias_p1b_e2b[1,1])])*1e6,color='r')
plt.ylabel(r"$\lambda$ [nm]")
plt.xlabel("Temperatura [K]")
plt.title(r"GaAs/Al$_{{0.33}}$Ga$_{{0.66}}$As - e2b")
plt.tick_params(axis='both',direction='in')
plt.savefig('3p-EF'+str(T[0])+'-'+str(T[len(T)-1])+'-e2b-deltaE-lambda.png',bbox_inches='tight')
plt.show()