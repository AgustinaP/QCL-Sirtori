#!/usr/bin/env python
# coding: utf-8

import pickle
import pkg_resources
pkg_resources.require('pythera==0.3.1')
import pythera
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rcParams
rcParams['font.family'] = 'serif'
rcParams['font.sans-serif'] = ['DejaVu Sans']
rcParams['font.size'] = 14
hc = 4.135667696e-15*3e8 #eV m

EF_ = 44
X1 = 0.33
ancho = np.arange(-20,50,1)

def closest_value(input_list, input_value):
    arr = np.asarray(input_list)
    i = (np.abs(arr - input_value)).argmin()
    return i


def suma(dens, x, xi, xf):
    xi_pos = closest_value(x,xi)
    xf_pos = closest_value(x,xf)
    return sum(dens[xi_pos:xf_pos])

#find p1b_e
for n in range(len(ancho)):
    with open('3p-EF'+str(EF_)+'-ancho'+str(ancho[n]+100)+'-p1b.pickles', 'rb') as f:
        x,dens,energy = pickle.load(f)
    x = np.array([x[i,:]-x[i,x.shape[1]//2] for i in range(x.shape[0])])
    p1b_e = np.zeros(4)
    for i in range(x.shape[0]):
        color = '0.5'
        if(suma(dens[i,:],x[i,:],-14.25*(1+ancho[n]/100),-11.25*(1+ancho[n]/100)) > suma(dens[int(p1b_e[3]),:],x[int(p1b_e[3]),:],-14.25*(1+ancho[n]/100),-11.25*(1+ancho[n]/100))) :
            p1b_e[3] = i
        if(suma(dens[i,:],x[i,:],-6.25*(1+ancho[n]/100),-4.25*(1+ancho[n]/100)) > suma(dens[int(p1b_e[2]),:],x[int(p1b_e[2]),:],-6.25*(1+ancho[n]/100),-4.25*(1+ancho[n]/100))):
            p1b_e[2] = i
        if(suma(dens[i,:],x[i,:],-3.15*(1+ancho[n]/100),2.45*(1+ancho[n]/100)) > suma(dens[int(p1b_e[1]),:],x[int(p1b_e[1]),:],-3.15*(1+ancho[n]/100),2.45*(1+ancho[n]/100))) and  energy[i] < 0.8:
            p1b_e[1] = i
        if(suma(dens[i,:],x[i,:],3.55*(1+ancho[n]/100),8.45*(1+ancho[n]/100)) > suma(dens[int(p1b_e[0]),:],x[int(p1b_e[0]),:],3.55*(1+ancho[n]/100),8.45*(1+ancho[n]/100)))and  energy[i] < 0.8:
            p1b_e[0] = i
    print(p1b_e)
 
#find e2b_e

    with open('3p-EF'+str(EF_)+'-ancho'+str(ancho[n]+100)+'-e2b.pickles', 'rb') as f:
        x,dens,energy = pickle.load(f)
    #find position of max density
    e2b_e = np.zeros(4)
    x = np.array([x[i,:]-x[i,x.shape[1]//2] for i in range(x.shape[0])])

    for i in range(x.shape[0]):
        color = '0.5'
        if(suma(dens[i,:],x[i,:],-14.25*(1+ancho[n]/100),-11.25*(1+ancho[n]/100)) > suma(dens[int(e2b_e[3]),:],x[int(e2b_e[3]),:],-14.25*(1+ancho[n]/100),-11.25*(1+ancho[n]/100))):
            e2b_e[3] = i
        if(suma(dens[i,:],x[i,:],-6.25*(1+ancho[n]/100),-4.25*(1+ancho[n]/100)) > suma(dens[int(e2b_e[2]),:],x[int(e2b_e[2]),:],-6.25*(1+ancho[n]/100),-4.25*(1+ancho[n]/100))):
            e2b_e[2] = i
        if(suma(dens[i,:],x[i,:],-3.15*(1+ancho[n]/100),2.45*(1+ancho[n]/100)) > suma(dens[int(e2b_e[1]),:],x[int(e2b_e[1]),:],-3.15*(1+ancho[n]/100),2.45*(1+ancho[n]/100))) and energy[i] < 0.98:
            e2b_e[1] = i
        if(suma(dens[i,:],x[i,:],3.55*(1+ancho[n]/100),8.45*(1+ancho[n]/100)) > suma(dens[int(e2b_e[0]),:],x[int(e2b_e[0]),:],3.55*(1+ancho[n]/100),8.45)) and energy[i] < 0.98:
            e2b_e[0] = i
    print(e2b_e)
    #save e2b_e and p1b_e
    with open('e2b-p1b-3p-EF{}'.format(EF_)+'-ancho'+str(ancho[n]+100)+'.pickle', 'wb') as f:
        pickle.dump(np.array([p1b_e,e2b_e]), f)
