#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 20:56:51 2018

@author: oanainel
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from mpl_toolkits.mplot3d import Axes3D

def compute_F1_score_highly_relevant(dataset):
    nyt_f1 = np.zeros(shape=(100, 3))
    for idx in range(0, 100):
        thresh = (idx + 1) / 100.0
        tp = 0
        fp = 0
        tn = 0
        fn = 0

        for gt_idx in range(0, len(dataset.index)):
            if dataset['max_relevance_score'].iloc[gt_idx] >= thresh:
                if dataset["reviewers_rel"].iloc[gt_idx] == 2:
                    tp = tp + 1.0
                else:
                    fp = fp + 1.0
            else:
                if dataset["reviewers_rel"].iloc[gt_idx] == 2:
                    fn = fn + 1.0
                else:
                    tn = tn + 1.0
        nyt_f1[idx, 0] = 1.0
        nyt_f1[idx, 1] = thresh
        if tp != 0:
            nyt_f1[idx, 2] = 2.0 * tp / (2.0 * tp + fp + fn)
        else:
            nyt_f1[idx, 2] = 0
    return nyt_f1

def compute_F1_score_not_relevant(dataset):
    nyt_f1 = np.zeros(shape=(100, 3))
    for idx in range(0, 100):
        thresh = (idx + 1) / 100.0
        tp = 0
        fp = 0
        tn = 0
        fn = 0

        for gt_idx in range(0, len(dataset.index)):
            if dataset['max_relevance_score'].iloc[gt_idx] <= thresh:
                if dataset["reviewers_rel"].iloc[gt_idx] == 0:
                    tp = tp + 1.0
                else:
                    fp = fp + 1.0
            else:
                if dataset["reviewers_rel"].iloc[gt_idx] == 0:
                    fn = fn + 1.0
                else:
                    tn = tn + 1.0
        nyt_f1[idx, 0] = 0.0
        nyt_f1[idx, 1] = thresh
        if tp != 0:
            nyt_f1[idx, 2] = 2.0 * tp / (2.0 * tp + fp + fn)
        else:
            nyt_f1[idx, 2] = 0
    return nyt_f1

def compute_F1_score_relevant(dataset, nyt_f1):
    for idx in range(0, 5050):
        tp = 0
        fp = 0
        tn = 0
        fn = 0
        
        for gt_idx in range(0, len(dataset.index)):
            if dataset['max_relevance_score'].iloc[gt_idx] > nyt_f1[idx, 0] and dataset['max_relevance_score'].iloc[gt_idx] < nyt_f1[idx, 1]:
                if dataset["reviewers_rel"].iloc[gt_idx] == 1:
                    tp = tp + 1.0
                else:
                    fp = fp + 1.0
            else:
                if dataset["reviewers_rel"].iloc[gt_idx] == 1:
                    fn = fn + 1.0
                else:
                    tn = tn + 1.0
        if tp != 0:
            nyt_f1[idx, 2] = 2.0 * tp / (2.0 * tp + fp + fn)
        else:
            nyt_f1[idx, 2] = 0
    return nyt_f1

idx = 0
nyt_f1 = np.zeros(shape=(5050, 3))
for idx1 in range(0, 100):
    thresh1 = (idx1) / 100.0
    for idx2 in range(idx1, 100):
        thresh2 = (idx2 + 1) /100.0
        nyt_f1[idx, 0] = thresh1
        nyt_f1[idx, 1] = thresh2
        nyt_f1[idx, 2] = 0.0
        idx = idx + 1

ordered_no_highlight = pd.read_csv("../Results/Pilot_2P-OrdPar-NoHigh/units_Pilot_2P-OrdPar-NoHigh.csv")
ordered_highlight = pd.read_csv("../Results/Pilot_2P-OrdPar-High/units_Pilot_2P-OrdPar-High.csv")
random_no_highlight = pd.read_csv("../Results/Pilot_2P-RndPar-NoHigh/units_Pilot_2P-RndPar-NoHigh.csv")
random_highlight = pd.read_csv("../Results/Pilot_2P-RndPar-High/units_Pilot_2P-RndPar-High.csv")

ordered_nohighlight_highlyrel = compute_F1_score_highly_relevant(ordered_no_highlight)
ordered_nohighlight_notrel = compute_F1_score_not_relevant(ordered_no_highlight)
ordered_nohighlight_rel = compute_F1_score_relevant(ordered_no_highlight, nyt_f1)

ordered_highlight_highlyrel = compute_F1_score_highly_relevant(ordered_highlight)
ordered_highlight_notrel = compute_F1_score_not_relevant(ordered_highlight)
ordered_highlight_rel = compute_F1_score_relevant(ordered_highlight, nyt_f1)

random_nohighlight_highlyrel = compute_F1_score_highly_relevant(random_no_highlight)
random_nohighlight_notrel = compute_F1_score_not_relevant(random_no_highlight)
random_nohighlight_rel = compute_F1_score_relevant(random_no_highlight, nyt_f1)

random_highlight_highlyrel = compute_F1_score_highly_relevant(random_highlight)
random_highlight_notrel = compute_F1_score_not_relevant(random_highlight)
random_highlight_rel = compute_F1_score_relevant(random_highlight, nyt_f1)



plt.rcParams['figure.figsize'] = 5.5, 5
fig = plt.figure()
ax = plt.axes(projection='3d')

x = random_highlight_rel[:,0]
y = random_highlight_rel[:,1]
z = random_highlight_rel[:,2]

xx, yy = np.meshgrid(x, y)

