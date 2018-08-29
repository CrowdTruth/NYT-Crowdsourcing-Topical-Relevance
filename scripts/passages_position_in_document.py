#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 20:32:23 2018

@author: oanainel
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

gt = pd.read_csv("../ground_truth_data/reviewers_pilot_aggregated_judgments.csv")
random_highlight_20 = pd.read_csv("../Results/Pilot_2P-RndPar-High/units_Pilot_2P-RndPar-High.csv")
random_highlight_19 = pd.read_csv("../Results/Pilot_2P-RndPar-High/units_withHighlight_15workers_2p_passages_max19.csv")
random_highlight_18 = pd.read_csv("../Results/Pilot_2P-RndPar-High/units_withHighlight_15workers_2p_passages_max18.csv")
random_highlight_17 = pd.read_csv("../Results/Pilot_2P-RndPar-High/units_withHighlight_15workers_2p_passages_max17.csv")
random_highlight_16 = pd.read_csv("../Results/Pilot_2P-RndPar-High/units_withHighlight_15workers_2p_passages_max16.csv")
random_highlight_15 = pd.read_csv("../Results/Pilot_2P-RndPar-High/units_withHighlight_15workers_2p_passages_max15.csv")
random_highlight_14 = pd.read_csv("../Results/Pilot_2P-RndPar-High/units_withHighlight_15workers_2p_passages_max14.csv")
random_highlight_13 = pd.read_csv("../Results/Pilot_2P-RndPar-High/units_withHighlight_15workers_2p_passages_max13.csv")
random_highlight_12 = pd.read_csv("../Results/Pilot_2P-RndPar-High/units_withHighlight_15workers_2p_passages_max12.csv")
random_highlight_11 = pd.read_csv("../Results/Pilot_2P-RndPar-High/units_withHighlight_15workers_2p_passages_max11.csv")
random_highlight_10 = pd.read_csv("../Results/Pilot_2P-RndPar-High/units_withHighlight_15workers_2p_passages_max10.csv")
random_highlight_9 = pd.read_csv("../Results/Pilot_2P-RndPar-High/units_withHighlight_15workers_2p_passages_max9.csv")
random_highlight_8 = pd.read_csv("../Results/Pilot_2P-RndPar-High/units_withHighlight_15workers_2p_passages_max8.csv")
random_highlight_7 = pd.read_csv("../Results/Pilot_2P-RndPar-High/units_withHighlight_15workers_2p_passages_max7.csv")
random_highlight_6 = pd.read_csv("../Results/Pilot_2P-RndPar-High/units_withHighlight_15workers_2p_passages_max6.csv")
random_highlight_5 = pd.read_csv("../Results/Pilot_2P-RndPar-High/units_withHighlight_15workers_2p_passages_max5.csv")
random_highlight_4 = pd.read_csv("../Results/Pilot_2P-RndPar-High/units_withHighlight_15workers_2p_passages_max4.csv")
random_highlight_3 = pd.read_csv("../Results/Pilot_2P-RndPar-High/units_withHighlight_15workers_2p_passages_max3.csv")
random_highlight_2 = pd.read_csv("../Results/Pilot_2P-RndPar-High/units_withHighlight_15workers_2p_passages_max2.csv")
random_highlight_1 = pd.read_csv("../Results/Pilot_2P-RndPar-High/units_withHighlight_15workers_2p_passages_max1.csv")


def compute_F1_score_relevant_binary(dataset):
    nyt_f1 = 0.0   
    tp = 0
    fp = 0
    tn = 0
    fn = 0

    for gt_idx in range(0, len(dataset.index)):
        if dataset['max_relevance_score'].iloc[gt_idx] >= 0.47:
            if dataset["reviewers_rel_merged"].iloc[gt_idx] == 1:
                tp = tp + 1.0
            else:
                fp = fp + 1.0
        else:
            if dataset["reviewers_rel_merged"].iloc[gt_idx] == 1:
                fn = fn + 1.0
            else:
                tn = tn + 1.0

    if tp != 0:
        nyt_f1 = 2.0 * tp / (2.0 * tp + fp + fn)
    else:
        nyt_f1 = 0
    return nyt_f1


def compute_F1_score_not_relevant_binary(dataset):
    nyt_f1 = 0.0
    tp = 0
    fp = 0
    tn = 0
    fn = 0

    for gt_idx in range(0, len(dataset.index)):
        if dataset['max_relevance_score'].iloc[gt_idx] < 0.47:
            if dataset["reviewers_rel_merged"].iloc[gt_idx] == 0:
                tp = tp + 1.0
            else:
                fp = fp + 1.0
        else:
            if dataset["reviewers_rel_merged"].iloc[gt_idx] == 0:
                fn = fn + 1.0
            else:
                tn = tn + 1.0

    if tp != 0:
        nyt_f1 = 2.0 * tp / (2.0 * tp + fp + fn)
    else:
        nyt_f1 = 0
    return nyt_f1


