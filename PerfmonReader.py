import csv
from collections import defaultdict
from collections import OrderedDict
from numpy import array

def pfreader(fn):
    pfmon=defaultdict(array)
    tmp_counters=defaultdict(list)
    with open(fn) as f:
        reader=csv.DictReader(f)
        for row in reader:
            data=[]
            for name,value in row.items():
                tmp_counters[name].append(int(value))
            
        for k in tmp_counters:
            pfmon[k]=array(tmp_counters[k])
        return pfmon


        

