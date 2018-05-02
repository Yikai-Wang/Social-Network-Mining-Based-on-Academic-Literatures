import os
import networkx as nx
import re
import pickle

def write_in_pickle(dir, data):
    output = open(dir, 'wb')
    pickle.dump(data, output)
    output.close()

def traverse(root):
    pathDir = os.listdir(root)
    childs = []
    for allDir in pathDir:
        childs.append(os.path.join('%s%s' % (root, allDir)))
    return childs

root_dir ='./clusters_kmeans_wizabstract/'
childs = traverse(root_dir)
for child in childs:
    G = nx.DiGraph()
    scholar_dict = {}
    # 计算文章重要性
    with open(child, 'r') as reader:
        line = reader.readline()
        while line:
            line_dic = eval(line)
            id = line_dic['id']
            references = []
            if 'references' in line_dic.keys():
                references = line_dic['references']
            if references != []:
                for reference in references:
                    G.add_edge(id,reference)
            line = reader.readline()
        #print(G.edge)
        # 介数中心性
        #score = nx.betweenness_centrality(G)
        # PageRank
        score = nx.pagerank(G)
        write_in_pickle('PageRank_score_c%s.pkl'%re.findall('[0-9][0-9]*', child)[0], score)
        score_list = sorted(score.items(), key=lambda item: item[1], reverse=True)
        print("In Cluster %s:"%re.findall('[0-9][0-9]*',child)[0])
        print(score_list[:5])

    # 计算该领域学者的重要性
    with open(child, 'r') as reader:
        line = reader.readline()
        while line:
            line_dic = eval(line)
            id = line_dic['id']
            authors = line_dic['authors']
            for author in authors:
                if id not in score.keys():
                    continue
                if author in scholar_dict.keys():
                    scholar_dict[author] += score[id]
                else:
                    scholar_dict[author] = score[id]
            line = reader.readline()
        scholar_influence = sorted(scholar_dict.items(), key=lambda item: item[1], reverse=True)
        write_in_pickle('PageRank_ScholarInfluence_c%s.pkl'%re.findall('[0-9][0-9]*', child)[0],scholar_dict)
        print("In Cluster %s:" % re.findall('[0-9][0-9]*', child)[0])
        print(scholar_influence[:5])
