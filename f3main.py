from f3module import *

egitestek:list[Egitest] = []
file = open(file='egitestek.txt', mode='r', encoding='utf-8')
for s in file: egitestek.append(Egitest(s))

print(f'3.1.: az állományban {len(egitestek)} égites adata van')

c:int = 0
for e in egitestek:
    if e.hol_kering == 'Nap':
        c += 1
print(f'3.2.: {c} égitest kering a nap körül')

