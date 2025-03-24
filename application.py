import sys,math,statistics,re
import pandas as pd
import mi_family
from mi_family import nesting_function
from mi_family import mmi
from mi_family import mi3
from mi_family import mi3_exp
from mi_family import pmi
from mi_family import treshold
f=re.compile('\([A-Z\|\s]+\)')
g=re.compile('[A-Z]+')
last=re.compile('[а-я][а-яё\|\s]+')
file = open('connectors.csv','r')
source=file.readlines()
connectors_dic={}
merged=[]
merged2=[]
merged3=[]
merged4=[]
merged5=[]
for line in source:
    l=line.split(',')   
    connectors_dic[l[0]]=l[1:]
patterns_dic={}
cnt_words=[]
pairs_total=[]
for item in connectors_dic.keys():
    wws=item.split(' ')
    cnt_words=cnt_words+wws
    clean_pattern=[]
    pattern=connectors_dic[item][1]
    for i in re.findall(f,pattern):
        h=list(set(re.findall(g,i)))
        h.sort()
        clean_pattern.append(h)
    patterns_dic[item]=clean_pattern
    for w in wws:
        if 0 <= wws.index(w) < len(clean_pattern):
            p=(w,clean_pattern[wws.index(w)])
            pairs_total.append(p)
final_cnt_words=list(set(cnt_words))
final_cnt_words.sort()
for abc in final_cnt_words:
    abc_patterns=[]
    for t in pairs_total:
        if t[0] == abc:
           abc_patterns.append(str(t[1]))
    abcp=list(set(abc_patterns))
file2 = open('embeddings.txt','r',encoding='UTF-8')
content = file2.readlines()
embeddings_dictionary={}
for line in content:
    s=line.split('[')
    key=s[0][2:-3]
    value=last.findall(s[1])
    embeddings_dictionary[key]=value