r1_nr = compute_F1_score_not_relevant_binary(random_highlight_1)
r1_r = compute_F1_score_relevant_binary(random_highlight_1)
r2_nr = compute_F1_score_not_relevant_binary(random_highlight_2)
r2_r = compute_F1_score_relevant_binary(random_highlight_2)
r3_nr = compute_F1_score_not_relevant_binary(random_highlight_3)
r3_r = compute_F1_score_relevant_binary(random_highlight_3)
r4_nr = compute_F1_score_not_relevant_binary(random_highlight_4)
r4_r = compute_F1_score_relevant_binary(random_highlight_4)
r5_nr = compute_F1_score_not_relevant_binary(random_highlight_5)
r5_r = compute_F1_score_relevant_binary(random_highlight_5)
r6_nr = compute_F1_score_not_relevant_binary(random_highlight_6)
r6_r = compute_F1_score_relevant_binary(random_highlight_6)
r7_nr = compute_F1_score_not_relevant_binary(random_highlight_7)
r7_r = compute_F1_score_relevant_binary(random_highlight_7)
r8_nr = compute_F1_score_not_relevant_binary(random_highlight_8)
r8_r = compute_F1_score_relevant_binary(random_highlight_8)
r9_nr = compute_F1_score_not_relevant_binary(random_highlight_9)
r9_r = compute_F1_score_relevant_binary(random_highlight_9)
r10_nr = compute_F1_score_not_relevant_binary(random_highlight_10)
r10_r = compute_F1_score_relevant_binary(random_highlight_10)
r11_nr = compute_F1_score_not_relevant_binary(random_highlight_11)
r11_r = compute_F1_score_relevant_binary(random_highlight_11)
r12_nr = compute_F1_score_not_relevant_binary(random_highlight_12)
r12_r = compute_F1_score_relevant_binary(random_highlight_12)
r13_nr = compute_F1_score_not_relevant_binary(random_highlight_13)
r13_r = compute_F1_score_relevant_binary(random_highlight_13)
r14_nr = compute_F1_score_not_relevant_binary(random_highlight_14)
r14_r = compute_F1_score_relevant_binary(random_highlight_14)
r15_nr = compute_F1_score_not_relevant_binary(random_highlight_15)
r15_r = compute_F1_score_relevant_binary(random_highlight_15)
r16_nr = compute_F1_score_not_relevant_binary(random_highlight_16)
r16_r = compute_F1_score_relevant_binary(random_highlight_16)
r17_nr = compute_F1_score_not_relevant_binary(random_highlight_17)
r17_r = compute_F1_score_relevant_binary(random_highlight_17)
r18_nr = compute_F1_score_not_relevant_binary(random_highlight_18)
r18_r = compute_F1_score_relevant_binary(random_highlight_18)
r19_nr = compute_F1_score_not_relevant_binary(random_highlight_19)
r19_r = compute_F1_score_relevant_binary(random_highlight_19)
r20_nr = compute_F1_score_not_relevant_binary(random_highlight_20)
r20_r = compute_F1_score_relevant_binary(random_highlight_20)

rel = [r1_r, r2_r, r3_r, r4_r, r5_r, r6_r, r7_r, r8_r, r9_r, r10_r, r11_r, r12_r, r13_r, r14_r, r15_r, r16_r, r17_r, r18_r, r19_r, r20_r]
notrel = [r1_nr, r2_nr, r3_nr, r4_nr, r5_nr, r6_nr, r7_nr, r8_nr, r9_nr, r10_nr, r11_nr, r12_nr, r13_nr, r14_nr, r15_nr, r16_nr, r17_nr, r18_nr, r19_nr, r20_nr]

