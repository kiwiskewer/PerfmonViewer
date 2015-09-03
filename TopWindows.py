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
from sympy.polys.groebnertools import groebner
from astropy.io.fits.hdu.groups import Group

class TopWindows:
    def __init__(self,parent):
        self.parent=parent
        view_name=('sheet',)
        self.sheetsViewModel=createModelOnView(parent,parent.ui.treeView_spreadSheets,0,0,view_name)
        self.curSheet=False
        self.sheets=defaultdict(SheetForm)
        self.sheetsView=parent.ui.treeView_spreadSheets
        self.sheetNameInput=parent.ui.lineEdit_sheetName
        
        self.pfCounterModels=[None,None,None]
        self.pfBatchModels=[None,None,None]
        
        parent.ui.pushButton_addSheet.clicked.connect(self.addSheet)
        parent.ui.pushButton_delSheet.clicked.connect(self.deleteSheet)
        parent.ui.pushButton_showSheet.clicked.connect(self.showSheet)
        parent.ui.treeView_spreadSheets.selectionModel().selectionChanged.connect(self.updatePerfBatchFromSheet)


        self.pfCounters=[defaultdict(list) for i in range(3)]
        i=0
        for name in ('Refer','Target','Diff'):
            self.pfCounterModels[i]=createModel(self.parent,0,0,(name,))
            headers=[]
            for h in ('BatchID',"RenderType"):
                headers.append(name+":"+h)
            self.pfBatchModels[i]=createModel(self.parent,0,1,headers)
            i+=1

        



    def reloadData(self,group):
        pfmon=self.pfCounters[group]
        model=self.pfCounterModels[group]
        if not pfmon:
            return
        
        model.clear()
        for pname in pfmon.keys():
            # self.refDataModel.appendRow(QStandardItem(k)) 
            model.insertRow(0) 
            model.setData(model.index(0, 0), pname)                
        
        model = self.pfBatchModels[group]    
        for b in range(len(pfmon['batch_id'])):
            model.insertRow(0)
            d=pfmon['batch_id'][b]
            model.setData(model.index(0,0),d)
            d=pfmon['batch_type'][b]
            model.setData(model.index(0,1),d)                
            

    def loadDataFromFile(self,ref_fn,group):
        if ref_fn:
            self.pfCounters[group] = pfreader(ref_fn)


    def addSheet(self,name=None):
        if not name:
            name=self.sheetNameInput.text()
        if not name:
            return
        if name not in self.sheets.keys():
            sheet=SheetForm(name,self.parent)
        else:
            sheet=self.sheets[name]
        sheet.orgCounters=self.pfCounters
        sheet.orgCounterModels=self.pfCounterModels
        sheet.orgBatcheModels=self.pfBatchModels

        self.sheets[sheet.name]=sheet
        self.sheetsViewModel.insertRow(0)
        self.sheetsViewModel.setData(self.sheetsViewModel.index(0,0),sheet.name)
        return sheet

    def deleteSheet(self):

        index=self.sheetsView.selectedIndexes()
        if not index:
            return
        item=self.sheetsViewModel.itemData(index[0])
        n=item[0]
        if n not in self.sheets:
            return
        sheet=self.sheets[n]
        self.sheets.pop(sheet.name,None)
        self.sheetsViewModel.removeRow(index[0].row())

    def updatePerfBatchFromSheet(self):
        index=self.sheetsView.selectedIndexes()
        if not index:
            return
        n=(self.sheetsViewModel.itemData(index[0]))[0]
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

