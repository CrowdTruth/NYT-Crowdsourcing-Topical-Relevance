# QRELS - Crowdsourcing Topical Relevance

This folder contains the raw crowdsourcing data for topical relevance over 23.554 documents and 250 topics provided during the TREC Core Track 2017. The crowdsourcing data was processed with the **[CrowdTruth](http://crowdtruth.org/)** metrics. 

The folder contains the following data:

* raw crowdsourcing data: `qrels\crowd_raw_data`

* binary and ternary qrels using the CrowdTruth aggregation method: `qrels\qrels_crowd_CT`

The 23.554 documents were selected from the documents of the participating teams in the TREC 2017 Core Track. For this crowdsourcing experiment we selected only short documents (we express the document length as bins). Our dataset contains *10.979* documents in bin1, having between 0 and 500 words and *12.575* documents in bin2 having between 501 and 1000 words. 

