# -*- coding: utf-8 -*-
"""
PETNIČKI PYTHON IZAZOV
LVL1 - Petnički pastir:
* Izbrojte ukupan broj reči u pesmi Devojka iz Petnice.
* Izbrojte broj različitih reči u pesmi.
LVL2 - Vešti Vebster:
* Napravite rečnik svih reči iz pesme uz podatak o učestalosti njihovog javljanja.
* Ispišite lepo formatiran rečnik i frekvence reči.
  REČ     FREKVENCA
  reč1    frekvenca1
  reč2    fekvenca2
  ..
* BONUS: Neka ispisani rečnik bude poređan po abecedi.
  HINT: http://python-reference.readthedocs.io/en/latest/docs/functions/sorted.html
LVL3 - Veliki Hudini:
* Načinite potrebne promene kako biste stvorili pesmu Dečak iz Petnice i ispišite tu pesmu.
  HINT: http://python-reference.readthedocs.io/en/latest/docs/str/endswith.html
Imate pravo za jedan dodatan hint na svakih 10 minuta tokom naredna 2 sata. Pošaljite pitanje u Viber grupi.
"""

devojka_iz_petnice = "Da je ljubav nauka\ndobio bih Nobela\nA da je ljubav knjiga\nuzeo bih NIN-a\n\nDevojke iz Petnice\nredom su pametnice\nA jedna među njima\nsad moje srce ima\n\nŽelim da sam projekat\ni da sam joj u mislima\nmrtvi Vizantinac\niz srednjeg veka pisac\nželim da sam bitan\nu njenim poslovima\n\nDevojka iz Petnice\nona meni znači sve\ni kada me se seti\nja hoću da poletim\n\nDevojka iz Petnice\nu koju sam zaljubljen\nsad uči tamo negde\nDa li pamti mene?\n\nHoću da sam tema\nU nečemu što sprema\nMrtvi Vizantinac\niz srednjeg veka pisac\nželim da sam bitan\nu njenim poslovima"
r=devojka_iz_petnice.lower()
x=r.split('\n')
y=[] 
for i in x:
    h=i.split(' ')
    for g in h:
        if g!='':
            y.append(g)
print (len(y))
unikati=[]
for i in y:
    if i not in unikati:
        unikati.append(i)
print (len(unikati))
yy=sorted(y)
recnik={j:yy.count(j) for j in yy}
print("RECI","FREKVENCA") #ne znam kako da formatiram lepo
for k, v in recnik.items():
    print(k,v)
  
for i in range(len(y)):
    if y[i].endswith('o'):
        y[i]=y[i][:-1]+'la'
    if y[i]=='devojke':
        y[i]='momci'
    if y[i].endswith('an'):
        y[i]=y[i][:-2]+'na'
    if y[i]== 'jedna':
        y[i]='jedan'
    if y[i]=='joj':
        y[i]='mu'
    if y[i]=='mrtvi':
        y[i]='mrtva'
    if y[i]=='vizantinac':
        y[i]='vizantinka'
    if y[i]=='njenim':
        y[i]='njegovim'
    if y[i]=='devojka':
        y[i]='momak'
    if y[i]=='ona':
        y[i]='on'
    if y[i]=='koju':
        y[i]='kog'
    if y[i].endswith('en'):
        y[i]=y[i][:-2]+'ena'
print (y)
        
    
