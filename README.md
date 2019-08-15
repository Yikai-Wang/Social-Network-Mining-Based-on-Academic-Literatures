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

## [Yikai Wang](https://github.com/Yikai-Wang)

In brief, he applies several methods in network representation learning and uses and expands a hierarchical representation learning algorithm(HARP) for Networks. For homogeneous networks, he mainly uses deepwalk, node2vec and LINE. For heterogeneous networks, he uses metapath2vec++. For task 1, he uses both homogeneous NRL and heterogeneous NRL methods to extract features for clustering and uses KMeans and Birch to complete the clustering task. For task 3, he uses heterogeneous NRL methods to generate the vector representation of scholar cooperation network, scholar citation network and scholar-conference network.

## [Dan Wu](https://github.com/WuDan0399)

She revises the preprocessing part of word2vec model in task 1. (Stop words deleted, all words are transformed into lower case.) To get the main subjects of the papers, a LDA model is built by her to get the key words of each group of the papers in task 1. After a comparision of different scoring indexes, she uses the PageRank index to calculate the influence of each paper and scholar, then visualize the citation and cooperative relationship in task 1. Another visualization work, the ego-network in task 2, is also implemented and improved by her. To make a contrast of different methods in task 3, she built a baseline model for link prediction.


## [Zheng Wei](https://github.com/WZ-ZXY)

In this project, his work is mainly divided into two part: For task1, he uses the word vector file to train the sentence vector of each paper, and he is responsible for generating small data sets for testing. For task3, he uses the MDP model to train the transition matrix and predicts the relationship between scholars and conferences. Based on this, he further predict the relationship between scholars and scholars. 

# File Structure

Data-Preprocessing: include all code we use to select the data we want to use from [Aminer](https://www.aminer.cn/citation).

HARP: include codes we use to realize our modified HARP model.

metapath2vec: include codes we use to generate vector depending on the metapath.

Task 1-3: include other codes we use to complete the task.

Task 1:

  [DrawCoauthorNetwork.py](https://github.com/Yikai-Wang/Social-Network-Mining-Based-on-Academic-Literatures/blob/master/Task1/DrawCoauthorNetwork.py) Given all the papers and the transformation from the paper id to a number (indicating which field the paper belongs to), calculate the influence of each paper and author, plot the cooperation network among scholars. Size of the nodes represent the influence of the scholar. Color indicates the major field the scholar belongs to.

 [DrawReferenceNetwork.py](https://github.com/Yikai-Wang/Social-Network-Mining-Based-on-Academic-Literatures/blob/master/Task1/DrawReferenceNetwork.py) Given all the papers and the transformation from the paper id to a number (indicating which field the paper belongs to), calculate the influence of each paper, plot the citation network among papers in NLP field. Size of the nodes represent the influence of the paper.

[HasVenue.py](https://github.com/Yikai-Wang/Social-Network-Mining-Based-on-Academic-Literatures/blob/master/Task1/HasVenue.py) Given the original whole dataset, select those whose 'venue' infomation is not empty, then write this item into "\[venue\].txt".

[LDA.ipynb](https://github.com/Yikai-Wang/Social-Network-Mining-Based-on-Academic-Literatures/blob/master/Task1/LDA.ipynb) & 
 [LDA.py](https://github.com/Yikai-Wang/Social-Network-Mining-Based-on-Academic-Literatures/blob/master/Task1/LDA.py)  Get the 6 main subjects of all the papers.

[ProcessBar.py](https://github.com/Yikai-Wang/Social-Network-Mining-Based-on-Academic-Literatures/blob/master/Task1/ProcessBar.py) Visualize a process bar to get the project progress. 

[getTopAuthor.py](https://github.com/Yikai-Wang/Social-Network-Mining-Based-on-Academic-Literatures/blob/master/Task1/getTopAuthor.py) Get the top 8 scholars, for experimental effect evaluation.

[wordvector.py](https://github.com/Yikai-Wang/Social-Network-Mining-Based-on-Academic-Literatures/blob/master/Task1/wordvector.py)An advanced version of [social_network_domain.ipynb](https://github.com/Yikai-Wang/Social-Network-Mining-Based-on-Academic-Literatures/blob/master/Task1/social_network_domain.ipynb)

[Naive_Clustering_Algorithm.py](https://github.com/Yikai-Wang/Social-Network-Mining-Based-on-Academic-Literatures/blob/master/Task1/Naive_Clustering_Algorithm.py): Using KMeans and Birch to cluster. To get the result, run: python Naive_Clustering_Algorithm.py --model line/deepwalk/node2vec/metapath2vec --mixture True/False --KMeans True/False --Birch True/False --classes 6

[result4cluster.py](https://github.com/Yikai-Wang/Social-Network-Mining-Based-on-Academic-Literatures/blob/master/Task1/result4cluster.py): compute the accuracy of cluster model.

Task 2

[ego-network.py](https://github.com/Yikai-Wang/Social-Network-Mining-Based-on-Academic-Literatures/blob/master/Task2/ego-network.py)  Draw ego-network. Open the ternimal, `cd` into the directory of the file, run `python ego-network.py [Author Name]` to get the ego-network of the specific author.

[getco-author.py](https://github.com/Yikai-Wang/Social-Network-Mining-Based-on-Academic-Literatures/blob/master/Task2/getco-author.py) Generate and save a dictionary of which the key is the name of a scholar, the value is a list containing all his coauthers. Source for task2 .


Task 3

[LinkPredictionBaseline.py](https://github.com/Yikai-Wang/Social-Network-Mining-Based-on-Academic-Literatures/blob/master/Task3/LinkPredictionBaseline.py) A baseline model for link prediction of co-author network.

[calculatePrecision.py](https://github.com/Yikai-Wang/Social-Network-Mining-Based-on-Academic-Literatures/blob/master/Task3/calculatePrecision.py)  Calculate the precision of link prediction of the baseline model.

[evaluation4task3.py](https://github.com/Yikai-Wang/Social-Network-Mining-Based-on-Academic-Literatures/blob/master/Task3/evaluation4task3.py): calculate AUC of our model. Run: python evaluation4task3.py --task cp/re/conf/all --AUC True/False --p True/False

[MDP model for task3.ipynb](https://github.com/Yikai-Wang/Social-Network-Mining-Based-on-Academic-Literatures/blob/master/Task3/MDP%20model%20%20for%20task3.ipynb): Build the transfer matrix and do prediction on scholar-reference and scholar-scholar.

result : include all kinds of results we achieve.

You could find further information about the code with a README under the corresponding folder and a complete introduction of our project in [report](https://github.com/Yikai-Wang/Social-Network-Mining-Based-on-Academic-Literatures/blob/master/report.pdf).

# Acknowledgements

Many thanks to the following excellent open source projects:

[HARP](https://github.com/GTmac/HARP)

[metapath2vec](https://ericdongyx.github.io/metapath2vec/m2v.html)
