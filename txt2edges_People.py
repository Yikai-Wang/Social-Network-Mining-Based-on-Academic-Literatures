dp_conf = ['PPOPP', 'PACT', 'IPDPS', 'ICPP']
ml_conf = ['IJCAI', 'ICML', 'NIPS']
dm_conf = ['ICDE', 'SIGMOD','KDD' , 'ICDM']
ed_conf = ['AIED', 'ITS', 'ICALT']
nl_conf = ['ACL','EACL' , 'COLING', 'EMNLP']
os_conf = ['MASCOTS', 'SOSP', 'OSDI']

import numpy as np
import pickle
import json

def load_pickle():
   pkl_file = open('cluster_Birch_nrl.pkl', 'rb')
   data1 = pickle.load(pkl_file)
   pkl_file.close()
   return data1

def load_json(dir):
   data = []
   with open(dir, 'r') as f:
       while True:
           a = f.readline()
           if not a:
               break
           b = json.loads(a)
           data.append(b)
   return data

# tmp = []
# for m in os_conf:
#     tmp += load_json(m+'.txt')
# for i in range(len(tmp)):
#     true_label[id2num[tmp[i]['id']]]='os'
    
# predict={}
# for i in range(6):
#     predict[i]=dict()
#     predict[i]['dp']=0
#     predict[i]['ml']=0
#     predict[i]['dm']=0
#     predict[i]['ed']=0
#     predict[i]['nl']=0
#     predict[i]['os']=0
# for k,v in result.items():
#     predict[v][true_label[k]] += 1
    
# num2str = dict()
# num2str[0]='ml'
# num2str[1]='os'
# num2str[2]='dp'
# num2str[3]='nl'
# num2str[4]='ed'
# num2str[5]='dm'
# prop = {}
# prop['dp']=[0,0]
# prop['ml']=[0,0]
# prop['dm']=[0,0]
# prop['ed']=[0,0]
# prop['nl']=[0,0]
# prop['os']=[0,0]
# for k,v in true_label.items():
#     prop[v][1] += 1
#     if num2str[result[k]]==v:
#         prop[v][0] += 1
# num0 = 0
# num1 = 0
# for k,v in prop.items():
#     num0 += v[0]
#     num1 += v[1]

# for i in range(67581):
    

papers = []
meetings = dp_conf+ml_conf+dm_conf+ed_conf+nl_conf+os_conf
for met in meetings:
    papers += load_json(str(met)+'.txt')

edges = []
name2num = dict()
num = 0
for j in range(len(papers)):
    tmp = papers[j]['authors']
    for i in range(len(tmp)):
        if tmp[i] not in name2num.keys():
          name2num[tmp[i]] = num
          num += 1
    if len(tmp) == 1:
        edges.append([name2num[tmp[0]],name2num[tmp[0]]])
    else:
        for l in range(len(tmp)-1):
            for k in range(l+1,len(tmp)):
                edges.append([name2num[tmp[l]],name2num[tmp[k]]])
                edges.append([name2num[tmp[k]],name2num[tmp[l]]])
#for i in range(len(papers)):
#    if 'references' in papers[i].keys() and papers[i]['references']:
#        tmp = len(papers[i]['references'])
#        for nn in papers[i]['references']:
#            if id2num.get(nn,-1)!=-1:
#                edges.append([id2num[papers[i]['id']], id2num[nn]])
#            elif [id2num[papers[i]['id']], id2num[papers[i]['id']]] not in edges[-tmp-1:]:
#                edges.append([id2num[papers[i]['id']], id2num[papers[i]['id']]])
#    else:
#        edges.append([id2num[papers[i]['id']], id2num[papers[i]['id']]])
with open('edges_people_cooperation.txt','w') as f:
   for i in range(len(edges)):
       f.write(str(edges[i][0])+" "+str(edges[i][1])+"\n")
with open('name2num.txt','w') as f:
   for k,v in name2num.items():
       f.write(str(k)+' '+str(v)+'\n')
#data = np.load('wyk.npy')
   
