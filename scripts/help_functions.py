import numpy as np

def compute_F1_score(dataset, gt_value, label, gt_column):
    nyt_f1 = np.zeros(shape=(10, 2))
    for idx in xrange(0, 10):
        thresh = (idx + 1) / 10.0
        tp = 0
        fp = 0
        tn = 0
        fn = 0

        for gt_idx in range(0, len(dataset.index)):
            #print(gt_idx)
            #print(dataset['unit_annotation_score'].iloc[gt_idx])
            if dataset['unit_annotation_score'].iloc[gt_idx][label] >= thresh:
                if dataset[gt_column].iloc[gt_idx] == gt_value:
                    tp = tp + 1.0
                else:
                    fp = fp + 1.0
            else:
                if dataset[gt_column].iloc[gt_idx] == gt_value:
                    fn = fn + 1.0
                else:
                    tn = tn + 1.0

        nyt_f1[idx, 0] = thresh
	if tp != 0:
        	nyt_f1[idx, 1] = 2.0 * tp / (2.0 * tp + fp + fn)
	else:
		nyt_f1[idx, 1] = 0
    return nyt_f1

def compute_F1_score_relevant(dataset):
    nyt_f1 = np.zeros(shape=(100, 2))
    for idx in xrange(0, 100):
        thresh = (idx + 1) / 100.0
        tp = 0
        fp = 0
        tn = 0
        fn = 0

        for gt_idx in range(0, len(dataset.index)):
            #print(gt_idx)
            #print(dataset['unit_annotation_score'].iloc[gt_idx])
            if dataset['unit_annotation_score'].iloc[gt_idx]["relevant"] >= thresh:
                if dataset["reviewers_rel_merged"].iloc[gt_idx] == 1:
                    tp = tp + 1.0
                else:
                    fp = fp + 1.0
            else:
                if dataset["reviewers_rel_merged"].iloc[gt_idx] == 1:
                    fn = fn + 1.0
                else:
                    tn = tn + 1.0

        nyt_f1[idx, 0] = thresh
        if tp != 0:
            nyt_f1[idx, 1] = 2.0 * tp / (2.0 * tp + fp + fn)
        else:
            nyt_f1[idx, 1] = 0
    return nyt_f1


def compute_F1_score_not_relevant(dataset):
    nyt_f1 = np.zeros(shape=(100, 2))
    for idx in xrange(0, 100):
        thresh = (idx + 1) / 100.0
        tp = 0
        fp = 0
        tn = 0
        fn = 0

        for gt_idx in range(0, len(dataset.index)):
            #print(gt_idx)
            #print(dataset['unit_annotation_score'].iloc[gt_idx])
            if dataset['unit_annotation_score'].iloc[gt_idx]["relevant"] <= thresh:
                if dataset["reviewers_rel_merged"].iloc[gt_idx] == 0:
                    tp = tp + 1.0
                else:
                    fp = fp + 1.0
            else:
                if dataset["reviewers_rel_merged"].iloc[gt_idx] == 0:
                    fn = fn + 1.0
                else:
                    tn = tn + 1.0

        nyt_f1[idx, 0] = thresh
        if tp != 0:
            nyt_f1[idx, 1] = 2.0 * tp / (2.0 * tp + fp + fn)
        else:
            nyt_f1[idx, 1] = 0
    return nyt_f1

def compute_R(dataset, gt_value, label, gt_column):
    nyt_r = np.zeros(shape=(10, 2))
    for idx in xrange(0, 10):
        thresh = (idx + 1) / 10.0
        tp = 0
        fp = 0
        tn = 0
        fn = 0

        for gt_idx in range(0, len(dataset.index)):
            if dataset['unit_annotation_score'].iloc[gt_idx][label] >= thresh:
                if dataset[gt_column].iloc[gt_idx] == gt_value:
                    tp = tp + 1.0
                else:
                    fp = fp + 1.0
            else:
                if dataset[gt_column].iloc[gt_idx] == gt_value:
                    fn = fn + 1.0
                else:
                    tn = tn + 1.0

        nyt_r[idx, 0] = thresh
	if tp != 0:
        	nyt_r[idx, 1] = tp / (tp + fn)
	else:
		nyt_r[idx, 1] = 0
    return nyt_r
                 
