from PyQt5.QtCore import Qt,QRegExp
from PyQt5.QtWidgets import QAbstractItemView
from utility import *
from SheetForm import SheetForm
class PerfmonWindows:
    def __init__(self,parent):
        self.curSheet=False
        self.group=SheetForm.REFER
        
        self.parent=parent
        self.orgPfmonView=parent.ui.treeView_pfmons
        initView(self.orgPfmonView)
        self.orgPfmonView.setSelectionMode(QAbstractItemView.MultiSelection)

        self.selPfmonView=parent.ui.treeView_pfmonSelected
        initView(self.selPfmonView)
        self.selPfmonView.setSelectionMode(QAbstractItemView.MultiSelection)

        self.pfmonFilter=parent.ui.lineEdit_pfmonFilter
        parent.ui.lineEdit_pfmonFilter.textChanged.connect(self.pfmonFilterChanged)
        parent.ui.pushButton_selectCounters.clicked.connect(self.addSelectedCounters)
        
    def setSheet(self,sheet):
        self.curSheet=sheet
        self.orgPfmonView.setModel(sheet.orgCountersModel[self.group])
        self.selPfmonView.setModel(sheet.selCountersModel[self.group])

    def pfmonFilterChanged(self):
        syntax = QRegExp.PatternSyntax(QRegExp.Wildcard)
        caseSensitivity = Qt.CaseInsensitive
        regExp = QRegExp(self.pfmonFilter.text(),caseSensitivity, syntax)
        self.curSheet.orgCountersModel[self.group].setFilterRegExp(regExp)

    def addSelectedCounters(self):
        index=self.orgPfmonView.selectedIndexes()
        model=self.curSheet.selCountersModel[self.group]
        for idx in index:           
            item=self.curSheet.orgCountersModel[self.group].itemData(idx)
            sels=self.curSheet.selCounters[self.group]
            if item[0] in sels:
                continue
            model.insertRow(0)
            model.setData(model.index(0,0),item[0])
            sels.append(item[0])
            
