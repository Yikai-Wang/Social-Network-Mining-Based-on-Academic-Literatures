import numpy as np

# def load_txt(filename):
#     txt = {}
#     with open(filename,'r') as f:
#         while True:
#             tmp = f.readline()
#             if not tmp:
#                 break
#             tmp = tmp.split(' ')
#             try:
#                 k = int(tmp[0][1:])
#                 v = []
#                 for i in range(1,len(tmp)-1):
#                     v.append(np.float(tmp[i]))
#                 txt[k] = v
#             except:
#                 pass
#     return txt
def load_txt(filename):
    txt = {'conf':{},'author':{}}
    with open(filename,'r') as f:
        while True:
            tmp = f.readline()
            if not tmp:
                break
            tmp = tmp.split(' ')
            if tmp[0][0]=='a':
                k = tmp[0][1:]
                v = []
                for i in range(1,len(tmp)-1):
                    v.append(np.float(tmp[i]))
                txt['author'][k] = v
            if tmp[0][0]=='v':
                k = tmp[0][1:]
                v = []
                for i in range(1,len(tmp)-1):
                    v.append(np.float(tmp[i]))
                txt['conf'][k] = v
    return txt
txt = load_txt('task3cp.vector.txt')
# result = np.array([])
# for k,v in txt.items():
#     np.append(result,np.array([k,v]))
f = open('task3cp.txt','w')  
f.write(str(txt))  
f.close()  