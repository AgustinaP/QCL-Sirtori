#!/usr/bin/env python
# coding: utf-8

# Es un ejemplo sencillo para ver si hace diferencia calcular usando el modelo simple de una banda (p1b) y el completo de dos bandas (e2b). 
# Se ve que la diferencia es apreciable y hay que usar el modelo de dos bandas.
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


def PlotBandZProfile_field(ax,structure,conduction_band = True,valence_band = False,n = 500):
    """ Plotea el perfil de bandas en la direccion z.
    Args: 
        ax: Axes donde plotear.
        structure: Struture a plotear.
        conduction_band: Define si se plotea la banda de conducción.
        valence_band: Define si se plotea la banda de valencia (hh y lh).
        n: Número de puntos a utilizar en el ploteo.
    Returns:
        Tupple de las Line2D devueltas por ax.plot, (conduction_line, valence_line).
    """
    external_field = structure.GetParameterDouble('FIELD')

    z = np.asarray(structure.Layers.GetZVectorDouble(n))
    external_potential_vector = external_field * (z-z[n//2])
    valence_band_profile    = np.asarray(structure.Layers.GetMaterialParameterZVectorDouble("VBO", n)) + external_potential_vector
    conduction_band_profile = np.asarray(structure.Layers.GetMaterialParameterZVectorDouble("GAP", n)) + valence_band_profile
    
    line_conduction_band = ax.plot(z-z[n//2], conduction_band_profile)
    if valence_band:
        line_valence_band = ax.plot(z, valence_band_profile)
        return line_conduction_band, line_valence_band
    with open("3p-EF"+str(EF_)+'-ancho'+str(ancho[i]+100)+'-pozo.pickles', 'wb') as f:
        pickle.dump([z,conduction_band_profile], f, protocol=pickle.HIGHEST_PROTOCOL)
    return (line_conduction_band,)

### Inicializo la estructura y le cargo los datos ###
EF_ =  44
X1 = 0.33
ancho = np.arange(-20,50,1)

for i in range(len(ancho)):
    print(ancho[i])
    structure = pythera.base.Structure()
    structure.Load("3p-EF"+str(EF_)+'-ancho'+str(ancho[i]+100)+".str")
    EF = - structure.GetParameterDouble('FIELD') * 1e7 /1000 #kV/cm
    
    fig, ax = plt.subplots(figsize=(8, 6))
    PlotBandZProfile_field(ax,structure,conduction_band = True,valence_band = False,n = 2500)
    plt.clf()
    plt.close(fig)
    ### solve p1b ###
    p1b_solver_cond = pythera.edifi.SolverP1b(pythera.edifi.BandTypes.Conduction, structure, 1500,30)
    p1b_solver_cond.Solve()
    p1b_states_cond = p1b_solver_cond.GetStates()
    p1b_energies_cond = np.asarray([p1b_states_cond[n].GetEnergy() for n in range(p1b_states_cond.GetNumStates())])
    p1b_resdata_cond = p1b_solver_cond.GetResolutionData()
    dens = np.array([np.asarray(p1b_states_cond[n].GetEnvelopesFunctions()[0].GetEnvelope() )**2 for n in range(p1b_states_cond.GetNumStates())])
    z = np.array([np.asarray(structure.Layers.GetZVectorDouble(p1b_resdata_cond.GetNumGrid())) for n in range(p1b_states_cond.GetNumStates())])
    ### Save with pickle ###
    with open("3p-EF"+str(EF_)+'-ancho'+str(ancho[i]+100)+'-p1b.pickles', 'wb') as handle:
        pickle.dump([z,dens, p1b_energies_cond], handle, protocol=pickle.HIGHEST_PROTOCOL)

    ### solve e2b ###
    e2b_solver = pythera.edifi.SolverE2b(False, structure, 1500,30)
    e2b_solver.Solve()
    e2b_states = e2b_solver.GetStates()
    e2b_energies = np.asarray([e2b_states[n].GetEnergy() for n in range(e2b_states.GetNumStates())])
    e2b_resdata = e2b_solver.GetResolutionData()
    dens = np.array([np.asarray(e2b_states[n].GetEnvelopesFunctions()[0].GetEnvelope() )**2 for n in range(e2b_states.GetNumStates())])
    z = np.array([np.asarray(structure.Layers.GetZVectorDouble(e2b_resdata.GetNumGrid())) for n in range(e2b_states.GetNumStates())])
    ### Save with pickle ###
    with open("3p-EF"+str(EF_)+'-ancho'+str(ancho[i]+100)+'-e2b.pickles', 'wb') as handle:
        pickle.dump([z,dens,e2b_energies], handle, protocol=pickle.HIGHEST_PROTOCOL)
