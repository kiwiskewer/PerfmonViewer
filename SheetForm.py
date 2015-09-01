from collections import defaultdict
from utility import *

class SheetForm:
    REFER,TARGET,DIFF=range(3)
    #parent pfmonMV,batchInfoMV
    #selected pfmonMV,batchInfoMV
    def __init__(self,name,parent,sheet=None):
        self.name=name
        self.orgCountersModel=[None,None,None]
        self.orgBatchesModel=[None,None,None]
        self.orgCounters=[None,None,None]

        self.selCountersModel=[None,None,None]
        self.selBatchesModel=[None,None,None]
        self.selCounters=[[] for i in range(3)]
        self.selBatches=[[] for i in range(3)]
        for i in range(3):
            self.selCountersModel[i] = createModel(parent,0,0,('Perfmons',))
            self.selBatchesModel[i]=createModel(parent,0,1,('BatchId','RenderType'))
        if not sheet:
            return
        for i in range(3):
            self.orgBatchesModel[i]=sheet.orgBatchesModel[i]
            self.orgCountersModel[i]=sheet.orgCountersModel[i]
        

        