ax.plot_surface(xx, yy, z, cmap=plt.cm.Greens) #cmap=)
ax.scatter(random_highlight_notrel[:,0], random_highlight_notrel[:,1], random_highlight_notrel[:,2], c='red', marker='o')
ax.scatter(random_highlight_highlyrel[:,1], random_highlight_highlyrel[:,0], random_highlight_highlyrel[:,2], c='darkblue', marker='o')

yy, xx = np.meshgrid(range(2), range(2))

ax.plot_surface(xx, yy, 0.79, color='pink', alpha=0.95)
ax.plot_surface(xx, yy, 0.57, color='lightblue', alpha=0.95)
ax.plot_surface(xx, yy, 0.45, color='lightgreen', alpha=0.95)

ax.set_xlabel('\n\nRelevance Score\n Lower Bound')
ax.set_ylabel('\n\nRelevance Score\n Upper Bound')
ax.set_zlabel('F1 score')

ax.view_init(6, 30)

fig.tight_layout()
bbox = fig.bbox_inches.from_bounds(0.12, 0.22, 5, 3.8)
plt.savefig("../Plots/random_highlight_3values.png" , bbox_inches=bbox, format="png")
plt.show()
plt.close()


plt.rcParams['figure.figsize'] = 5.5, 5
fig = plt.figure()
ax = plt.axes(projection='3d')

x = random_nohighlight_rel[:,0]
y = random_nohighlight_rel[:,1]
z = random_nohighlight_rel[:,2]

xx, yy = np.meshgrid(x, y)

ax.plot_surface(xx, yy, z, cmap=plt.cm.Greens)
ax.scatter(random_nohighlight_notrel[:,0], random_nohighlight_notrel[:,1], random_nohighlight_notrel[:,2], c='red', marker='o')
ax.scatter(random_nohighlight_highlyrel[:,1], random_nohighlight_highlyrel[:,0], random_nohighlight_highlyrel[:,2], c='darkblue', marker='o')

yy, xx = np.meshgrid(range(2), range(2))

ax.plot_surface(xx, yy, 0.79, color='pink', alpha=0.95)
ax.plot_surface(xx, yy, 0.57, color='lightblue', alpha=0.95)
ax.plot_surface(xx, yy, 0.45, color='lightgreen', alpha=0.95)

ax.set_xlabel('\n\nRelevance Score\n Lower Bound')
ax.set_ylabel('\n\nRelevance Score\n Upper Bound')
ax.set_zlabel('F1 score')

ax.view_init(6, 30)

fig.tight_layout()
bbox = fig.bbox_inches.from_bounds(0.12, 0.22, 5, 3.8)
plt.savefig("../Plots/random_nohighlight_3values.png", bbox_inches=bbox, format="png")
plt.show()
plt.close()



plt.rcParams['figure.figsize'] = 5.5, 5
fig = plt.figure()
ax = plt.axes(projection='3d')

x = ordered_highlight_rel[:,0]
y = ordered_highlight_rel[:,1]
z = ordered_highlight_rel[:,2]

xx, yy = np.meshgrid(x, y)

ax.plot_surface(xx, yy, z, cmap=plt.cm.Greens)
ax.scatter(ordered_highlight_notrel[:,0], ordered_highlight_notrel[:,1], ordered_highlight_notrel[:,2], c='red', marker='o')
ax.scatter(ordered_highlight_highlyrel[:,1], ordered_highlight_highlyrel[:,0], ordered_highlight_highlyrel[:,2], c='darkblue', marker='o')

yy, xx = np.meshgrid(range(2), range(2))

ax.plot_surface(xx, yy, 0.79, color='pink', alpha=0.95)
ax.plot_surface(xx, yy, 0.57, color='lightblue', alpha=0.95)
ax.plot_surface(xx, yy, 0.45, color='lightgreen', alpha=0.95)

ax.set_xlabel('\n\nRelevance Score\n Lower Bound')
ax.set_ylabel('\n\nRelevance Score\n Upper Bound')
ax.set_zlabel('F1 score')

ax.view_init(6, 30)

fig.tight_layout()
bbox = fig.bbox_inches.from_bounds(0.12, 0.22, 5, 3.8)
plt.savefig("../Plots/ordered_highlight_3values.png", bbox_inches=bbox, format="png")
plt.show()
plt.close()



plt.rcParams['figure.figsize'] = 5.5, 5
fig = plt.figure()
ax = plt.axes(projection='3d')

x = ordered_nohighlight_rel[:,0]
y = ordered_nohighlight_rel[:,1]
z = ordered_nohighlight_rel[:,2]

xx, yy = np.meshgrid(x, y)

ax.plot_surface(xx, yy, z, cmap=plt.cm.Greens)
ax.scatter(ordered_nohighlight_notrel[:,0], ordered_nohighlight_notrel[:,1], ordered_nohighlight_notrel[:,2], c='red', marker='o')
ax.scatter(ordered_nohighlight_highlyrel[:,1], ordered_nohighlight_highlyrel[:,0], ordered_nohighlight_highlyrel[:,2], c='darkblue', marker='o')

yy, xx = np.meshgrid(range(2), range(2))

ax.plot_surface(xx, yy, 0.79, color='pink', alpha=0.95)
ax.plot_surface(xx, yy, 0.57, color='lightblue', alpha=0.95)
ax.plot_surface(xx, yy, 0.45, color='lightgreen', alpha=0.95)

ax.set_xlabel('\n\nRelevance Score\n Lower Bound')
ax.set_ylabel('\n\nRelevance Score\n Upper Bound')
ax.set_zlabel('F1 score')

ax.view_init(6, 30)

fig.tight_layout()
bbox = fig.bbox_inches.from_bounds(0.12, 0.22, 5, 3.8)
plt.savefig("../Plots/ordered_nohighlight_3values.png", bbox_inches=bbox, format="png")
plt.show()
plt.close()
