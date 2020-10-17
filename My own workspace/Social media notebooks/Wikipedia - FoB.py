#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# !curl "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=%Net%20worth%22AND%Born%22&
# format=jsonfm&srprop=snippet"

import requests

S = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"
cmcontinue=""
i=0
list_persons=[]

def get_names(cmcontinue):
    PARAMS = {
        "action": "query",
        "format": "json",
        "list": "categorymembers",
        "cmtitle":"Category:Living people",
        "cmlimit":500,
        "cmcontinue":cmcontinue
    }

    R = S.get(url=URL, params=PARAMS)
    DATA = R.json()
    print(DATA)
    PAGES = DATA["query"]["categorymembers"]

    global i
    global list_persons
    for page in PAGES:
        i += 1
#         print(page["title"])
        list_persons.append(page["title"])
    print(i)
    
#     if (1)
    if i<limit:
        cmcontinue=DATA["continue"]["cmcontinue"]
        get_names(cmcontinue)

delta=100000
limit=delta
while limit<900000:
    get_names(cmcontinue)
    print(len(list_persons))
    limit=limit+delta


# In[ ]:


#We can actually actively exclude PEPs
# https://en.wikipedia.org/w/api.php?action=query&prop=revisions&rvprop=content&format=xmlfm&titles=Amitabh%20Bachchan&rvsection=0
# officeholder, 

def get_wiki_in_data_structure(DATA):
    rich_guys_data=[]
    subset=DATA['query']['pages'][list(DATA['query']['pages'].keys())[0]]['revisions'][0]['*'].split('\n')
#     print(subset)
    subset_str=str(subset)
    person_info={}
    rich_guy=0
    if ('net_worth' in subset_str) or ('salary' in subset_str):
        for term in subset:
    #         print(term)
            try:
                if (term[0]=='|'):
                    key=term[1:].split('=')[0]
    #                 print(key)
                    value=term[len(key)+2:].strip()
                    key=key.strip()
    #                 print(value)
                    person_info[key]=value                
            except:
                pass
#         print(person_info)
        person_keys=person_info.keys()
        
        if 'net_worth' in person_keys:
            value=person_info['net_worth']
            if value!='' and value!='<!-- Net worth should be supported with a citation from a reliable source -->':
                rich_guy=1
#                 print(person_info['name'])
#                 print(key)
#                 print(value)
        if 'salary' in person_keys:
            value=person_info['salary']
            if value!='':
                rich_guy=1
    if rich_guy:
        return(person_info)
    else:
        return
    
        
# get_wiki_in_data_structure(DATA)


# In[ ]:


import requests
S = requests.Session()

def infobox_check(title):
    URL="http://en.wikipedia.org/w/api.php"
    PARAMS = {
        'action':'query',
        'prop':'revisions',
        'rvprop':'content',
        'format':'json', 
        'titles':title,
        'rvsection':0
    }    
#         "format": "json",
#         "list": "categorymembers",
#         "cmtitle":"Category:Living people",
#         "cmlimit":500,
#         "cmcontinue":cmcontinue
    
    R = S.get(url=URL, params=PARAMS)
    DATA = R.json()
#     print(DATA)
    return(DATA)
#     get_wiki_in_data_structure(DATA)

pehla=0
delta=10000
doosra=pehla+delta
len_all_persons=len(list_persons)
while doosra<len_all_persons:
    
    file=open("HNIs_"+str(pehla)+"_"+str(doosra)+".txt", "w")
    j=0
    print("Pehla is "+str(pehla))
    print("Doosra is "+str(doosra))
    subset_list_persons=list_persons[pehla:doosra]
    for person_item in subset_list_persons:
    #     print(person_item)
        DATA=infobox_check(person_item)
        infobox_details=get_wiki_in_data_structure(DATA)
        if infobox_details is not None:
            print('writing')
            file.write(str(infobox_details)+'\n')

        if j%100==0: # Heartbeat
            print(j)
        j += 1
    
    pehla=doosra+1
    doosra=doosra+delta

    file.close()
# nw_sum=0
# for person in list_persons:
#     networth=''
#     networth=infobox_check(person)['networth']
#     if networth!='':
#         final_list.append({"person":person, "networth":networth])
#         nw_sum += nw_sum
        
# print(len(final_list))
# print(str(len(final_list)*100/len(list_persons))+'% have net worth mentioned')
# print(nw_sum/len(final_list)+' is the average income')


# In[ ]:




