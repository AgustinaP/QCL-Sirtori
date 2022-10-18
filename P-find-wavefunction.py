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

def closest_value(input_list, input_value):
    arr = np.asarray(input_list)
    i = (np.abs(arr - input_value)).argmin()
    return i


def suma(dens, x, xi, xf):
    xi_pos = closest_value(x,xi)
    xf_pos = closest_value(x,xf)
    return sum(dens[xi_pos:xf_pos])

EF_ = 44
periodos = np.arange(1, 30, 2)

for n in range(len(periodos)):
    with open(str(periodos[n])+"p-EF"+str(EF_)+'-p1b.pickles', 'rb') as f:
        x,dens,energy = pickle.load(f)
    x = np.array([x[i,:]-x[i,x.shape[1]//2] for i in range(x.shape[0])])
    #find position of max density
    p1b_e = np.zeros(4)
    for i in range(x.shape[0]):
        color = '0.5'
        if(suma(dens[i,:],x[i,:],-14.25,-11.25) > suma(dens[int(p1b_e[3]),:],x[int(p1b_e[3]),:],-14.25,-11.25)) :
            p1b_e[3] = i
        if(suma(dens[i,:],x[i,:],-6.25,-4.25) > suma(dens[int(p1b_e[2]),:],x[int(p1b_e[2]),:],-6.25,-4.25)):
            p1b_e[2] = i
        if(suma(dens[i,:],x[i,:],-3.15,2.45) > suma(dens[int(p1b_e[1]),:],x[int(p1b_e[1]),:],-3.15,2.45)) and  energy[i] < 0.8:
            p1b_e[1] = i
        if(suma(dens[i,:],x[i,:],3.55,8.45) > suma(dens[int(p1b_e[0]),:],x[int(p1b_e[0]),:],3.55,8.45))and  energy[i] < 0.8:
            p1b_e[0] = i
    print(p1b_e)
 
#find e2b_e

    with open(str(periodos[n])+"p-EF"+str(EF_)+'-e2b.pickles', 'rb') as f:
        x,dens,energy = pickle.load(f)

    x = np.array([x[i,:]-x[i,x.shape[1]//2] for i in range(x.shape[0])])
    #find position of max density
    e2b_e = np.zeros(4)
    for i in range(x.shape[0]):
        color = '0.5'
        if(suma(dens[i,:],x[i,:],-14.25,-11.25) > suma(dens[int(e2b_e[3]),:],x[int(e2b_e[3]),:],-14.25,-11.25)):
            e2b_e[3] = i
        if(suma(dens[i,:],x[i,:],-6.25,-4.25) > suma(dens[int(e2b_e[2]),:],x[int(e2b_e[2]),:],-6.25,-4.25)):
            e2b_e[2] = i
        if(suma(dens[i,:],x[i,:],-3.15,2.45) > suma(dens[int(e2b_e[1]),:],x[int(e2b_e[1]),:],-3.15,2.45)) and energy[i] < 0.98:
            e2b_e[1] = i
        if(suma(dens[i,:],x[i,:],3.55,8.45) > suma(dens[int(e2b_e[0]),:],x[int(e2b_e[0]),:],3.55,8.45)) and energy[i] < 0.98:
            e2b_e[0] = i
    print(e2b_e)
    #save e2b_e and p1b_e
    with open(f'e2b-p1b-{periodos[n]}p-EF{EF_}.pickle', 'wb') as f:
        pickle.dump(np.array([p1b_e,e2b_e]), f)

