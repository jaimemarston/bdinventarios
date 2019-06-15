import operator
from decimal import *
import collections
from operator import itemgetter, attrgetter

import operator

origin_list = [{'codigo': 'BOLS-001', 'saldo.actual': Decimal('98.50')}, {'codigo': 'LLA-001', 'saldo.actual': Decimal('12.00')}, {'codigo': 'LLA-001', 'saldo.actual': Decimal('18.00')}]


#origin_list = [
#    {"name": "foo", "rank": 0, "rofl": 20000},
#    {"name": "Silly", "rank": 15, "rofl": 1000},
#    {"name": "Baa", "rank": 300, "rofl": 20},
#    {"name": "Zoo", "rank": 10, "rofl": 200},
#    {"name": "Penguin", "rank": -1, "rofl": 10000}
#]
nitem=0
delete = [key for key in origin_list if float(key['saldo.actual'])>float(15)]
for foo in origin_list:
    print (nitem,float(foo['saldo.actual']),float(10))
    #if float(foo['saldo.actual'])>float(10):
       
    #   del origin_list[nitem]
    nitem+=1
	#if foo['saldo.actual']
    #   del foo['saldo.actual']
  

print (delete)
#print (origin_list)
#print (float(0.00))

#for foo in sorted(origin_list, key=operator.itemgetter("codigo")):
#    print (foo)


#for foo in sorted(origin_list, key=operator.itemgetter("saldo.actual")):
#    print (foo)

#def custom_sort(t):
#    return t[1]

#L = [("Alice", 25), ("Bob", 20), ("Alex", 5)]
#L.sort(key=custom_sort)


#print(L)

#numbermap = [{'codigo': 'BOLS-001', 'saldo.actual': Decimal('98.50')}, {'codigo': 'LLA-001', 'saldo.actual': Decimal('12.00')}]

#print(type(numbermap))
#numbermap.sort(key=custom_sort)
#numbermap2 = sorted(numbermap, key=operator.itemgetter(1))

#for item in numbermap:
#    print (item)
