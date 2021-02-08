#!/usr/bin/env python
#This code has been developed by David Arias-Olivares, Ph. D. ndariaso@gmail.com
#Please mention it if you use it
#If a scan of electrostatic repulsion using Bader's charges is developed, this file helps to read all the *sum files,
#extract the Bader's charges as well as the coordinates and compute the electrostatic respulsion.
#all *sum files must be in one folder without any other file. You should provide the number of
#atoms in your system.
#You need only to call this file

import sys
import os
import numpy as np

Nnuc = int(input("Enter the number of atoms: "))
U = 0
resu = sorted(os.listdir(os.curdir))  # list and save the files of current directory

for i in resu:
    f_dat = open("datos.dat", "a")
    q1_list = []
    x1_list = []
    arch = open(i, 'r')
    line = arch.readlines()
    for j in range(Nnuc):
        atom = (line[36 + j])
        coor = (atom.split())
        x1_list.append(coor[2:])
        bade = (line[36 + Nnuc + 11 + j])
        qnuc = bade.split()
        q1_list.append(qnuc[1])
        j = j + 1
    q2_list = np.array(q1_list).astype(float)
    x2_list = np.array(x1_list).astype(float)
    for a in range(Nnuc):
        for b in range(Nnuc):
            if a != b:
                q_ij = q2_list[a] * q2_list[b]
                d2_ij = np.linalg.norm(x2_list[a] - x2_list[b])
                U = U + (q_ij / d2_ij)
    value = str(U / 2)
    f_dat.write(value)
    f_dat.write("\n")
    U = 0
    arch.close()