print(rel)
expert_nr = 0.79
expert_r = 0.80
cols = ['p1', 'p2', 'p3', 'p4', 'p5', 'p6', 'p7', 'p8', 'p9', 'p10', 'p11', 'p12', 'p13', 'p14', 'p15', 'p16', 'p17', 'p18', 'p19', 'p20']
xticks = [1, 2, 3, 4, 5, 6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
plt.rcParams['figure.figsize'] = 6, 4
plt.plot(xticks, notrel, 'bo-', color = 'red', lw = 2, label = "F1 Crowd - Not Relevant")
plt.plot(xticks, rel, 'bo-', color = 'darkgreen', lw = 2, label = "F1 Crowd - Relevant")

plt.axhline(y = expert_nr, ls = '-', color = 'salmon', lw = 2, label = "F1 NIST - Not Relevant")
plt.axhline(y = expert_r, ls = '--', color = 'lightgreen', lw = 2, label = "F1 NIST - Relevant")


plt.xticks(xticks, cols, rotation=45, fontsize=16)
plt.xlabel("paragraph index", fontsize=20)
plt.ylabel("F1-score", fontsize=20)
plt.yticks(fontsize=20)
plt.legend()
plt.ylim(0.0, 1.0)
leg = plt.legend(fontsize=14)
leg.get_frame().set_alpha(0.5)
plt.grid(ls=':')
plt.savefig("../Plots/paragraph_position_2prhighlight.png", bbox_inches='tight', format='png', dpi=1000, rasterized=True)
plt.show()
plt.close()    


def compute_F1_score_highlyrelevant(dataset):
    nyt_f1 = 0.0   
    tp = 0
    fp = 0
    tn = 0
    fn = 0

    for gt_idx in range(0, len(dataset.index)):
        if dataset['max_relevance_score'].iloc[gt_idx] >= 0.63:
            if dataset["reviewers_rel"].iloc[gt_idx] == 2:
                tp = tp + 1.0
            else:
                fp = fp + 1.0
        else:
            if dataset["reviewers_rel"].iloc[gt_idx] == 2:
                fn = fn + 1.0
            else:
                tn = tn + 1.0

    if tp != 0:
        nyt_f1 = 2.0 * tp / (2.0 * tp + fp + fn)
    else:
        nyt_f1 = 0
    return nyt_f1


def compute_F1_score_not_relevant(dataset):
    nyt_f1 = 0.0
    tp = 0
    fp = 0
    tn = 0
    fn = 0

    for gt_idx in range(0, len(dataset.index)):
        if dataset['max_relevance_score'].iloc[gt_idx] <= 0.47:
            if dataset["reviewers_rel"].iloc[gt_idx] == 0:
                tp = tp + 1.0
            else:
                fp = fp + 1.0
        else:
            if dataset["reviewers_rel"].iloc[gt_idx] == 0:
                fn = fn + 1.0
            else:
                tn = tn + 1.0

    if tp != 0:
        nyt_f1 = 2.0 * tp / (2.0 * tp + fp + fn)
    else:
        nyt_f1 = 0
    return nyt_f1


def compute_F1_score_relevant(dataset):
    nyt_f1 = 0.0
    tp = 0
    fp = 0
    tn = 0
    fn = 0

    for gt_idx in range(0, len(dataset.index)):
        if dataset['max_relevance_score'].iloc[gt_idx] >= 0.47 and dataset['max_relevance_score'].iloc[gt_idx] <= 0.63:
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
        nyt_f1 = 2.0 * tp / (2.0 * tp + fp + fn)
    else:
        nyt_f1 = 0
    return nyt_f1


r1_nr = compute_F1_score_not_relevant(random_highlight_1)
r1_r = compute_F1_score_relevant(random_highlight_1)
r1_hr = compute_F1_score_highlyrelevant(random_highlight_1)

r2_nr = compute_F1_score_not_relevant(random_highlight_2)
r2_r = compute_F1_score_relevant(random_highlight_2)
r2_hr = compute_F1_score_highlyrelevant(random_highlight_2)

r3_nr = compute_F1_score_not_relevant(random_highlight_3)
r3_r = compute_F1_score_relevant(random_highlight_3)
r3_hr = compute_F1_score_highlyrelevant(random_highlight_3)

r4_nr = compute_F1_score_not_relevant(random_highlight_4)
r4_r = compute_F1_score_relevant(random_highlight_4)
r4_hr = compute_F1_score_highlyrelevant(random_highlight_4)

r5_nr = compute_F1_score_not_relevant(random_highlight_5)
r5_r = compute_F1_score_relevant(random_highlight_5)
r5_hr = compute_F1_score_highlyrelevant(random_highlight_5)

r6_nr = compute_F1_score_not_relevant(random_highlight_6)
r6_r = compute_F1_score_relevant(random_highlight_6)
r6_hr = compute_F1_score_highlyrelevant(random_highlight_6)

r7_nr = compute_F1_score_not_relevant(random_highlight_7)
r7_r = compute_F1_score_relevant(random_highlight_7)
r7_hr = compute_F1_score_highlyrelevant(random_highlight_7)

r8_nr = compute_F1_score_not_relevant(random_highlight_8)
r8_r = compute_F1_score_relevant(random_highlight_8)
r8_hr = compute_F1_score_highlyrelevant(random_highlight_8)

r9_nr = compute_F1_score_not_relevant(random_highlight_9)
r9_r = compute_F1_score_relevant(random_highlight_9)
r9_hr = compute_F1_score_highlyrelevant(random_highlight_9)

r10_nr = compute_F1_score_not_relevant(random_highlight_10)
r10_r = compute_F1_score_relevant(random_highlight_10)
r10_hr = compute_F1_score_highlyrelevant(random_highlight_10)

r11_nr = compute_F1_score_not_relevant(random_highlight_11)
r11_r = compute_F1_score_relevant(random_highlight_11)
r11_hr = compute_F1_score_highlyrelevant(random_highlight_11)

r12_nr = compute_F1_score_not_relevant(random_highlight_12)
r12_r = compute_F1_score_relevant(random_highlight_12)
r12_hr = compute_F1_score_highlyrelevant(random_highlight_12)

r13_nr = compute_F1_score_not_relevant(random_highlight_13)
r13_r = compute_F1_score_relevant(random_highlight_13)
r13_hr = compute_F1_score_highlyrelevant(random_highlight_13)

r14_nr = compute_F1_score_not_relevant(random_highlight_14)
r14_r = compute_F1_score_relevant(random_highlight_14)
r14_hr = compute_F1_score_highlyrelevant(random_highlight_14)

r15_nr = compute_F1_score_not_relevant(random_highlight_15)
r15_r = compute_F1_score_relevant(random_highlight_15)
r15_hr = compute_F1_score_highlyrelevant(random_highlight_15)

r16_nr = compute_F1_score_not_relevant(random_highlight_16)
r16_r = compute_F1_score_relevant(random_highlight_16)
r16_hr = compute_F1_score_highlyrelevant(random_highlight_16)

r17_nr = compute_F1_score_not_relevant(random_highlight_17)
r17_r = compute_F1_score_relevant(random_highlight_17)
r17_hr = compute_F1_score_highlyrelevant(random_highlight_17)

r18_nr = compute_F1_score_not_relevant(random_highlight_18)
r18_r = compute_F1_score_relevant(random_highlight_18)
r18_hr = compute_F1_score_highlyrelevant(random_highlight_18)

r19_nr = compute_F1_score_not_relevant(random_highlight_19)
r19_r = compute_F1_score_relevant(random_highlight_19)
r19_hr = compute_F1_score_highlyrelevant(random_highlight_19)

r20_nr = compute_F1_score_not_relevant(random_highlight_20)
r20_r = compute_F1_score_relevant(random_highlight_20)
r20_hr = compute_F1_score_highlyrelevant(random_highlight_20)

rel = [r1_r, r2_r, r3_r, r4_r, r5_r, r6_r, r7_r, r8_r, r9_r, r10_r, r11_r, r12_r, r13_r, r14_r, r15_r, r16_r, r17_r, r18_r, r19_r, r20_r]
notrel = [r1_nr, r2_nr, r3_nr, r4_nr, r5_nr, r6_nr, r7_nr, r8_nr, r9_nr, r10_nr, r11_nr, r12_nr, r13_nr, r14_nr, r15_nr, r16_nr, r17_nr, r18_nr, r19_nr, r20_nr]
hrel = [r1_hr, r2_hr, r3_hr, r4_hr, r5_hr, r6_hr, r7_hr, r8_hr, r9_hr, r10_hr, r11_hr, r12_hr, r13_hr, r14_hr, r15_hr, r16_hr, r17_hr, r18_hr, r19_hr, r20_hr]

expert_nr = 0.79
expert_r = 0.45
expert_hr = 0.57
cols = ['p1', 'p2', 'p3', 'p4', 'p5', 'p6', 'p7', 'p8', 'p9', 'p10', 'p11', 'p12', 'p13', 'p14', 'p15', 'p16', 'p17', 'p18', 'p19', 'p20']
xticks = [1, 2, 3, 4, 5, 6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
plt.rcParams['figure.figsize'] = 6, 4
plt.plot(xticks, notrel, 'bo-', color = 'red', lw = 2, label = "F1 Crowd - Not Relevant")
plt.plot(xticks, rel, 'bo-', color = 'darkgreen', lw = 2, label = "F1 Crowd - Relevant")
plt.plot(xticks, hrel, 'bo-', color = 'darkblue', lw = 2, label = "F1 Crowd - Highly Relevant")

plt.axhline(y = expert_nr, ls = '--', color = 'salmon', lw = 2, label = "F1 NIST - Not Relevant")
plt.axhline(y = expert_r, ls = '--', color = 'lightgreen', lw = 2, label = "F1 NIST - Relevant")
plt.axhline(y = expert_hr, ls = '--', color = 'lightblue', lw = 2, label = "F1 NIST - Highly Relevant")


plt.xticks(xticks, cols, rotation=45, fontsize=16)
plt.xlabel("paragraph index", fontsize=20)
plt.ylabel("F1-score", fontsize=20)
plt.yticks(fontsize=20)
plt.legend(fontsize=14)
plt.ylim(0.0, 1.0)
leg = plt.legend()
leg.get_frame().set_alpha(0.5)
plt.grid(ls=':')
plt.savefig("../Plots/paragraph_position_3prhighlight.png", bbox_inches='tight', format='png', dpi=1000, rasterized=True)
plt.show()
plt.close()  
