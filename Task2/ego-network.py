import os
import sys
import json
import pickle
from pyecharts import Graph
import pyecharts.echarts.events as events
from pyecharts_javascripthon.dom import window, alert
with open("co-author.json", 'r') as f:
    ego_dic = json.load(f)
with open("./PageRank/Author_score.json") as f:
    auscore = json.load(f)

# 读取文件
def load_pickle(dir):
    pkl_file = open(dir, 'rb')
    ego = pickle.load(pkl_file)
    pkl_file.close()
    return ego

def on_click(params):
    window.open(params.name+'.html')
    #window.close()

def formatter(params):
    return params.name

def ego_network(author , ego_dic):
    #ego_dic = load_pickle(dic_dir)
    nodes = [{'name':author, 'symbolSize':auscore[author][0]*10**6}]
    links = []
    #print(ego_dic[author].items())
    for item in ego_dic[author].items():
        if item[0] not in auscore.keys():
            nodes.append({'name': item[0], 'symbolSize': 5})
            links.append({"source": author, "target": item[0], 'value': item[1]})
        else:
            nodes.append({'name': item[0],  'symbolSize': auscore[item[0]][0]*10**6})
            links.append({"source": author, "target": item[0], 'value': item[1]})

    graph = Graph("Ego-network of %s"%author, width= 900, height = 800)
    graph.add("", nodes, links,
              is_label_show=True,label_text_color='g',
              repulsion=8000, is_focusnode=True, is_rotatelabel=True, is_roam=True,
              tooltip_formatter=formatter)
    graph.on(events.MOUSE_CLICK, on_click)
    graph.render(path='./Ego-nw-html/'+author+".html")
    return ego_dic[author]

#ego_network(author = "Hamish Cunningham", ego_dic = ego_dic)
#ego_network(author = "Yorick Wilks", ego_dic = ego_dic)
#ego_network(author = "Kalina Bontcheva", ego_dic = ego_dic)
for arg in sys.argv[1:]:
    print(arg)
    ego_network(arg, ego_dic)
