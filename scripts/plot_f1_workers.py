#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue May 22 10:26:59 2018

@author: oanainel
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

F1_3w = pd.read_csv("../Results/Pilot_2P-RndPar-High/F1_3.csv")
F1_4w = pd.read_csv("../Results/Pilot_2P-RndPar-High/F1_4.csv")
F1_5w = pd.read_csv("../Results/Pilot_2P-RndPar-High/F1_5.csv")
F1_6w = pd.read_csv("../Results/Pilot_2P-RndPar-High/F1_6.csv")
F1_7w = pd.read_csv("../Results/Pilot_2P-RndPar-High/F1_7.csv")
F1_8w = pd.read_csv("../Results/Pilot_2P-RndPar-High/F1_8.csv")
F1_9w = pd.read_csv("../Results/Pilot_2P-RndPar-High/F1_9.csv")
F1_10w = pd.read_csv("../Results/Pilot_2P-RndPar-High/F1_10.csv")
F1_11w = pd.read_csv("../Results/Pilot_2P-RndPar-High/F1_11.csv")
F1_12w = pd.read_csv("../Results/Pilot_2P-RndPar-High/F1_12.csv")
F1_13w = pd.read_csv("../Results/Pilot_2P-RndPar-High/F1_13.csv")
F1_14w = pd.read_csv("../Results/Pilot_2P-RndPar-High/F1_14.csv")

F1_15w_b_r = 0.95
F1_15w_b_nr = 0.94
F1_15w_t_hr = 0.66
F1_15w_t_r = 0.56
F1_15w_t_nr = 0.94

nist_b_r = 0.80
nist_b_nr = 0.79

nist_t_hr = 0.57
nist_t_r = 0.45
nist_t_nr = 0.79

F1_b_nr = [F1_3w["F1_nr_binary"].mean(), F1_4w["F1_nr_binary"].mean(), F1_5w["F1_nr_binary"].mean(), 
           F1_6w["F1_nr_binary"].mean(), F1_7w["F1_nr_binary"].mean(), F1_8w["F1_nr_binary"].mean(), 
           F1_9w["F1_nr_binary"].mean(), F1_10w["F1_nr_binary"].mean(), F1_11w["F1_nr_binary"].mean(),
           F1_12w["F1_nr_binary"].mean(), F1_13w["F1_nr_binary"].mean(), F1_14w["F1_nr_binary"].mean(), 
           F1_15w_b_nr]

F1_b_r = [F1_3w["F1_n_binary"].mean(), F1_4w["F1_n_binary"].mean(), F1_5w["F1_n_binary"].mean(), 
           F1_6w["F1_n_binary"].mean(), F1_7w["F1_n_binary"].mean(), F1_8w["F1_n_binary"].mean(), 
           F1_9w["F1_n_binary"].mean(), F1_10w["F1_n_binary"].mean(), F1_11w["F1_n_binary"].mean(),
           F1_12w["F1_n_binary"].mean(), F1_13w["F1_n_binary"].mean(), F1_14w["F1_n_binary"].mean(), 
           F1_15w_b_r]

F1_t_nr = [F1_3w["F1_nr_ternary"].mean(), F1_4w["F1_nr_ternary"].mean(), F1_5w["F1_nr_ternary"].mean(), 
           F1_6w["F1_nr_ternary"].mean(), F1_7w["F1_nr_ternary"].mean(), F1_8w["F1_nr_ternary"].mean(), 
           F1_9w["F1_nr_ternary"].mean(), F1_10w["F1_nr_ternary"].mean(), F1_11w["F1_nr_ternary"].mean(),
           F1_12w["F1_nr_ternary"].mean(), F1_13w["F1_nr_ternary"].mean(), F1_14w["F1_nr_ternary"].mean(), 
           F1_15w_t_nr]

F1_t_r = [F1_3w["F1_r_ternary"].mean(), F1_4w["F1_r_ternary"].mean(), F1_5w["F1_r_ternary"].mean(), 
           F1_6w["F1_r_ternary"].mean(), F1_7w["F1_r_ternary"].mean(), F1_8w["F1_r_ternary"].mean(), 
           F1_9w["F1_r_ternary"].mean(), F1_10w["F1_r_ternary"].mean(), F1_11w["F1_r_ternary"].mean(),
           F1_12w["F1_r_ternary"].mean(), F1_13w["F1_r_ternary"].mean(), F1_14w["F1_r_ternary"].mean(), 
           F1_15w_t_r]

F1_t_hr = [F1_3w["F1_hr_ternary"].mean(), F1_4w["F1_hr_ternary"].mean(), F1_5w["F1_hr_ternary"].mean(), 
           F1_6w["F1_hr_ternary"].mean(), F1_7w["F1_hr_ternary"].mean(), F1_8w["F1_hr_ternary"].mean(), 
           F1_9w["F1_hr_ternary"].mean(), F1_10w["F1_hr_ternary"].mean(), F1_11w["F1_hr_ternary"].mean(),
           F1_12w["F1_hr_ternary"].mean(), F1_13w["F1_hr_ternary"].mean(), F1_14w["F1_hr_ternary"].mean(), 
           F1_15w_t_hr]

plt.rcParams['figure.figsize'] = 6, 4
plt.plot([x for x in range(3, 16)], F1_t_nr, 'bo-',
         color = 'r', lw = 2, label = "F1 Crowd - Not Relevant")
plt.plot([x for x in range(3, 16)], F1_t_r , 'bo-',
         color = 'darkgreen', lw = 2, label = "F1 Crowd - Relevant")
plt.plot([x for x in range(3, 16)], F1_t_hr, 'bo-',
         color = 'darkblue', lw = 2, label = "F1 Crowd - Highly Relevant")
plt.axhline(y = nist_t_nr, color = 'pink', lw = 2, label = "F1 NIST - Not Relevant")
plt.axhline(y = nist_t_r, color = 'lightgreen', lw = 2, label = "F1 NIST - Relevant")
plt.axhline(y = nist_t_hr, color = 'lightblue', lw = 2, label = "F1 NIST - Highly Relevant")

plt.xlabel("number of workers", fontsize=16)
plt.ylabel("F1-score", fontsize=16)
plt.xticks( range(3,16) , fontsize=16)
plt.ylim(0.0, 1.0)
leg = plt.legend(fontsize=10)
leg.get_frame().set_alpha(0.5)
plt.grid(ls=':')
plt.tight_layout()
plt.savefig("../Plots/ternary_no_of_workers.eps", format='eps', dpi=1000)
plt.show()
plt.close()


plt.rcParams['figure.figsize'] = 6, 4
plt.plot([x for x in range(3, 16)], F1_b_nr, 'bo-',
         color = 'r', lw = 2, label = "F1 Crowd - Not Relevant")
plt.plot([x for x in range(3, 16)], F1_b_r , 'bo-',
         color = 'darkgreen', lw = 2, label = "F1 Crowd - Relevant")
plt.axhline(y = nist_b_nr, color = 'pink', lw = 2, label = "F1 NIST - Not Relevant")
plt.axhline(y = nist_b_r, color = 'lightgreen', lw = 2, label = "F1 NIST - Relevant")

plt.xlabel("number of workers", fontsize=16)
plt.ylabel("F1-score", fontsize=16)
plt.xticks( range(3,16) , fontsize=16)
plt.ylim(0.0, 1.0)
leg = plt.legend(fontsize=14)
leg.get_frame().set_alpha(0.5)
plt.tight_layout()
plt.grid(ls=':')
plt.savefig("../Plots/binary_no_of_workers.eps", format='eps', dpi=1000)