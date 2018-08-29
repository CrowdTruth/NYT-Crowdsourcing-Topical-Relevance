#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon May 21 12:20:12 2018

@author: oanainel
"""

import pandas as pd
import itertools as it
import random
import os
import numpy as np

import crowdtruth
from crowdtruth.configuration import DefaultConfig
import logging
import warnings; warnings.simplefilter('ignore')

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

def get_uniq_unit_ids(df):
    unique_unit_ids = df["_unit_id"].unique()
    return unique_unit_ids

def get_no_work_unit_id(df, unit_id):
    subset_unit_id = df[df["_unit_id"] == unit_id]
    return (len(subset_unit_id), subset_unit_id)	

def count_bits(number, n_bits):
    ret = 0
    bit_pos = []
    for i in xrange(0, n_bits):
        if (1 << i) & number != 0:
            ret += 1
            bit_pos.append(i)
    return (ret, bit_pos)
 	
def gen_all_k_combinations(k, num_size):
    result = []
    for i in xrange(1, 2**num_size):
        bit_count, bit_pos = count_bits(i, num_size)
        if bit_count == k:
            result.append(bit_pos)
    return result

def gen_all_worker_combinations(subset_size, count, subset_unit_id):
    combinations = gen_all_k_combinations(subset_size, count)
    final_result = []
    for comb in combinations:
        crnt_workers = []
        for j in xrange(0, len(comb)):
            crnt_workers.append(subset_unit_id["_worker_id"].iloc[comb[j]])
        final_result.append(crnt_workers)
    return final_result

def get_all_unit_combinations(unit_dict):
    sorted_unit_dict = sorted(unit_dict)
    combinations = it.product(*(unit_dict[unit_id] for unit_id in sorted_unit_dict))
    print(list(combinations))

def my_product(dicts):
    units, comb_of_workers = zip(*dicts.items())
    return [dict(zip(units, x)) for x in it.product(*comb_of_workers)]
	#return list((dict(it.izip(dicts, x)) for x in it.product(*dicts.itervalues())))

def pick_random_worker_set(worker_sets):
    return random.choice(worker_sets)

def compute_F1_score_relevant_binary(dataset):
    tp = 0
    tn = 0
    fp = 0
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


def compute_F1_score_highly_relevant_ternary(dataset):
    tp = 0
    tn = 0
    fp = 0
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



def compute_F1_score_not_relevant_ternary(dataset):
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


def compute_F1_score_relevant_ternary(dataset):
    tp = 0
    fp = 0
    tn = 0
    fn = 0
        
    for gt_idx in range(0, len(dataset.index)):
        if dataset['max_relevance_score'].iloc[gt_idx] > 0.47 and dataset['max_relevance_score'].iloc[gt_idx] < 0.63:
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

def create_analysis_files(dataset, max_no_workers, max_runs, storing_folder):
    unique_unit_ids = get_uniq_unit_ids(dataset)

    for subset_size in xrange(3, max_no_workers):
        workers_directory = storing_folder + str(subset_size) + "workers"
        if not os.path.exists(workers_directory):
            os.makedirs(workers_directory)
        
        map_unit_id_combinations = {}
        for unit_id in xrange(0, len(unique_unit_ids)):
            (count, subset_unit_id) = get_no_work_unit_id(dataset, unique_unit_ids[unit_id])
            combinations = gen_all_worker_combinations(subset_size, count, subset_unit_id)
            map_unit_id_combinations[unique_unit_ids[unit_id]] = combinations
        
        import csv   
        fields=['F1_nr_binary','F1_n_binary','F1_nr_ternary', 'F1_r_ternary', 'F1_hr_ternary']
        with open('F1_' + str(subset_size) + ".csv", 'w') as f:
            writer = csv.writer(f)
            writer.writerow(fields)
    
    
        for run_no in xrange(1, max_runs):
            unit_worker_set = {}
            for unit_id, worker_sets in map_unit_id_combinations.iteritems():
                unit_worker_set[unit_id] = pick_random_worker_set(worker_sets)
            	
            df_subset_size = pd.DataFrame()
            for unit_id, worker_set in unit_worker_set.iteritems():
                df_subset = dataset[(dataset["_unit_id"] == unit_id) & (dataset["_worker_id"].isin(worker_set))]
                frames = [df_subset_size, df_subset]
                df_subset_size = pd.concat(frames)
            
            df_subset_size.to_csv(workers_directory + "/run.csv", index=False)
            
            filename = workers_directory + "/run.csv"
            results_with_newGT = pd.read_csv("../ground_truth_data/reviewers_pilot_aggregated_judgments.csv")
            
            class config(DefaultConfig):
                inputColumns = ["index", "bin", "doc_len", "document_id", "document_body", "document_title", "rel", 
                                "topic", "topic_description", "topic_query"]
                outputColumns = ["relevant_snippets"]
                
                # processing of a closed task
                open_ended_task = True
                annotation_separator = ","
                annotation_vector = []
                
                def processJudgments(self, judgments):
                    for col in self.outputColumns:
                        judgments[col] = judgments[col].apply(lambda x: x.replace('[',''))
                        judgments[col] = judgments[col].apply(lambda x: x.replace(']',''))
                        judgments[col] = judgments[col].apply(lambda x: x.replace('"',''))
                        judgments[col] = judgments[col].apply(lambda x: x.replace(' ',','))
                    return judgments


            # Read data
            data, config = crowdtruth.load(
                file = filename,
                config = config()
            )
            
            data['judgments'].head()
            results = crowdtruth.run(data, config)
            
            results["units"]['max_relevance_score'] = pd.Series(np.random.randn(len(results["units"])), index=results["units"].index)
            for i in xrange(0, len(results["units"])):
                maxVal = 0.0
                for key, value in results["units"]["unit_annotation_score"].iloc[i].items():
                    if key != "none":
                        if value > maxVal:
                            maxVal = value
                results["units"]['max_relevance_score'].iloc[i] = maxVal

            results["units"]["reviewers_rel"] = pd.Series(np.random.randn(len(results["units"])), index=results["units"].index)
            results["units"]["reviewers_rel_merged"] = pd.Series(np.random.randn(len(results["units"])), index=results["units"].index)
            for i in xrange(0, len(results_with_newGT.index)):
                for j in xrange(0, len(results["units"].index)):
                    if (results_with_newGT["topic"].iloc[i] == results["units"]["input.topic"].iloc[j]) and (results_with_newGT["document_id"].iloc[i] == results["units"]["input.document_id"].iloc[j]):
                        results["units"]["reviewers_rel"].iloc[j] = results_with_newGT["reviewers_rel"].iloc[i]
                        results["units"]["reviewers_rel_merged"].iloc[j] = results_with_newGT["reviewers_rel_merged"].iloc[i]


            F1_notrelevant_binary = compute_F1_score_not_relevant_binary(results["units"])
            F1_relevant_binary = compute_F1_score_relevant_binary(results["units"])
            
            F1_notrelevant_ternary = compute_F1_score_not_relevant_ternary(results["units"])
            F1_relevant_ternary = compute_F1_score_relevant_ternary(results["units"])
            F1_highlyrelevant_ternary = compute_F1_score_highly_relevant_ternary(results["units"])

            row = [F1_notrelevant_binary, F1_relevant_binary, F1_notrelevant_ternary, F1_relevant_ternary, F1_highlyrelevant_ternary]
            with open('F1_' + str(subset_size) + ".csv", 'a') as f:
                writer = csv.writer(f)
                writer.writerow(row)
            
storing_folder = "../Results/Pilot_2P-RndPar-High/"
file_name = "2p_withHighlight_15workers_passages.csv"
dataset = pd.read_csv(storing_folder + file_name)
max_no_workers = 15
max_runs = 100

create_analysis_files(dataset, max_no_workers, max_runs, storing_folder)         
            