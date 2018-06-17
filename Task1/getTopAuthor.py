import json
with open('./PageRank/Author_score.json', 'r', encoding='utf-8') as f:
	score = json.load(f)
top = sorted(score.items(), key = lambda p: p[1][0], reverse = True)[:10]
print(top)
