from PyQt5.QtCore import Qt,QRegExp
from PyQt5.QtWidgets import QAbstractItemView
from utility import *
from SheetForm import SheetForm
from winnt import BTYPE

class BatchWindows:
    def __init__(self,parent):
        self.curSheet=False
        self.group=SheetForm.REFER
            
        self.parent=parent
        self.orgBatchesView=parent.ui.treeView_batches
        initView(self.orgBatchesView)

        self.selBatchesView=parent.ui.treeView_batchSelected
        initView(self.selBatchesView)

        self.batchFilter=parent.ui.lineEdit_batchFilter
        parent.ui.lineEdit_batchFilter.textChanged.connect(self.batchFilterChanged)
        parent.ui.pushButton_selBatches.clicked.connect(self.addSelectedBatches)
    def setSheet(self,sheet):
        self.curSheet=sheet
        self.orgBatchesView.setModel(sheet.orgBatcheModels[self.group])
        self.selBatchesView.setModel(sheet.selBatchesModel[self.group])

    def addSelectedBatches(self):
        index=self.orgBatchesView.selectedIndexes()
        sel_model=self.curSheet.selBatchesModel[self.group]
        org_model=self.curSheet.orgBatcheModels[self.group]
        for idx in index: 
            row=idx.row()          
            b_id=org_model.itemData(org_model.index(row,0))
            b_type=org_model.itemData(org_model.index(row,1))
            sels=self.curSheet.selBatches[self.group]
            if b_id[0] in sels:
                continue
            sel_model.insertRow(0)
            sel_model.setData(sel_model.index(0,0),b_id[0])
            sel_model.setData(sel_model.index(0,1),b_type[0])
            sels.append(b_id[0])

        
    def batchFilterChanged(self):
        syntax = QRegExp.PatternSyntax(QRegExp.Wildcard)
        caseSensitivity = Qt.CaseInsensitive
        regExp = QRegExp(self.batchFilter.text(),caseSensitivity, syntax)
        self.curSheet.orgBatcheModels[self.group].setFilterRegExp(regExp)
        