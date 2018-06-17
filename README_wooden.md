# File Description

##File Tree

.

├── AcademicPartnership.html

├── AcademicReferenceNetwork.html

├── DrawCoauthorNetwork.py

├── DrawReferenceNetwork.py

├── Ego-nw-html

│   ├── Antonio\ Zamora.html

│   ├── Francisco\ Javier\ �\201lvarez\ �\201lvarez.html

│   ├── Joan-Josep\ Climent.html

│   ├── Jose\ F.\ Vicent.html

│   ├── José\ Luis\ Oliver.html

│   ├── José-Francisco\ Vicent.html

│   ├── Leandro\ Tortosa.html

│   ├── Leticia\ Serrano-Estrada.html

│   ├── Pedro\ R.\ Navarro.html

│   ├── Rafael\ �\201lvarez.html

│   └── Taras\ Agryzkov.html

├── HasVenue.py

├── LDA.ipynb

├── LDA.py

├── LinkPredictionBaseline.py

├── PageRank

│   ├── Author_score.json

│   └── PageRank_score.json

├── ProcessBar.py

├── ReducedPrediction.txt

├── Select-Papers

│   ├── ACL.txt

│   ├── AIED.txt

│   ├── COLING.txt

│   ├── EACL.txt

│   ├── EMNLP.txt

│   ├── ICALT.txt

│   ├── ICDE.txt

│   ├── ICDM.txt

│   ├── ICML.txt

│   ├── ICPP.txt

│   ├── IJCAI.txt

│   ├── IPDPS.txt

│   ├── ITS.txt

│   ├── KDD.txt

│   ├── MASCOTS.txt

│   ├── NIPS.txt

│   ├── OSDI.txt

│   ├── PACT.txt

│   ├── PPOPP.txt

│   ├── SIGMOD.txt

│   └── SOSP.txt

├── TopPrediction.txt

├── all_conf.txt

├── au2id.json

├── calculatePrecision.py

├── ego-network.py

├── getTopAuthor.py

├── id2au.json

├── id2num.txt

├── nrlvector.pkl

├── top8autor.xls

├── word2vec.model

├── wordvec.pkl

└── wordvector.py

3 directories, 59 files

## File Description

AcademicPartnership.html: The co-author relationship graph, different color for different field.

AcademicReferenceNetwork.html:  The citation relationship graph in NLP filed.

DrawCoauthorNetwork.py: Draw the network of co-author relationship.

DrawReferenceNetwork.py: Draw the network of citation network.

Ego-nw-html: Folder, contains several ego-networks. The name of the file is also the name of the author.

HasVenue.py: Select items with 'venue' information.

LDA.py: Use LDA model to get the subjects of the papers.

LinkPredictionBaseline.py: A baseline model for link prediction of co-author network.

PageRank: Folder. 

Author_score.json: A dictionary contains the authors and their influence score.  

PageRank_score.json: A dictionary contains the papers and their influence score.  

ProcessBar.py: Visualize a process bar to get the project progress. 

ReducedPrediction.txt: Top 23237790 edges for link prediction in the baseline model.

Select-Papers: Folder, containing the summits we selected as the resource of papers.

TopPrediction.txt:  Top  34225975 edges for link prediction in the baseline model.

all_conf.txt: A combination of all the papers we selected as the resource for the project.

au2id.json: A dictionary with authors as the key, author IDs as the value.

calculatePrecision.py: Calculate the precision of link prediction in the baseline model.

ego-network.py: Draw ego-network. Run `python ego-network.py [Author Name]` to get the ego-network of the specific author.

getTopAuthor.py: Get the top 8 authors to test whether the model works well.

id2au.json:  A dictionary with author IDs as the key, authors as the value.

id2num.txt: A dictionary with regenreated paper ids (start from 0) as the key,  the real ids of paper as the value.

top8autor.xls: The pagerank score, h-score, r10 score of the top 8 authors. 

word2vec.model: The word2vector model trained on the corpus. The titles and abstracts of papers are trained as documents of the corpus.

wordvec.pkl: The paper id and corresponding vector generated.

wordvector.py: An advanced version of [social_network_domain.ipynb](https://github.com/Wang-Yikai/Social-Network-Mining-Based-on-Academic-Literatures/blob/master/social_network_domain.ipynb)