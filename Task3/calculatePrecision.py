import json
import ProcessBar as PB
net_dir = 'all_conf.txt'
all_info = {}
id2num_file = 'id2num.txt'
au2id = {}
id2au = {}
i = 0
with open("./PageRank/PageRank_score.json", 'r') as f:
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
        if id in score.keys():
            authors = line_dic['authors']
            for author in authors:
                if author not in au2id.keys():
                    au2id[author] = i
                    id2au[i] = author
                    i += 1
        line = reader.readline()
print("Part One Finished.")
prediction = []

with open("ReducedPrediction4500.txt", 'r') as reader:
    line = reader.readline()
    while line:
        prediction.append(line.strip().split('\t'))
        line = reader.readline()
    top_score =[(x[0], x[1]) for x in sorted(prediction, key=lambda t: t[2], reverse=True)]
hit = 0
print("Part Two Finished.")
process_bar = PB.ShowProcess(16642)
with open(net_dir) as reader:
    line = reader.readline()
    while line:
        line_dic = eval(line)
        id = line_dic['id']
        year = line_dic['year']
        if year > 2012:
            process_bar.show_process()
            authors = line_dic['authors']
            for author1 in authors:
                if author1 not in au2id.keys():
                    continue
                for author2 in authors:
                    if author2 not in au2id.keys():
                        continue
                    if (au2id[author1], au2id[author2]) in top_score or (au2id[author2], au2id[author1]) in top_score:
                        hit += 1
        line = reader.readline()
process_bar.close('done')
print("Part Three Finished.")

print(hit)
print(hit/16642)