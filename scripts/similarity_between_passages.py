#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 10:27:21 2018

@author: oanainel
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats.stats import spearmanr

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

similarity = pd.read_csv("aggregated_similarity.csv")
gt = pd.read_csv("../ground_truth_data/reviewers_pilot_aggregated_judgments.csv")
random_highlight = pd.read_csv("../Results/Pilot_2P-RndPar-High/units_Pilot_2P-RndPar-High.csv")
random_no_highlight = pd.read_csv("../Results/Pilot_2P-RndPar-NoHigh/units_Pilot_2P-RndPar-NoHigh.csv")
ordered_highlight = pd.read_csv("../Results/Pilot_2P-OrdPar-High/units_Pilot_2P-OrdPar-High.csv")
ordered_no_highlight = pd.read_csv("../Results/Pilot_2P-OrdPar-NoHigh/units_Pilot_2P-OrdPar-NoHigh.csv")


similarity = pd.read_csv("aggregated_similarity.csv")
subset = similarity[similarity["reviewers_rel"] != 0]
#subset=similarity
cor_tfidf_onh = spearmanr(subset["paragraph_score_tfidf"], subset["random_highlight"])
print(cor_tfidf_onh)


cols = ['p1', 'p2', 'p3', 'p4', 'p5', 'p6', 'p7', 'p8', 'p9', 'p10', 'p11', 'p12', 'p13', 'p14', 'p15', 'p16', 'p17', 'p18', 'p19', 'p20']
corr = []
pvals = []

for i in cols:
    subset = similarity[similarity["paragraph_index"] == i]
    cor_tfidf_onh = spearmanr(subset["paragraph_score_tfidf"], subset["random_highlight"])
    corr.append(cor_tfidf_onh.correlation)
    pvals.append(cor_tfidf_onh.pvalue)
    
Index= ['TF-IDF']
Cols = ['p1', 'p2', 'p3', 'p4', 'p5', 'p6', 'p7', 'p8', 'p9', 'p10', 'p11', 'p12', 'p13', 'p14', 'p15', 'p16', 'p17', 'p18', 'p19', 'p20']
df = pd.DataFrame(data=[corr], index=Index, columns=Cols)


#plt.pcolor(df)

#plt.ylim((0, len(Cols)))
plt.figure(figsize=(7,1.5))
heatmap = plt.pcolor([corr], cmap=plt.cm.Blues)
plt.yticks(np.arange(0.5, 1, 0.6), df.index)
plt.xticks(np.arange(0.5, len(df.columns), 1), df.columns, rotation=45)
plt.colorbar(orientation='horizontal',pad=0.45, fraction=0.2)
plt.tight_layout()
plt.savefig("../Plots/paragraph_corr_tfidf.pdf",bbox_inches='tight',format='pdf', dpi=1000)
plt.show()
plt.close()

pvals = [0.00280111294, 0.00000849883, 0.000438194924187, 0.01920314894, 0.00411472861, 
         0.00397953231577, 0.00136286378092, 0.110953038178, 0.00920726520126, 
         0.000636487507785, 0.00331998736559, 0.0115102457042,
         0.198287622487, 0.0526169658811, 0.0102594511971, 0.106317546425, 
         0.6, 0.0, 1.0, 1.0]

Index= ['P-Value']
df = pd.DataFrame(data=[pvals], index=Index, columns=cols)

#plt.ylim((0, len(Cols)))
plt.figure(figsize=(7,1.5))
heatmap = plt.pcolor([pvals], cmap=plt.cm.Blues)
plt.yticks(np.arange(0.5, 1, 0.6), df.index)
plt.xticks(np.arange(0.5, len(df.columns), 1), df.columns, rotation=45)
cbar=plt.colorbar(orientation='horizontal',pad=0.45, fraction=0.2)
plt.tight_layout()
plt.savefig("../Plots/paragraph_corr_tfidf_pvals.pdf",bbox_inches='tight',format='pdf', dpi=1000)
plt.show()
plt.close()
