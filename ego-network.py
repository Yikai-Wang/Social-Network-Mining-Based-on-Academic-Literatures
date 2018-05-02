import pickle
from pyecharts import Graph
# 读取文件
def load_pickle(dir):
    pkl_file = open(dir, 'rb')
    ego = pickle.load(pkl_file)
    pkl_file.close()
    return ego

dic_dir = "coo_author.pkl"
author = "Leandro Tortosa"
ego_dic = load_pickle(dic_dir)

nodes = [{'name':author, 'symbolSize':10}]
links = []
for item in ego_dic[author].items():
    nodes.append({'name': item[0],  'symbolSize': item[1]})
    links.append({"source": author, "target": item[0]})

graph = Graph("Ego-network of %s"%author)
graph.add("", nodes, links,is_label_show=True,label_text_color='k',is_legend_show=True,repulsion=8000,is_focusnode=True,is_rotatelabel=True,is_roam=True)
graph.render()
