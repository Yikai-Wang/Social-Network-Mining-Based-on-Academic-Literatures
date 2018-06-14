# 基于学术文献的社交网络挖掘
## 数据集
[DBLP](http://dblp.org/) 是国际上最知名的收录计算机/IT领域学术文献的网址，其收录的数据包括论文的标题、作者列表、发表时间、发表刊物/会议等信息。清华大学的学术搜索网站[ArnetMiner](https://cn.aminer.org/)基于DBLP和ACM等数据源收集了更丰富的文献数据，其中就有[文献的引用数据集](https://cn.aminer.org/citation)，其中包含了几十万篇计算机学术论文的相关数据，为txt格式，需自行解析。
## 项目要求
### 1. 设计聚类算法或社区挖掘算法，对数据集中的所有论文进行聚类，用可视化工具展现出各个领域（即社区，需注明对应的社区研究主题），并凸显各领域中最有影响力的学者
Solution:
1. 对每篇文献进行向量化

   （添加于6.4：对每篇文献的向量化分为两个部分：针对title与abstract，利用word2vec方法进行向量化，针对引用网络结构，合作者网络结构，分别利用同构网络的（node2vec,line,deepwalk）方法和异构网络的（metapath2vec）方法进行向量化，将两者向量化进行拼接作为文献最终的向量。）

2. 利用聚类方法将文献分成不同的领域：

   K-means

   Birch

   各模型聚类结果与正确率：

   | Model                        | 0    | 1    | 2    | 3    | 4    | 5    | accuracy            |
   | ---------------------------- | ---- | ---- | ---- | ---- | ---- | ---- | ------------------- |
   | Birch Deepwalk               | Nl   | Ml   | Ed   | dm   | dp   | os   | 0.5384945472839999  |
   | KMeans  Line                 | dp   | Os   | nl   | Ed   | ml   | dm   | 0.5043577336825439  |
   | Birch Deepwalk word2vec      | Nl   | Os   | dm   | Dp   | Ml   | Ed   | 0.5223953478048564  |
   | Birch Line                   | Ml   | Nl   | dm   | Ed   | Dp   | Os   | 0.38818602861751084 |
   | Birch Line word2vec          | Nl   | Ml   | Ed   | Dp   | Dm   | os   | 0.3677364939849958  |
   | Birch metapath2vec           | Ml   | Nl   | Ed   | Os   | Dm   | Dp   | 0.5968985365709297  |
   | Birch metapath2vec word2vec  | Nl   | Os   | dm   | Ed   | ml   | Dp   | 0.5811544664920614  |
   | KMeans deepwalk              | dp   | Ed   | Ml   | dm   | Os   | Nl   | 0.5308888592947723  |
   | Kmeans deepwalk word2vec     | Nl   | Os   | Dm   | ed   | dp   | Ml   | 0.5225877095633388  |
   | Kmeans line word2vec         | Ml   | Ed   | dm   | Nl   | dp   | Os   | 0.5120670010801852  |
   | Kmeans metapath2vec          | Dm   | Ml   | Ed   | Nl   | Dp   | os   | 0.6638552255811545  |
   | Kmeans metapath2vec word2vec | Dm   | nl   | Ed   | dp   | Os   | Ml   | 0.4987644456282091  |
   | Birch word2vec               | Ml   | Os   | Ed   | dp   | Nl   | Dm   | 0.45135467069146656 |
   | Kmeans word2vec              | os   | Nl   | ml   | ed   | Dp   | dm   | 0.4425208268596203  |
   | Kmeans line mix              | dm   | ed   | Ml   | os   | Nl   | dp   | 0.6704991047779701  |
   | Kmeans deepwalk mix          | Ed   | Nl   | ml   | dm   | Os   | dp   | 0.716621535638715   |
   |                              |      |      |      |      |      |      |                     |
   |                              |      |      |      |      |      |      |                     |
   |                              |      |      |      |      |      |      |                     |
   |                              |      |      |      |      |      |      |                     |
   |                              |      |      |      |      |      |      |                     |
   |                              |      |      |      |      |      |      |                     |
   |                              |      |      |      |      |      |      |                     |

   

3. 打社区标签：根据聚类后的标签结果，将全部的文献按照类别划分，结合每个类的title和abstract信息，用LDA对每一类的文本打标签。

处理后效果（没用到之前的分类信息）：
Topic 0:
based systems paper user information

Topic 1:
performance parallel memory distributed applications

Topic 2:
language based model text using

Topic 3:
learning classification data training feature

Topic 4:
algorithm model time problem algorithms

Topic 5:
data query mining database queries

4. 选出影响力高的学者：

    4.1 根据引用关系计算每篇文献的影响力

    4.2 对每个作者发表过的全部文章的影响力进行加和作为改学者的影响力

对应文件见 render.html

已经选出影响力最高的20个人，并绘制他们和其邻居（coauthor）的网络。**TODO** ：Highlight影响力最高的20个人。

### 2. 对输入的任意一个学者，展现ego-network（参照ArnetMiner网站上的功能示例）

Solution:
1. 对原始数据进行处理，得到如下结构的信息：

    {'Author':{'Coauthor1':#cooperation,'Coauthor2':#cooperation}}

2. 对于给定作者，画出ego-network.

    修改：

    **TODO：**节点大小表示学者影响力，边的长短（粗细）表示学者关系

### 3. 加分项参考

**TODO：**

 利用DBLP和ArnetMiner提供的其它数据，对更多的学者间社会关系进行分析建模和预测，例如预测两个学者间的合作或引用关系，预测一个学者将来会在哪个刊物/会议上发表论文。

学者-期刊：

学者-学者：

（添加于6.4：已经可以做到的是可以对固定年限前的学者利用网络结构进行向量化，如何对时间序列进行预测？）

学者合作AUC：0.7539 0.8338(deepwalk) 0.8373(line) 0.8572(all deepwalk) 0.5686(all line)

学者引用AUC:  0.6692 0.8780 0.7693 0.8530 0.5643

学者会议AUC: 0.7785 0.8776 0.6732 0.8850 0.5481

可以用的：

[Graph Embedding Methods](https://github.com/palash1992/GEM)

## Appendix
可视化工具：
Pajek:http://pajek.imfm.si 

D3: https://d3js.org 

NetworkX: https://networkx.readthedocs.io/en/stable/ 

http://blog.sciencenet.cn/home.php?mod=space&uid=404069&do=blog&classid=141080&view=me&from=space 

Gephi: https://gephi.org/users/ 

http://blog.csdn.net/zdw12242/article/details/8687644 


爬虫Cookie：http://blog.csdn.net/zhyh1435589631/article/details/51307915 


			 http://www.nowamagic.net/academy/detail/1302882 


爬虫防封技巧：http://blog.csdn.net/zhanghaipeng1989/article/details/40828377 

## 参考文献

【1】HARP: Hierarchical Representation Learning for Networks

【2】metapath2vec: Scalable Representation Learning for Heterogeneous Networks

