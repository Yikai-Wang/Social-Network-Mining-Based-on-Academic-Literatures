import json
import string
import numpy as np
import gensim
import nltk
from nltk.corpus import stopwords
punc = string.punctuation
result_dic = {}

import pickle

id2num_file = 'id2num.txt'
num2id = {}
id2num = {}

with open(id2num_file, 'r') as f:
    line = f.readline()
    while line:
        para = line.strip().split(' ')
        num2id[int(para[1])] = para[0]
        id2num[para[0]] = int(para[1])
        line = f.readline()

def write_in_pickle(data, path):
    output = open(path, 'wb')
    pickle.dump(data, output)
    output.close()

def load_pickle(path):
    pkl_file = open(path, 'rb')
    data = pickle.load(pkl_file)
    pkl_file.close()
    return data

# 分词，去停用词
def sent2word(sentence):
    """
    Segment a sentence to words
    Delete stopwords
    """
    segList = nltk.word_tokenize(sentence)
    filtered = [w for w in segList if w not in stopwords.words('english') and w not in punc]
    return filtered


def getWordVecs(wordList, model):
    vecs = []
    for word in wordList:
        word = word.replace('\n', '')
        try:
            vecs.append(model[word])
        except KeyError:
            continue
    # vecs = np.concatenate(vecs)
    return np.array(vecs, dtype='float')


def buildVecs(sentences,name):
    posInput = []
    parsered = []
    for line in sentences:
        parsered.append(sent2word(line))
    print("build word2vec model.")
    #model = KeyedVectors.load_word2vec_format('/tmp/vectors.bin', binary=False)
    model = gensim.models.Word2Vec(parsered, size=100, window=5, min_count=5, workers=4)
    model.save(name)
    for line in parsered:
        resultList = getWordVecs(line, model)
        # for each sentence, the mean vector of all its vectors is used to represent this sentence
        if len(resultList) != 0:
            resultArray = sum(np.array(resultList))/len(resultList)
            posInput.append(resultArray)
    return np.array(posInput)


def loadVecs(sentences,name):
    print("分词...")
    print("len(sentences):%d"%len(sentences))
    posInput = []
    parsered = []
    for line in sentences:
        parsered.append(sent2word(line))
    print("load word2vec model.")
    model = gensim.models.Word2Vec.load(name)
    print(len(parsered))
    for line in parsered:
        resultList = getWordVecs(line, model)
        # for each sentence, the mean vector of all its vectors is used to represent this sentence
        if len(resultList) != 0:
            resultArray = sum(np.array(resultList)) / len(resultList)
            posInput.append(resultArray)
        else:
            posInput.append(np.zeros(100))
    return np.array(posInput)

#pre = load_pickle('wordvec.pkl')-
with open('all_conf.txt', 'r') as f:
    line = f.readline()
    texts = []
    ids = []
    i = 0
    while line:
        if i > 67576:
            print(i)
        i += 1
        line = json.loads(line)
        text = ''
        ids.append(id2num[line['id']])
        if 'abstract' in line:
            text += line['abstract']+' '
        text += line['title']
        texts.append(text)
        line = f.readline()
    print("Number of texts:%d"%len(texts))
    vecs = loadVecs(texts,'word2vec.model')
    print("Number of vecs:%d"%len(vecs))
    print("Number of ids:%d"%len(ids))
    for id, vec in zip(ids, vecs):
        result_dic[id] = vec
write_in_pickle(result_dic, 'wordvec.pkl')