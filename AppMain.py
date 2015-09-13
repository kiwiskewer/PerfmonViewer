import sys

from PyQt5.QtWidgets import QApplication, QMainWindow,QFileDialog,QWidget
from collections import defaultdict
#from PyQt5 import QtCore,QtGui
from numpy import array

from MainWindow_rc import Ui_MainWindow


from ChartSheet import ChartSheet
from PerfmonReader import pfreader
from BatchPfmonTable import BatchPfmonTable
from utility import *

        

class TheMainWindow(QMainWindow):
    #class TheMainWindow(QWidget):
    
    def __init__(self):
        super().__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle('Start')
        self.refPerfFile=False
        self.TargetPerfFile=False
        self.sheet=ChartSheet(self,'Default')
        self.chart=None

        self.counters=[defaultdict(list) for i in range(3)]
        self.modelCounters=createModel(self,0,0,('CounterName',))
        self.modelBatches=createModel(self,0,1,('batch_id','batch_type'))

        self.viewAllCounters=self.ui.treeView_pfmons
        self.viewSelectedCounters=self.ui.treeView_pfmonSelected
        self.viewAllBatches=self.ui.treeView_batches
        self.viewSelectedBatches=self.ui.treeView_batchSelected

        self.viewAllCounters.setModel(self.modelCounters)
        self.viewSelectedCounters.setModel(self.sheet.modelCounters)
        self.viewAllBatches.setModel(self.modelBatches)
        self.viewSelectedBatches.setModel(self.sheet.modelBatches)


        self.pfmonFilter=self.ui.lineEdit_pfmonFilter
        self.ui.lineEdit_pfmonFilter.textChanged.connect(self.pfmonFilterChanged)
        self.ui.pushButton_selectCounters.clicked.connect(self.addSelectedCounters)

        self.batchFilter=self.ui.lineEdit_batchFilter
        self.ui.lineEdit_batchFilter.textChanged.connect(self.batchFilterChanged)
        self.ui.pushButton_selBatches.clicked.connect(self.addSelectedBatches)
        #Actions
        
        #Project
        self.ui.actionOpen.triggered.connect(self.openPrj)
        self.ui.actionSave.triggered.connect(self.savePrj)
        self.ui.actionSave_As.triggered.connect(self.saveAsPrj)

        self.ui.pushButton_LoadRef.clicked.connect(self.setRefFileName)
        self.ui.pushButton_LoadTarget.clicked.connect(self.setTargetFileName)

        #Sheet/Chart 
        self.chartsView=self.ui.treeView_charts
        view_name=('Charts',)
        self.chartsModel=createModelOnView(self,self.chartsView,0,0,view_name)
        self.ui.pushButton_addChart.clicked.connect(self.addChart)
        self.ui.pushButton_delChart.clicked.connect(self.delChart)
        self.ui.pushButton_showChart.clicked.connect(self.showChart)
        self.ui.treeView_charts.selectionModel().selectionChanged.connect(self.setCurChart)
        #Perf/Batches
        
        #self.ui.treeView_charts.selectionModel().selectionChanged.connect(self.updatePerfBatch_chart)
        self.show()

    def openPrj(self):
        fileName, _ = QFileDialog.getOpenFileName(self)
        if not fileName:
            return
        with open(fileName) as f:
            self.ui.label_prj.setText(fileName)
            #wins=f.readlines()
            wins=f.read().splitlines()
            self.ui.listWidget_spreadSheets.addItems(wins)

    def savePrj(self):
        pass

    def saveAsPrj(self):
        pass

    def setRefFileName(self):  
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self,
                "Get Reference Perfmon", self.ui.label_RefFile.text(),
                "All Files (*);;Text Files (*.txt)", options=options)
        if fileName:
            self.ui.label_RefFile.setText(fileName)
            self.counters[0]=pfreader(fileName)
#            self.modelCounters.clear()
            
            for pname in self.counters[0].keys():
                self.modelCounters.insertRow(0) 
                self.modelCounters.setData(self.modelCounters.index(0, 0), pname)
            

            for b in range(len(self.counters[0]['batch_id'])):
                self.modelBatches.insertRow(0)
                d=self.counters[0]['batch_id'][b]
                self.modelBatches.setData(self.modelBatches.index(0,0),int(d))
                d=self.counters[0]['batch_type'][b]
                self.modelBatches.setData(self.modelBatches.index(0,1),int(d))
            self.calcDiff()                               


    def setTargetFileName(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self,
                "Get Target Perfmon", self.ui.label_TargetFile.text(),
                "All Files (*);;Text Files (*.txt)", options=options)
        if fileName:
            self.ui.label_TargetFile.setText(fileName)
            self.counters[1]=pfreader(fileName)
            self.calcDiff()
            
    def calcDiff(self):
        if not self.counters[0]:
            return 
        if not self.counters[1]:
            return
        for k in self.counters[0]:
            ref=array(self.counters[0][k])
            tgt=array(self.counters[1][k])
            self.counters[2][k]=(tgt-ref).tolist()

    def pfmonFilterChanged(self):
        syntax = QRegExp.PatternSyntax(QRegExp.Wildcard)
        caseSensitivity = Qt.CaseInsensitive
        regExp = QRegExp(self.pfmonFilter.text(),caseSensitivity, syntax)
        self.modelCounters.setFilterRegExp(regExp)

    def batchFilterChanged(self):
        syntax = QRegExp.PatternSyntax(QRegExp.Wildcard)
        caseSensitivity = Qt.CaseInsensitive
        regExp = QRegExp(self.batchFilter.text(),caseSensitivity, syntax)
        self.modelBatches.setFilterRegExp(regExp)

    def addSelectedCounters(self):
        index=self.viewAllCounters.selectedIndexes()
        model=self.sheet.modelCounters
        for idx in index:           
            item=self.modelCounters.itemData(idx)
            self.sheet.addCounter(item[0])

        

    def addSelectedBatches(self):
        index=self.viewAllBatches.selectedIndexes()
        org_model=self.modelBatches
        for idx in index: 
            row=idx.row()          
            b_id=org_model.itemData(org_model.index(row,0))[0]
            b_type=org_model.itemData(org_model.index(row,1))[0]
            self.sheet.addBatche(b_id,b_type)
    def addChart():
        pass
    def delChart():
        pass
    def setCurChart():
        return
    def showChart(self):
        if not self.chart:
            self.chart=BatchPfmonTable(self)
            self.chart.show()
        else:
            self.chart.updateAllTables(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = TheMainWindow()
    sys.exit(app.exec_())


