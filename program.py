# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 18:48:54 2018

@author: admin
"""
korpus=open('korpus.xml','r',encoding='utf-8')
frekvenca=open('frekvenca.txt','w',encoding='utf-8')
frekvenca_imenica=open('frekvenca imenica.txt','w',encoding='utf-8')
lista=[]
lista_imenica=[]
for red in korpus:
    if '<' not in red:
        podaci=red.split('\t')
        if podaci[3].startswith('Z')==False:
            lista.append(podaci[2])
            if podaci[3].startswith('N'):
                lista_imenica.append(podaci[2])
        
recnik={j:lista.count(j) for j in lista}
for k,v in recnik.items():
    frekvenca.write(k+'\t'+'\t'+'\t'+str(v)+'\n')
frekvenca.close()
recnik_imenica={j:lista_imenica.count(j) for j in lista_imenica}
for k,v in recnik_imenica.items():
    frekvenca_imenica.write(k+'\t'+'\t'+'\t'+str(v)+'\n')
