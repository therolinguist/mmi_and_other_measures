import sys,math,statistics
def nesting_function(embeddings_dictionary,connectors_dic,a): # проверка выражения на вложенность и поправка наблюдаемой абсолютной частоты коннектора:
    # если короткое выражение входит в состав более длинного, то надо вычесть из абсолютной частотности первого абсолютную частотность второго
    r=connectors_dic[a]
    f_obs=int(r[3]) # значение наблюдаемой абсолютной частоты коннектора в таблице
    if a in embeddings_dictionary.keys(): # embeddings_dictionary - Словарь, составляемый по заранее подготовленному текстовому файлу
        minus=0
        for smth in embeddings_dictionary[a]:
            ff_obs=int(connectors_dic[smth][3])
            minus=minus+ff_obs
        f_obs=int(r[3])-minus
    else:
        f_obs=int(r[3])
    return f_obs
def mmi(embeddings_dictionary,connectors_dic,a): # embeddings_dictionary - Словарь, составляемый по заранее подготовленному текстовому файлу
    r=connectors_dic[a] # connectors_dic - cловарь, составляемый по таблице данных
    f_obs=nesting_function(embeddings_dictionary,connectors_dic,a)
    if r[0]=='2':
        mmi=math.log(f_obs / ((int(r[4]) * int(r[5]))/int(r[6])**2))
    if r[0]=='3':
        mmi=math.log(f_obs / ((int(r[4]) * int(r[5]) * int(r[6]))/int(r[7])**3))
    if r[0]=='4':
        mmi=math.log(f_obs / ((int(r[4]) * int(r[5]) * int(r[6]) * int(r[7]))/int(r[8])**4))
    if r[0]=='5':
        mmi=math.log(f_obs / ((int(r[4]) * int(r[5]) * int(r[6]) * int(r[7]) * int(r[8]))/int(r[9])**5))
    return round(mmi,5)

#def mi3(embeddings_dictionary,connectors_dic,a,N):# ОШИБКА!!! НЕ БРАТЬ ЭТУ ФУНКЦИЮ ВООБЩЕ!!! формула "MI в кубе", используемая в НКРЯ для ранжирования
#    # результатов при поиске двухсловных коллокаций. Отличается от формулы, предложенной в диссертации
#    # Daille, Béatrice (1994). Approche mixte pour l’extraction automatique de terminologie : statistiques lexicales et filtres linguistiques. Ph.D. thesis, Université Paris 7.
#    # тем, что используется натуральный логарифм, а не логарифм по основанию 2. 
#    r=connectors_dic[a]
#    f_obs=nesting_function(embeddings_dictionary,connectors_dic,a)
#    f=f_obs**3
#    if r[0]=='2':
#        mi3=math.log(f / ((int(r[4]) * int(r[5]))/N))
#    if r[0]=='3':
#        mi3=math.log(f / ((int(r[4]) * int(r[5]) * int(r[6]))/N))
#    if r[0]=='4':
#        mi3=math.log(f / ((int(r[4]) * int(r[5]) * int(r[6]) * int(r[7]))/N))
#    if r[0]=='5':
#        mi3=math.log(f / ((int(r[4]) * int(r[5]) * int(r[6]) * int(r[7]) * int(r[8]))/N))
#    return round(mi3,5)

def mi3_exp(embeddings_dictionary,connectors_dic,a,N): #Вариант формулы "MI в кубе", адаптированной для словосочетаний разной длины
    # по той же логике, что и pmi 
    r=connectors_dic[a]
    f_obs=nesting_function(embeddings_dictionary,connectors_dic,a)
    f=f_obs**3
    if r[0]=='2':
        mi3=math.log(f / ((int(r[4]) * int(r[5]))/N))
    if r[0]=='3':
        mi3=math.log(f / ((int(r[4]) * int(r[5]) * int(r[6]))/N **2))
    if r[0]=='4':
        mi3=math.log(f / ((int(r[4]) * int(r[5]) * int(r[6]) * int(r[7]))/N**3))
    if r[0]=='5':
        mi3=math.log(f / ((int(r[4]) * int(r[5]) * int(r[6]) * int(r[7]) * int(r[8]))/N**4))
    return round(mi3,5)

def mi3_with_pattern(embeddings_dictionary,connectors_dic,a):
    r=connectors_dic[a]
    f_obs=nesting_function(embeddings_dictionary,connectors_dic,a)
    f=f_obs**3
    if r[0]=='2':
        mi3=math.log(f / ((int(r[4]) * int(r[5]))/int(r[6])))
    if r[0]=='3':
        mi3=math.log(f / ((int(r[4]) * int(r[5]) * int(r[6]))/int(r[7])))
    if r[0]=='4':
        mi3=math.log(f / ((int(r[4]) * int(r[5]) * int(r[6]) * int(r[7]))/int(r[8])))
    if r[0]=='5':
        mi3=math.log(f / ((int(r[4]) * int(r[5]) * int(r[6]) * int(r[7]) * int(r[8]))/int(r[9])))
    return round(mi3,5)

def pmi(embeddings_dictionary,connectors_dic,a,N): # формула для двухсловных выражений изначально предложена в работе
    # Church K, Hanks P. Word association norms, mutual information, and lexicography. Computational linguistics. 1990;16(1):22-9.
    # Черч и Хэнкс предпочитают называть ее association ratio.
    # мы используем адаптацию формулы для словосочетаний разной длины, предложенную в работе
    # Ramisch C., Villavicencio A., Boitet C. mwetoolkit: A framework for multiword expression identification // Proceedings of the Seventh International Conference on Language Resources and Evaluation (LREC 2010), Valetta, Malta, 2010. P. 662–669.
    # И вслед за  [Ramisch et al. 2010] называем ее pointwise mutual information,  сокрщенно pmi
    r=connectors_dic[a]
    f_obs=nesting_function(embeddings_dictionary,connectors_dic,a)
    if r[0]=='2':
        pmi=math.log(f_obs / ((int(r[4]) * int(r[5]))/N),2)
    if r[0]=='3':
        pmi=math.log(f_obs / ((int(r[4]) * int(r[5]) * int(r[6]))/N**2),2)
    if r[0]=='4':
        pmi=math.log(f_obs / ((int(r[4]) * int(r[5]) * int(r[6]) * int(r[7]))/N**3),2)
    if r[0]=='5':
        pmi=math.log(f_obs / ((int(r[4]) * int(r[5]) * int(r[6]) * int(r[7]) * int(r[8]))/N**4),2)    
    return round(pmi,5)

def treshold(b):
    tr_len=len(b)
    #print(tr_len)
    tr_mean=round(statistics.mean(b),2)
    #print(round(tr_mean,2))
    tr_median=round(statistics.median(b),2)
    #print(round(tr_median,2))
    tr_stdev=round(statistics.stdev(b),2)
    #print(round(tr_stdev,2))
    tr_min = tr_mean-tr_stdev
    #print(round(tr_min,2))
    tr_max= tr_mean+tr_stdev
    #print(round(tr_max,2))
    return tr_len, tr_mean, tr_median, tr_stdev, tr_min, tr_max     
