import os
import nltk
import math
import string
from collections import Counter
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import re

# 遍历获取文件夹下的文件路径
def traverse(root):
    pathDir = os.listdir(root)
    childs = []
    for allDir in pathDir:
        childs.append(os.path.join('%s%s' % (root, allDir)))
    return childs

# 小写，去标点，分词，去停用词，词性还原  返回单词
def get_words(text, del_type):
    lowers = text.lower()
    #remove the punctuation using the character deletion step of translate
    remove_punctuation_map = dict((ord(char), None) for char in string.punctuation)
    no_punctuation = lowers.translate(remove_punctuation_map)
    words = nltk.word_tokenize(no_punctuation)
    filtered = [w for w in words if w not in stopwords.words('english')]
    word_tags = nltk.pos_tag(filtered)
    final =[]
    lemmatizer = WordNetLemmatizer()
    # 新句子
    for word_tag in word_tags:
        if word_tag[1] in del_type:
            # 去除助词，副词，形容词
            continue
        else:
            # 对于其他单词，还原后，加入到新的句子中
            final.append(lemmatizer.lemmatize(word_tag[0]))
    return final


def tf(word, count):
    return count[word] / sum(count.values())


def n_containing(word, count_list):
    return sum(1 for count in count_list if word in count)


def idf(word, count_list):
    return math.log(len(count_list) / (1 + n_containing(word, count_list)))


def tfidf(word, count, count_list):
    return tf(word, count) * idf(word, count_list)

### 跟目录要改
root_dir ='./clusters_kmeans_wizabstract/'
# https://blog.csdn.net/qq_27231343/article/details/51934490
del_type = ['CD','DT','IN','LS','PRP','RB','RBR','RBS','UH','RP','PRP','MD','EX']
childs = traverse(root_dir)
out = open(root_dir.strip('/.')+'_labels.txt','w')
for child in childs:
    out.write("In cluster %s:\n"%re.findall('[0-9][0-9]*',child)[0])
    with open(child,'r',encoding='utf-8') as reader:
        corpus = ''
        line = reader.readline()
        line_dic = eval(line)
        title = line_dic['title']
        # version1.0 缺失值处理方法：全部舍弃
        abstract = ''
        if 'abstract' in line_dic.keys():
            abstract = line_dic['abstract']
        corpus = corpus+' '+title+' '+abstract
        # preprocessed words
        pre_words = get_words(corpus, del_type)
        count = Counter(pre_words)
        scores = {word: tfidf(word, count, [count]) for word in count}
        sorted_words = sorted(scores.items(), key=lambda x: x[1], reverse=True)
        for word, score in sorted_words[:3]:
            out.write("\tWord: {}, TF-IDF: {}\n".format(word, round(score, 5)))
