from collections import defaultdict
from utility import *

class SheetForm:
    REFER,TARGET,DIFF=range(3)
    #parent pfmonMV,batchInfoMV
    #selected pfmonMV,batchInfoMV
    def __init__(self,name,parent,sheet=None):
        self.name=name
        self.orgCounterModels=[None,None,None]
        self.orgBatchModels=[None,None,None]
        self.orgCounters=[None,None,None]

        self.selCountersModel=[None,None,None]
        self.selBatchesModel=[None,None,None]
        self.selCounters=[[] for i in range(3)]
        self.selBatches=[[] for i in range(3)]
        for i in range(3):
            self.selCountersModel[i] = createModel(parent,0,0,('Perfmons',))
            self.selBatchesModel[i]=createModel(parent,0,1,('BatchId','RenderType'))
        if sheet:        
            for i in range(3):
                self.orgBatchModels[i]=sheet.orgBatchModels[i]
                self.orgCounterModels[i]=sheet.orgCounterModels[i]
        
            
        

        


