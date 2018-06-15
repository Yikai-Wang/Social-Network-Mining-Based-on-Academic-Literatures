import networkx as nx
import json

net_dir = 'all_conf.txt'
all_info = {}

id2num_file = 'id2num.txt'
num2id = {}
id2num = {}
with open(id2num_file, 'r') as f:
    line = f.readline()
    while line:
        para = line.strip().split(' ')
        num2id[int(para[1])] = para[0]
        id2num[para[0]] = int(para[1])
        line = f.readline()

i = 0
G = nx.DiGraph()
scholar_dict = {}
score = {}
# 计算文章重要性
print("Article")
with open(net_dir, 'r') as reader:
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
    score = nx.pagerank(G)
    out = open('./PageRank/PageRank_score.json', 'w', encoding='utf-8')
    json.dump(score, out)
    out.close()
print("Author")
with open(net_dir) as reader:
    line = reader.readline()
    while line:
        line_dic = eval(line)
        id = line_dic['id']
        authors = line_dic['authors']
        nid = id2num[id]
        if nid <= 12308:
            tag = 'Distributed & Parallel Computing'
        elif nid <= 29508:
            tag = 'Machine Learning'
        elif nid <= 47962:
            tag = 'Data Mining'
        elif nid <= 53586:
            tag = 'Computer Education'
        elif nid <= 65480:
            tag = 'Natural Language Processing'
        else:
            tag = 'Operating Systems / Simulations'
        line = reader.readline()
        for author in authors:
            if id not in score.keys():
                continue
            if author in scholar_dict.keys():
                scholar_dict[author][0] += score[id]
                if tag in scholar_dict[author][1].keys():
                    scholar_dict[author][1][tag] += 1
                else:
                    scholar_dict[author][1][tag] = 1
            else:
                scholar_dict[author] = [score[id], {tag: 1}]
        line = reader.readline()

highrank = sorted(scholar_dict.items(),key=lambda item: item[1][0], reverse=True)[:20]
highrankname = []
for i in highrank:
    highrankname.append(i[0])

# Draw a co-author network
nodes = {}
link = []
cat2num = {'Natural Language Processing': 0, 'Distributed & Parallel Computing': 1,
           'Machine Learning': 2, 'Data Mining': 3, 'Computer Education': 4,
           'Operating Systems / Simulations': 5}
print("Draw")
import numpy as np


def symbolsize(id):
    if id in scholar_dict.keys():
        if scholar_dict[id][0] * (10 ** 5) > 10:
            return int(scholar_dict[id][0] * (10 ** 5))
        else:
            return 10


with open(net_dir) as reader:
    line = reader.readline()
    while line:
        line_dic = eval(line)
        id = line_dic['id']
        authors = line_dic['authors']
        for i in authors:
            if i in highrankname:
                if i not in nodes.keys():
                    print("draw one node")
                    nodes[i] = {'name': i, 'value': scholar_dict[i][0] * (10 ** 5), "symbolSize": symbolsize(i),
                                'category': cat2num[
                                    sorted(scholar_dict[i][1].items(), key=lambda item: item[1], reverse=True)[0][0]]}
                # au_copy = authors
                for j in authors:
                    if j not in nodes.keys() and j in scholar_dict.keys():
                        nodes[j] = {'name': j, 'value': scholar_dict[j][0] * (10 ** 5), "symbolSize": symbolsize(j),
                                    'category': cat2num[
                                        sorted(scholar_dict[j][1].items(), key=lambda item: item[1], reverse=True)[0][
                                            0]]}
                    if j in nodes.keys():
                        link.append({'source': i, 'target': j})
        line = reader.readline()
nodes = [x[1] for x in nodes.items()]

# Draw a co-author network. Part 2
categories = ['Natural Language Processing','Distributed & Parallel Computing',
              'Machine Learning','Data Mining','Computer Education',
              'Operating Systems / Simulations']
def formatter(params):
    return params.name+': '+params.value+';'+params.symbolSize

print("Gnerate the Website")
from pyecharts import Graph
graph = Graph("Academic partnership",width=1200, height=800)
graph.add("", nodes, link, categories ,label_pos="right",
          graph_repulsion=50, is_legend_show=False,
          line_curve=0.2, label_text_color=None,
              tooltip_formatter=formatter)
graph.render("AcademicPartnership.html")