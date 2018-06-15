import os
import sys
import pickle
from pyecharts import Graph
import pyecharts.echarts.events as events
from pyecharts_javascripthon.dom import window, alert


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

def ego_network(author = "Leandro Tortosa", ego_dic='{}'):
    #ego_dic = load_pickle(dic_dir)
    nodes = [{'name':author, 'symbolSize':10}]
    links = []
    #print(ego_dic[author].items())
    for item in ego_dic[author].items():
        nodes.append({'name': item[0],  'symbolSize': item[1]})
        links.append({"source": author, "target": item[0]})

    graph = Graph("Ego-network of %s"%author)
    graph.add("", nodes, links,
              is_label_show=True,label_text_color='g',
              repulsion=8000, is_focusnode=True, is_rotatelabel=True, is_roam=True,
              tooltip_formatter=formatter)
    graph.on(events.MOUSE_CLICK, on_click)
    graph.render(path='./Ego-nw-html/'+author+".html")
    return ego_dic[author]

dic_dir = "coo_author.pkl"
ego_dic = load_pickle(dic_dir)
#for it in ego_dic.items():
#    ego_network(it[0], ego_dic)
#    print("Generating %s"%it[0])
#print(sys.argv[1])
#ego_network(sys.argv[1],ego_dic)
q = []
eg = ego_dic["Leandro Tortosa"].items()
ego_network("Leandro Tortosa", ego_dic)
for i in eg:
    print(i[0])
    q.append(i[0])
for p in q:
    #print(p)
    ego_network(p, ego_dic)
'''
P = q
q = []
for i in P:
    el = ego_dic[i].items()
    for e in el:
        print(e[0])
        q.append(e[0])
for p in q:
    print(p)
    ego_network(p, ego_dic)
'''
