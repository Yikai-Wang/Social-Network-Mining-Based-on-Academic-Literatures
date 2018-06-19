# Introduction

This is our final project for Social network mining(DATA130007) in Fudan university. 

# Task Review

###### Task 1

Design clustering algorithms or community mining algorithms to cluster all the papers in the data set. Use visualize tools to show all fields (ie, communities, identify corresponding community research topics), and highlight the most influential scholars in each field.

###### Task 2

Realization of demonstrating the ego-network to any input scholar (refer to the function example on the ArnetMiner website).

###### Task 3

Use the data provided by DBLP and ArnetMiner to analyze and model more social relationships among scholars, such as predicting the cooperation or citation relationship between two scholars, and predicting which conference will a scholar publish papers on in the future.

# Division of work

## [Yikai Wang](https://github.com/Wang-Yikai)

In brief, he applies several methods in network representation learning and uses and expands a hierarchical representation learning algorithm(HARP) for Networks. For homogeneous networks, he mainly uses deepwalk, node2vec and LINE. For heterogeneous networks, he uses metapath2vec++. For task 1, he uses both homogeneous NRL and heterogeneous NRL methods to extract features for clustering and uses KMeans and Birch to complete the clustering task. For task 3, he uses heterogeneous NRL methods to generate the vector representation of scholar cooperation network, scholar citation network and scholar-conference network.

## [Dan Wu](https://github.com/WuDan0399)

She revises the preprocessing part of word2vec model in task 1. (Stop words deleted, all words are transformed into lower case.) A LDA model is built by her to get the key words of each group of the papers in task 1. She uses PageRank index to calculate the influence of each paper and scholar, then visualize  the citation and cooperative relationship in task 1.
Aisualize the ego-network in task 2.
 Vnisualize the ego-network in task 2.
 Voisualize the ego-network in task 2.
 Vtisualize the ego-network in task 2.
 Vhisualize the ego-network in task 2.
 Verisualize the ego-network in task 2.
 V isualize the ego-network in task 2.
 Visualize the ego-network in task 2.
5. Build a baseline model for link prediction in task 3.

## [Zheng Wei](https://github.com/WZ-ZXY)

In this project, his work is mainly divided into two part: For task1, he uses the word vector file to train the sentence vector of each paper, and he is responsible for generating small data sets for testing. For task3, he uses the MDP model to train the transition matrix and predicts the relationship between scholars and conferences. Based on this, he further predict the relationship between scholars and scholars. 

# File Structure

Data-Preprocessing: include all code we use to select the data we want to use from [Aminer](https://www.aminer.cn/citation).

HARP: include codes we use to realize our modified HARP model.

metapath2vec: include codes we use to generate vector depending on the metapath.

Task 1-3: include other codes we use to complete the task.

result : include all kinds of results we achieve.

You could find further information about the code with a README unde the corresponding folder.

# Acknowledgements

Many thanks to the following excellent open source projects:

[HARP](https://github.com/GTmac/HARP)

[metapath2vec](https://ericdongyx.github.io/metapath2vec/m2v.html)