def compute_F1_score_experts(dataset, label_value):
    nyt_f1 = 0
    tp = 0
    fp = 0
    tn = 0
    fn = 0

    for gt_idx in range(0, len(dataset.index)):
        if dataset['reviewers_rel'].iloc[gt_idx] == label_value:
            if dataset['input.rel'].iloc[gt_idx] == label_value:
                tp = tp + 1.0
            else:
                fn = fn + 1.0
        else:
            if dataset['input.rel'].iloc[gt_idx] == label_value:
                fp = fp + 1.0
            else:
                tn = tn + 1.0

    nyt_f1 = 2.0 * tp / (2.0 * tp + fp + fn)
    return nyt_f1

def compute_F1_score_experts_merged(dataset, label_value):
    nyt_f1 = 0
    tp = 0
    fp = 0
    tn = 0
    fn = 0

    for gt_idx in range(0, len(dataset.index)):
        if dataset['reviewers_rel_merged'].iloc[gt_idx] == label_value:
            if dataset['rel_merged'].iloc[gt_idx] == label_value:
                tp = tp + 1.0
            else:
                fn = fn + 1.0
        else:
            if dataset['rel_merged'].iloc[gt_idx] == label_value:
                fp = fp + 1.0
            else:
                tn = tn + 1.0

    nyt_f1 = 2.0 * tp / (2.0 * tp + fp + fn)
    return nyt_f1

def compute_F1_score_experts_2p(dataset, label_value):
    nyt_f1 = 0
    tp = 0
    fp = 0
    tn = 0
    fn = 0
    for gt_idx in range(0, len(dataset.index)):
        if dataset['eval_gt_merged'].iloc[gt_idx] == label_value:
            if dataset['initial_gt_merged'].iloc[gt_idx] == label_value:
                tp = tp + 1.0
            else:
                fn = fn + 1.0
        else:
            if dataset['initial_gt_merged'].iloc[gt_idx] == label_value:
                fp = fp + 1.0
            else:
                tn = tn + 1.0

    nyt_f1 = 2.0 * tp / (2.0 * tp + fp + fn)
    return nyt_f1

def compute_A(dataset, gt_value, label, gt_column):
    nyt_a = np.zeros(shape=(10, 2))
    for idx in xrange(0, 10):
        thresh = (idx + 1) / 10.0
        tp = 0
        fp = 0
        tn = 0
        fn = 0

        for gt_idx in range(0, len(dataset.index)):
            if dataset['unit_annotation_score'].iloc[gt_idx][label] >= thresh:
                if dataset[gt_column].iloc[gt_idx] == gt_value:
                    tp = tp + 1.0
                else:
                    fp = fp + 1.0
            else:
                if dataset[gt_column].iloc[gt_idx] == gt_value:
                    fn = fn + 1.0
                else:
                    tn = tn + 1.0

        nyt_a[idx, 0] = thresh
        nyt_a[idx, 1] = (tp + tn) / (tp + tn + fp + fn)
    return nyt_a

def compute_A_experts(dataset, label_value):
    nyt_a = 0
    tp = 0
    fp = 0
    tn = 0
    fn = 0

    for gt_idx in range(0, len(dataset.index)):
        if dataset['eval_gt'].iloc[gt_idx] == label_value:
            if dataset['input.rel'].iloc[gt_idx] == label_value:
                tp = tp + 1.0
            else:
                fn = fn + 1.0
        else:
            if dataset['input.rel'].iloc[gt_idx] == label_value:
                fp = fp + 1.0
            else:
                tn = tn + 1.0

    nyt_a = (tp + tn) / (tp + tn + fp + fn)
    return nyt_a


def compute_P(dataset, gt_value, label, gt_column):
    nyt_p = np.zeros(shape=(10, 2))
    for idx in xrange(0, 10):
        thresh = (idx + 1) / 10.0
        tp = 0
        fp = 0
        tn = 0
        fn = 0

        for gt_idx in range(0, len(dataset.index)):
            if dataset['unit_annotation_score'].iloc[gt_idx][label] >= thresh:
                if dataset[gt_column].iloc[gt_idx] == gt_value:
                    tp = tp + 1.0
                else:
                    fp = fp + 1.0
            else:
                if dataset[gt_column].iloc[gt_idx] == gt_value:
                    fn = fn + 1.0
                else:
                    tn = tn + 1.0

        nyt_p[idx, 0] = thresh
	if tp != 0:
        	nyt_p[idx, 1] = tp / (tp + fp)
	else:
		nyt_p[idx, 1] = 0
		
    return nyt_p

