# Social-Network-Mining-Based-on-Academic-Literatures 基于学术文献的社交网络挖掘
## 数据集
[DBLP](http://dblp.org/) 是国际上最知名的收录计算机/IT领域学术文献的网址，其收录的数据包括论文的标题、作者列表、发表时间、发表刊物/会议等信息。清华大学的学术搜索网站[ArnetMiner](https://cn.aminer.org/)基于DBLP和ACM等数据源收集了更丰富的文献数据，其中就有[文献的引用数据集](https://cn.aminer.org/citation)，其中包含了几十万篇计算机学术论文的相关数据，为txt格式，需自行解析。
## 项目要求
### 设计聚类算法或社区挖掘算法，对数据集中的所有论文进行聚类，用可视化工具展现出各个领域（即社区，需注明对应的社区研究主题），并凸显各领域中最有影响力的学者。
Solution:
	1. 根据title和abstract信息，对每篇文献进行向量化
	2. 聚类
	3. 打社区标签：根据聚类后的标签结果，将全部的文献按照类别划分，结合每个类的title和abstract信息，用tf-idf(finished)/LDA(on processing)对每一类的文本打标签。
	4. 选出影响力高的学者：
    4.1 根据引用关系计算每篇文献的影响力
    4.2 对每个作者发表过的全部文章的影响力进行加和作为改学者的影响力

### 能对输入的任意一个学者，展现其自我中心网络（ego-network）的功能（参照ArnetMiner网站上的功能示例）。

Solution:
	1. 对原始数据进行处理，得到如下结构的信息：
    {'Author':{'Coauthor1':#cooperation,'Coauthor2':#cooperation}}
	2. 对于给定作者，画出ego-network.

### 加分项参考：利用DBLP和ArnetMiner提供的其它数据，对更多的学者间社会关系进行分析建模和预测，例如预测两个学者间的合作或引用关系，预测一个学者将来会在哪个刊物/会议上发表论文。

Solution:
	1.

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
