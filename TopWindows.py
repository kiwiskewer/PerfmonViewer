from PyQt5.QtCore import QRegExp, QSortFilterProxyModel,Qt
from PyQt5.QtGui import QStandardItemModel
from PyQt5.QtWidgets import QAbstractItemView
from PyQt5.QtGui import QStandardItem

from collections import defaultdict

from PerfmonReader import pfreader
from SheetForm import SheetForm
from BatchWindows import BatchWindows
from PerfmonWindows import PerfmonWindows
from utility import *
from BatchPfmonTable import BatchPfmonTable

class TopWindows:
    def __init__(self,parent):
        self.parent=parent
        view_name=('sheet',)
        self.sheetProxyModel=createModelOnView(parent,parent.ui.treeView_spreadSheets,0,0,view_name)
        self.curSheet=False
        self.sheets=defaultdict(SheetForm)
        self.sheetsView=parent.ui.treeView_spreadSheets
        self.sheetNameInput=parent.ui.lineEdit_sheetName
        
        parent.ui.pushButton_addSheet.clicked.connect(self.addSheet)
        parent.ui.pushButton_delSheet.clicked.connect(self.deleteSheet)
        parent.ui.pushButton_showSheet.clicked.connect(self.showSheet)
        parent.ui.treeView_spreadSheets.selectionModel().selectionChanged.connect(self.updatePerfBatchFromSheet)

        #ONLY FOR TEST
        debug_data=defaultdict(list)
#        debug_data['batch_id']=[0,1,2,3]
#        debug_data['batch_type']=[10,20,30,40]
#        debug_data['value']=[10,20,30,40]
        self.refData=debug_data
        self.targetData=debug_data
        self.diffData=debug_data
        



        

    def loadDataFromFile(self,ref_fn,group):
        if ref_fn:
            self.refData = pfreader(ref_fn)
            names=('Refernece',)
            self.refDataModel=createModel(self.parent,0,0,names)    
                              
            for k in self.refData.keys():
                #self.refDataModel.appendRow(QStandardItem(k)) 
                self.refDataModel.insertRow(0) 
                self.refDataModel.setData(self.refDataModel.index(0,0),k) 

            names=('BatchID',"RenderType",)
            bmodel=createModel(self.parent,0,1,names)
            for b in range(len(self.refData['batch_id'])):
                bmodel.insertRow(0)
                d=self.refData['batch_id'][b]
                bmodel.setData(bmodel.index(0,0),d)
                d=self.refData['batch_type'][b]
                bmodel.setData(bmodel.index(0,1),d)
            self.refBatchesModel=bmodel
#         if target_fn:
#             self.targetData=pfreader(target_fn)
#             names=('Target',)
#             self.targetDataModel=createModel(self.parent,0,0,names)     
#         if self.refData and self.targetData:
#             self.diffData=dict.fromkeys([x for x in self.targetData if x in self.refData])
#             names=('Diff',)
#             self.diffDataModel=createModel(self.parent,0,0,names)
    def addSheet(self,name=None):
        if not name:
            name=self.sheetNameInput.text()
        if not name:
            return
        sheet=SheetForm(name,self.parent)
        sheet.orgCounters[SheetForm.REFER]=self.refData
        sheet.orgCounters[SheetForm.TARGET]=self.targetData
        sheet.orgCounters[SheetForm.DIFF]=self.diffData
        if self.refData:
            sheet.orgCountersModel[SheetForm.REFER]=self.refDataModel
            sheet.orgBatchesModel[SheetForm.REFER]=self.refBatchesModel


        self.sheets[sheet.name]=sheet
        self.sheetProxyModel.insertRow(0)
        self.sheetProxyModel.setData(self.sheetProxyModel.index(0,0),sheet.name)
        return sheet

    def deleteSheet(self):

        index=self.sheetsView.selectedIndexes()
        if not index:
            return
        item=self.sheetProxyModel.itemData(index[0])
        n=item[0]
        if n not in self.sheets:
            return
        sheet=self.sheets[n]
        self.sheets.pop(sheet.name,None)
        self.sheetProxyModel.removeRow(index[0].row())

    def updatePerfBatchFromSheet(self):
        index=self.sheetsView.selectedIndexes()
        if not index:
            return
        n=(self.sheetProxyModel.itemData(index[0]))[0]
        self.curSheet=self.sheets[n]
        self.parent.sheetSelected(self.curSheet)
    def selectSheet(self,sheet):
        self.curSheet=sheet
        self.parent.sheetSelected(self.curSheet)
    def showSheet(self):
        sheet=self.curSheet
        #FIXME: only update the table view if it's already created
        if not self.parent.curTable:
            self.parent.curTable=BatchPfmonTable(sheet)
            self.parent.curTable.show()
        else:
            self.parent.curTable.updateTable(sheet)

