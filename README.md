# QCL-Sirtori

Some simulation files of Sirtori Article about QCL around 11 um (10.1051/bib-sfo:2002057). 

We change some parameters such as length(L), width(W), number of periods(P), electric field(EF), and temperature(T) around the QCL described in the article. 
This repository contains a python script to create the structures in the correct format and another to solve those structures. Moreover, I include two programs to graph results, one to make a gif with the most significant wavefunction and their respective structure. The other one contains a graph of ΔE and Δλ. 


## About the solver 
The modeling of heterostructures involves several parameters. Some of them define the structure design, such as the materials and the width of each layer. There are other parameters such as material characteristics, common to all heterostructures (like their gap). In addition, there are environmental parameters, where the heterostructure lies (for example temperature and electric field) which modify the result.
There are 3 entry files types:
- Structure file
- Matirial file 
- Options file 

All of them are JSON type (with comments) and important labels are defined in defin.hpp.

The electronic state calculus formulated on in envelop function method and their implementation is based on finite difference method.
There are two solvers that are based in two different structure band model:
- P1b Model: Parabolic model of 1 band.
- e2b Model: Effective model of 2 bands
