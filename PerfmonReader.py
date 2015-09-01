import csv
from collections import defaultdict
from collections import OrderedDict

def pfreader(fn):
    pfmon=defaultdict(list)
    with open(fn) as f:
        reader=csv.DictReader(f)
        for row in reader:
            for name,value in row.items():
                pfmon[name].append(int(value))
                #a=list(map(int,list_))
        return pfmon


        