result=[]
question=[]
mmi_2=[]
mmi_3=[]
mmi_4=[]
mmi_5=[]
mi3_2=[]
mi3_3=[]
mi3_4=[]
mi3_5=[]
mi3_exp_2=[]
mi3_exp_3=[]
mi3_exp_4=[]
mi3_exp_5=[]
pmi_2=[]
pmi_3=[]
pmi_4=[]
pmi_5=[]
for item in connectors_dic.keys():
    if connectors_dic[item][0]=='2':
        if connectors_dic[item][7]=='единый':
            mmi_2.append(mmi(embeddings_dictionary,connectors_dic,item))
            mi3_2.append(mi3(embeddings_dictionary,connectors_dic,item,374449975))
            mi3_exp_2.append(mi3_exp(embeddings_dictionary,connectors_dic,item,374449975))
            pmi_2.append(pmi(embeddings_dictionary,connectors_dic,item,374449975))
            result.append({'connective': item,'mmi': mmi(embeddings_dictionary,connectors_dic,item), \
                              'mi3': mi3_exp(embeddings_dictionary,connectors_dic,item,374449975), \
                              'pmi': pmi(embeddings_dictionary,connectors_dic,item,374449975)})
        if connectors_dic[item][7]=='вопрос':
            question.append({'connective': item,'mmi': mmi(embeddings_dictionary,connectors_dic,item), \
                              'mi3': mi3_exp(embeddings_dictionary,connectors_dic,item,374449975), \
                              'pmi': pmi(embeddings_dictionary,connectors_dic,item,374449975)})
    if connectors_dic[item][0]=='3':
        if connectors_dic[item][8]=='единый':
            mmi_3.append(mmi(embeddings_dictionary,connectors_dic,item))
            mi3_3.append(mi3(embeddings_dictionary,connectors_dic,item,374449975))
            mi3_exp_3.append(mi3_exp(embeddings_dictionary,connectors_dic,item,374449975))
            pmi_3.append(pmi(embeddings_dictionary,connectors_dic,item,374449975))
            result.append({'connective': item,'mmi': mmi(embeddings_dictionary,connectors_dic,item), \
                              'mi3': mi3_exp(embeddings_dictionary,connectors_dic,item,374449975), \
                              'pmi': pmi(embeddings_dictionary,connectors_dic,item,374449975)})
        if connectors_dic[item][8]=='вопрос':
            question.append({'connective': item,'mmi': mmi(embeddings_dictionary,connectors_dic,item), \
                              'mi3': mi3_exp(embeddings_dictionary,connectors_dic,item,374449975), \
                              'pmi': pmi(embeddings_dictionary,connectors_dic,item,374449975)})
    if connectors_dic[item][0]=='4':
        if connectors_dic[item][9]=='единый':
            mmi_4.append(mmi(embeddings_dictionary,connectors_dic,item))
            mi3_4.append(mi3(embeddings_dictionary,connectors_dic,item,374449975))
            mi3_exp_4.append(mi3_exp(embeddings_dictionary,connectors_dic,item,374449975))
            pmi_4.append(pmi(embeddings_dictionary,connectors_dic,item,374449975))
            result.append({'connective': item,'mmi': mmi(embeddings_dictionary,connectors_dic,item), \
                              'mi3': mi3_exp(embeddings_dictionary,connectors_dic,item,374449975), \
                              'pmi': pmi(embeddings_dictionary,connectors_dic,item,374449975)})
        if connectors_dic[item][9]=='вопрос':
            question.append({'connective': item,'mmi': mmi(embeddings_dictionary,connectors_dic,item), \
                              'mi3': mi3_exp(embeddings_dictionary,connectors_dic,item,374449975), \
                              'pmi': pmi(embeddings_dictionary,connectors_dic,item,374449975)})
    if connectors_dic[item][0]=='5':
        if connectors_dic[item][10]=='единый' or connectors_dic[item][10]=='единый\n':
            mmi_5.append(mmi(embeddings_dictionary,connectors_dic,item))
            mi3_5.append(mi3(embeddings_dictionary,connectors_dic,item,374449975))
            mi3_exp_5.append(mi3_exp(embeddings_dictionary,connectors_dic,item,374449975))
            pmi_5.append(pmi(embeddings_dictionary,connectors_dic,item,374449975))
            result.append({'connective': item,'mmi': mmi(embeddings_dictionary,connectors_dic,item), \
                              'mi3': mi3_exp(embeddings_dictionary,connectors_dic,item,374449975), \
                              'pmi': pmi(embeddings_dictionary,connectors_dic,item,374449975)})
        if connectors_dic[item][10]=='вопрос':
            question.append({'connective': item,'mmi': mmi(embeddings_dictionary,connectors_dic,item), \
                              'mi3': mi3_exp(embeddings_dictionary,connectors_dic,item,374449975), \
                              'pmi': pmi(embeddings_dictionary,connectors_dic,item,374449975)})
print(len(result))           
print(len(question))
treshold_dic={}
treshold_dic['mmi_2']=treshold(mmi_2)
treshold_dic['mmi_3']=treshold(mmi_3)
treshold_dic['mmi_4']=treshold(mmi_4)
treshold_dic['mmi_5']=treshold(mmi_5)
treshold_dic['mi3_2']=treshold(mi3_2)
treshold_dic['mi3_3']=treshold(mi3_3)
treshold_dic['mi3_4']=treshold(mi3_4)
treshold_dic['mi3_5']=treshold(mi3_5)
treshold_dic['mi3_exp_2']=treshold(mi3_exp_2)
treshold_dic['mi3_exp_3']=treshold(mi3_exp_3)
treshold_dic['mi3_exp_4']=treshold(mi3_exp_4)
treshold_dic['mi3_exp_5']=treshold(mi3_exp_5)
treshold_dic['pmi_2']=treshold(pmi_2)
treshold_dic['pmi_3']=treshold(pmi_3)
treshold_dic['pmi_4']=treshold(pmi_4)
treshold_dic['pmi_5']=treshold(pmi_5)
for i in treshold_dic.items():
    print (i)
pd.DataFrame(result).to_csv('result.csv',index=False)
pd.DataFrame(question).to_csv('connectives_in_question.csv',index=False)
sys.exit()    
