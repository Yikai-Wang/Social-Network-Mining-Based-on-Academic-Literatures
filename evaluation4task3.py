import random
import numpy as np

def AUC(exist_edges,missing_edges,nodes_number,times,node_vector):
	nonexist_edges = []
	tmp = exist_edges + missing_edges
	for i in range(nodes_number-1):
		for j in range(i+1, nodes_number):
			if [i j] not in tmp:
				nonexist_edges.append([i,j])
	n1 = 0
	n2 = 0
	for _ in range(times):
		missing_edge = random.sample(missing_edges)
		nonexist_edge = random.sample(nonexist_edges)
		score_miss = np.dot(node_vector[missing_edge[0]],node_vector[missing_edge[1]])
		score_none = np.dot(node_vector[nonexist_edge[0]],node_vector[nonexist_edge[1]])
		if score_miss > score_none:
			n1 += 1
		elif score_miss == score_none:
			n2 += 1
	return (n1+0.5*n2)/times

def Precision(exist_edges,missing_edges,nodes_number,L,node_vector):
	non_observed_edges = []
	for i in range(nodes_number-1):
		for j in range(i+1,nodes_number):
			if [i,j] not in exist_edges:
				score = np.dot(node_vector[i],node_vector[j])
				non_observed_edges.append([[i,j],score])
	non_observed_edges.sort(key= lambda x: -x[1])
	Lr = 0
	for i in range(L):
		if non_observed_edges[i][0] in missing_edges:
			Lr += 1
	return Lr/L

