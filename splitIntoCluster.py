import json
import pickle

# 读取文件
def load_pickle(dir):
    pkl_file = open(dir, 'rb')
    tags = pickle.load(pkl_file)
    pkl_file.close()
    return tags
# 直接加载可能会爆
#def load_json(dir):
#    with open(dir, 'r') as f:
#        fullNet = json.load(f)
#    return fullNet

tag_dir = '/Users/wooden/Desktop/tags.pkl'
net_dir = '/Users/wooden/Desktop/dblp-ref-0.json'
# 分类类别个数
ncluster = 10
'''
f1 = open('c1.txt','w',encoding='utf-8')
f2 = open('c2.txt','w',encoding='utf-8')
f3 = open('c3.txt','w',encoding='utf-8')
f4 = open('c4.txt','w',encoding='utf-8')
f5 = open('c5.txt','w',encoding='utf-8')
f6 = open('c6.txt','w',encoding='utf-8')
f7 = open('c7.txt','w',encoding='utf-8')
f8 = open('c8.txt','w',encoding='utf-8')
f9 = open('c9.txt','w',encoding='utf-8')
f10 = open('c10.txt','w',encoding='utf-8')
'''
tag_dic = load_pickle(tag_dir)
i = 0
with open(net_dir) as reader:
    line = reader.readline()
    while line:
        i += 1
        if i%10000 == 0:
            print("processing %d"%i)
        id = eval(line)['id']
        tag = tag_dic[id]
        f = open('./clusters_kmeans/c%d.txt'%tag,'a',encoding='utf-8')
        f.write(line)
        f.close()
        line = reader.readline()
