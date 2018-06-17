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

# 小写，去标点，分词，去停用词  返回单词
def get_words(text):
    lowers = text.lower()
    words = nltk.word_tokenize(lowers)
    return words

### 跟目录要改
root_dir ='./clusters_kmeans_nrl/'
childs = traverse(root_dir)
corpus = []
for child in childs:
    #out.write("In cluster %s:\n"%re.findall('[0-9][0-9]*',child)[0])
    with open(child,'r',encoding='utf-8') as reader:
        # corpus = ''
        line = reader.readline()
        while line:
            line_dic = eval(line)
            title = line_dic['title']+' '
            # version1.0 缺失值处理方法：全部舍弃
            abstract = ''
            if 'abstract' in line_dic.keys():
                abstract = line_dic['abstract']+' '
            corpus.append(title+abstract)
            line = reader.readline()
#pre_words = get_words(corpus, del_type)
#count = Counter(pre_words)

from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
n_features = 1000
tf_vectorizer = CountVectorizer(strip_accents = 'unicode',
                                max_features=n_features,
                                stop_words='english',
                                max_df = 0.5,
                                min_df = 10)
tf = tf_vectorizer.fit_transform(corpus)

from sklearn.decomposition import LatentDirichletAllocation
n_topics = 6
lda = LatentDirichletAllocation(n_topics=n_topics, max_iter=50,
                                learning_method='online',
                                learning_offset=50.,
                                random_state=0)
lda.fit(tf)

def print_top_words(model, feature_names, n_top_words):
    for topic_idx, topic in enumerate(model.components_):
        print("Topic #%d:" % topic_idx)
        print(" ".join([feature_names[i]
                        for i in topic.argsort()[:-n_top_words - 1:-1]]))
    print()

n_top_words = 5
tf_feature_names = tf_vectorizer.get_feature_names()
print_top_words(lda, tf_feature_names, n_top_words)


