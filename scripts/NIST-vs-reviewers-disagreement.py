#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 16:41:55 2018

@author: oanainel
"""

import pandas as pd
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt

import numpy as np
import itertools


def plot_confusion_matrix(cm, classes,
                          normalize=False,
                          cmap=plt.cm.Blues):

    print(cm)

    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45, fontsize=11)
    plt.yticks(tick_marks, classes, fontsize=11)

    fmt = '.2f' if normalize else 'd'
    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, format(cm[i, j], fmt),
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black", fontsize=14)

    plt.tight_layout()
    plt.ylabel('NIST Relevance', fontsize=12)
    plt.xlabel('Reviewers Relevance', fontsize=12)

# Compute confusion matrix
dataset = pd.read_csv("../ground_truth_data/reviewers_pilot_aggregated_judgments.csv")

y_test = dataset['nist_rel']
y_pred = dataset['reviewers_rel']

class_names = ['Highly Relevant', 'Relevant', 'Not Relevant']

cnf_matrix = confusion_matrix(y_test, y_pred, labels=[2,1,0])

np.set_printoptions(precision=2)

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

# Plot non-normalized confusion matrix
plt.figure()
plot_confusion_matrix(cnf_matrix, classes=class_names)
plt.tight_layout()
plt.savefig("../Plots/confusion_matrix_expert_sample.pdf", bbox_inches='tight', format='pdf', dpi=1000)

plt.show()


'''
Compute inter-rater agreement.
'''

reviewers_annotations = pd.read_csv("../ground_truth_data/reviewers_pilot_independent_judgments.csv")

def fleiss_kappa(M):
  """
  See `Fleiss' Kappa <https://en.wikipedia.org/wiki/Fleiss%27_kappa>`_.
  :param M: a matrix of shape (:attr:`N`, :attr:`k`) where `N` is the number of subjects and `k` is the number of categories into which assignments are made. `M[i, j]` represent the number of raters who assigned the `i`th subject to the `j`th category.
  :type M: numpy matrix
  """
  N, k = M.shape  # N is # of items, k is # of categories
  n_annotators = float(np.sum(M[0, :]))  # # of annotators

  p = np.sum(M, axis=0) / (N * n_annotators)
  P = (np.sum(M * M, axis=1) - n_annotators) / (n_annotators * (n_annotators - 1))
  Pbar = np.sum(P) / N
  PbarE = np.sum(p * p)

  kappa = (Pbar - PbarE) / (1 - PbarE)

  return kappa

unit_ids = list(reviewers_annotations["_unit_id"].unique())

M = np.zeros((120,3))

for i in range(len(unit_ids)):
    subset = reviewers_annotations[reviewers_annotations["_unit_id"] == unit_ids[i]]
    
    for j in range(len(subset.index)):
        if subset["relevance"].iloc[j] == "highly_relevant":
            M[i,0] = M[i,0] + 1
        if subset["relevance"].iloc[j] == "relevant":
            M[i,1] = M[i,1] + 1
        if subset["relevance"].iloc[j] == "not_relevant":
            M[i,2] = M[i,2] + 1

print("initial agreement among reviewers - ternary: ", fleiss_kappa(M)  ) 


M = np.zeros((120,3))

for i in range(len(unit_ids)):
    #print(i)
    subset = reviewers_annotations[reviewers_annotations["_unit_id"] == unit_ids[i]]
    
    for j in range(len(subset.index)):
        if subset["new_relevance"].iloc[j] == "highly_relevant":
            M[i,0] = M[i,0] + 1
        if subset["new_relevance"].iloc[j] == "relevant":
            M[i,1] = M[i,1] + 1
        if subset["new_relevance"].iloc[j] == "not_relevant":
            M[i,2] = M[i,2] + 1

print("agreement after discussion among reviewers - ternary:", fleiss_kappa(M)  ) 


M= np.zeros((120,2))

for i in range(len(unit_ids)):
    #print(i)
    subset = reviewers_annotations[reviewers_annotations["_unit_id"] == unit_ids[i]]
    
    for j in range(len(subset.index)):
        if subset["relevance"].iloc[j] == "highly_relevant":
            M[i,0] = M[i,0] + 1
        if subset["relevance"].iloc[j] == "relevant":
            M[i,0] = M[i,0] + 1
        if subset["relevance"].iloc[j] == "not_relevant":
            M[i,1] = M[i,1] + 1

print("initial agreement among reviewers - binary: ", fleiss_kappa(M)  ) 


M = np.zeros((120,3))

for i in range(len(unit_ids)):
    #print(i)
    subset = reviewers_annotations[reviewers_annotations["_unit_id"] == unit_ids[i]]
    
    for j in range(len(subset.index)):
        if subset["new_relevance"].iloc[j] == "highly_relevant":
            M[i,0] = M[i,0] + 1
        if subset["new_relevance"].iloc[j] == "relevant":
            M[i,0] = M[i,0] + 1
        if subset["new_relevance"].iloc[j] == "not_relevant":
            M[i,1] = M[i,1] + 1

print("agreement after discussion among reviewers - binary: ", fleiss_kappa(M)  ) 


all_assessments = pd.read_csv("../ground_truth_data/reviewers_pilot_aggregated_judgments.csv")

from sklearn.metrics import cohen_kappa_score
labeler1 = list(all_assessments["nist_rel"])
labeler2 = list(all_assessments["reviewers_old_rel"])
print("initial reviewers relevance annotations and NIST - ternary: ", cohen_kappa_score(labeler1, labeler2))

labeler1 = list(all_assessments["nist_rel"])
labeler2 = list(all_assessments["reviewers_rel"])
print("final reviewers relevance annotations and NIST - ternary: ", cohen_kappa_score(labeler1, labeler2))

labeler1 = list(all_assessments["nist_rel_merged"])
labeler2 = list(all_assessments["reviewers_old_rel_merged"])
print("initial reviewers relevance annotations and NIST - binary: ", cohen_kappa_score(labeler1, labeler2))

labeler1 = list(all_assessments["nist_rel_merged"])
labeler2 = list(all_assessments["reviewers_rel_merged"])
print("final reviewers relevance annotations and NIST - binary: ", cohen_kappa_score(labeler1, labeler2))