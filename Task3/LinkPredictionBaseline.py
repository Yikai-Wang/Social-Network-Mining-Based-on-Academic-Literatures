import json
import networkx as nx
import ProcessBar as PB
net_dir = 'all_conf.txt'
all_info = {}
id2num_file = 'id2num.txt'
au2id = {}
id2au = {}
i = 0
#train_out = open("train.txt", 'w')
#est_out = open("test.txt",'w')
fdic = open("au2id.json", 'w')
fnum = open('id2au.json', 'w')
G = nx.Graph()
i = 0
#G2 = nx.Graph()
with open("PageRank_score.json", 'r') as f:
    score = json.load(f)
with open(net_dir) as reader:
    line = reader.readline()
    while line:
        line_dic = eval(line)
        id = line_dic['id']
        year = line_dic['year']
        if year > 2012:
            i += 1
            line = reader.readline()
            continue
        #line = reader.readline()
    #print(i)
        if id in score.keys():
            authors = line_dic['authors']
            for author in authors:
                if author not in au2id.keys():
                    au2id[author] = i
                    id2au[i] = author
                    i += 1
            for p in authors:
                for q in authors:
                    G.add_edge(au2id[p],au2id[q], weight=score[id])
        line = reader.readline()
json.dump(au2id, fdic)
json.dump(id2au, fnum)
fdic.close()
fnum.close()
all_pair = []
#au = [x[0] for x in au2id.items()]
out = open("TopPrediction.txt", 'w')
length = len(au2id.items())
process_bar = PB.ShowProcess(length)
for p in range(length):
    process_bar.show_process()
    for q in range(p+1, length):
        prediction = nx.preferential_attachment(G, [(p,q)])
        for u,v,t in prediction:
            if t > 0:
                out.write("%d\t%d\t%d\n"%(u,v,t))
process_bar.close('done')
out.close()