import json

net_dir = 'all_conf.txt'
coau = {}
with open(net_dir) as reader:
    line = reader.readline()
    while line:
        line_dic = eval(line)
        authors = line_dic['authors']
        for i in authors:
            for j in authors:
                if i == j :
                    continue
                else:
                    if i not in coau.keys():
                        coau[i] = {j:1}
                    elif j not in coau[i].keys():
                        coau[i][j] = 1
                    else:
                        coau[i][j] += 1
        line = reader.readline()
with open("co-author.json", 'w') as f:
    json.dump(coau,f)
