from collections import defaultdict
from utility import *
from numpy import array

class ChartSheet:
    REFER,TARGET,DIFF=range(3)
    #parent pfmonMV,batchInfoMV
    #selected pfmonMV,batchInfoMV
    def __init__(self,parent,name):
        self.name=name
        self.modelCounters=createModel(parent,0,0,('Perfmons',))
        self.modelBatches=createModel(parent,0,1,('BatchId','RenderType'))
        self.counters=[]
        self.batches=[]

    def addCounter(self,n):       
        if n in self.counters:
            pass
        self.counters.append(n)
        self.modelCounters.insertRow(0)
        self.modelCounters.setData(self.modelCounters.index(0,0),n)
    def addBatche(self,id,type):               
        if id in self.batches:
            return
        self.batches.append(id)
        self.modelBatches.insertRow(0)
        self.modelBatches.setData(self.modelBatches.index(0,0),id)
        self.modelBatches.setData(self.modelBatches.index(0,1),type)
        

           

     
            


