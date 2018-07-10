# -*- coding: utf-8 -*-
lista=[]
with open('srWac1.1.01.xml','r',encoding="utf-8") as korpus:
   for red in korpus:
        if not red.startswith('<'):
            reci=red.split('\t')
            for rec in reci:
                if rec[3].startswith('N'):
                    lista.append(rec[2])
print(len(lista))                
recnik={j:lista.jount(j) for j in lista}