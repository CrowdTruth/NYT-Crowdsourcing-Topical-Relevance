#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 13:11:17 2018

@author: oanainel
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def variance(scores, value):
    
    variance=0
    for score in scores:
        variance += ((value-score)**2)
        final_variance=variance/float(len(scores) - 1)
    return final_variance


result_folder = "../Results/Pilot_2P-OrdPar-NoHigh/"
result_file = "units_Pilot_2P-OrdPar-NoHigh.csv"

dict_passages_counts = {'p1': 0, 'p2': 0, 'p3': 0, 'p4': 0, 'p5': 0, 
        'p6': 0, 'p7': 0, 'p8': 0, 'p9': 0, 'p10': 0, 'p11': 0, 'p12': 0, 
        'p13': 0, 'p14': 0, 'p15': 0, 'p16': 0, 'p17': 0, 'p18': 0, 'p19': 0, 'p20': 0 }
dict_passages_counts_nr = {'p1': 0, 'p2': 0, 'p3': 0, 'p4': 0, 'p5': 0, 
        'p6': 0, 'p7': 0, 'p8': 0, 'p9': 0, 'p10': 0, 'p11': 0, 'p12': 0, 
        'p13': 0, 'p14': 0, 'p15': 0, 'p16': 0, 'p17': 0, 'p18': 0, 'p19': 0, 'p20': 0 }
dict_passages_counts_r = {'p1': 0, 'p2': 0, 'p3': 0, 'p4': 0, 'p5': 0, 
        'p6': 0, 'p7': 0, 'p8': 0, 'p9': 0, 'p10': 0, 'p11': 0, 'p12': 0, 
        'p13': 0, 'p14': 0, 'p15': 0, 'p16': 0, 'p17': 0, 'p18': 0, 'p19': 0, 'p20': 0 }
dict_passages_all_votes = {'p1': [], 'p2': [], 'p3': [], 'p4': [], 'p5': [], 
        'p6': [], 'p7': [], 'p8': [], 'p9': [], 'p10': [], 'p11': [], 'p12': [], 
        'p13': [], 'p14': [], 'p15': [], 'p16': [], 'p17': [], 'p18': [], 'p19': [], 'p20': [] }

similarity = pd.read_csv("aggregated_similarity.csv")

for i in range(len(similarity.index)):
    dict_passages_counts[similarity["paragraph_index"].iloc[i]] += 1
    if (similarity["reviewers_rel"].iloc[i] == 0):
        dict_passages_counts_nr[similarity["paragraph_index"].iloc[i]] += 1
    else:
        dict_passages_counts_r[similarity["paragraph_index"].iloc[i]] += 1
    
gt = pd.read_csv("../ground_truth_data/reviewers_pilot_aggregated_judgments.csv")

wohpr = pd.read_csv(result_folder + result_file)


wohpr = wohpr[wohpr["reviewers_rel"] == 0]

for i in range(0, len(wohpr.index)):
    passages = wohpr['unit_annotation_score'].iloc[i]
    passages = passages[9:-2].replace("'", "").replace("s", "p")
    listOfPassages = passages.split(", ")
    
    for item in listOfPassages:
        pair = item.split(": ")
        if pair[0] != "none":
            dict_passages_all_votes[pair[0]].append(float(pair[1]))
          
for item in dict_passages_all_votes:
    if (len(dict_passages_all_votes[item]) != dict_passages_counts_nr[item]):
        for i in range(len(dict_passages_all_votes[item]), dict_passages_counts_nr[item]):
            dict_passages_all_votes[item].append(float(0.0))
 

dict_votes = pd.DataFrame.from_dict(dict_passages_all_votes, orient='index')
dict_votes = dict_votes.transpose()

print(dict_votes.describe())
cols = ['p1', 'p2', 'p3', 'p4', 'p5', 'p6', 'p7', 'p8', 'p9', 'p10', 'p11', 'p12', 'p13', 'p14', 'p15', 'p16', 'p17', 'p18', 'p19', 'p20']
dict_votes = dict_votes[cols]

plt.figure(figsize=(6,4))
fig, ax1 = plt.subplots()

color = dict(boxes='DarkBlue', whiskers='DarkBlue', medians='DarkBlue', caps='DarkBlue')

plot = dict_votes.plot(kind='box', color=color, ax=ax1, figsize=[6,4], showmeans=True, flierprops = dict(marker='o', markerfacecolor='darkblue', markersize=6,
                  linestyle='none'), medianprops = dict(linestyle='-', linewidth=2.5, color='red'), legend=True)

ax1.set_xticks(np.arange(1,len(cols)+1))
ax1.set_xticklabels(cols, rotation=45, fontsize=16)

ax1.set_yticks([0.0, 0.2, 0.4, 0.6, 0.8, 1.0])
ax1.set_yticklabels([0.0, 0.2, 0.4, 0.6, 0.8, 1.0], fontsize=20)

ax1.set_ylabel('relevance score', fontsize=20)
ax1.set_xlabel('paragraph index (position in document)', fontsize=17)
ax1.set_ylim(0.0, 1.1)

fig.tight_layout()
plt.savefig("../Plots/passages_owohighlight_medians_nr.eps",format='eps', dpi=1000)
plt.show()
plt.close()


