import sys

from PyQt5.QtWidgets import QApplication, QMainWindow,QFileDialog,QWidget
from collections import defaultdict
#from PyQt5 import QtCore,QtGui

from MainWindow_rc import Ui_MainWindow
from Ui_SpreadSheet import Ui_Form_SpreadSheet

from TopWindows import TopWindows
from PerfmonWindows import PerfmonWindows
from BatchWindows import BatchWindows
from ChartWindows import ChartWindows
from SheetForm import SheetForm


        

class TheMainWindow(QMainWindow):
    #class TheMainWindow(QWidget):
    
    def __init__(self):
        super().__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle('Start')
        self.refPerfFile=False
        self.TargetPerfFile=False
        self.defaultSheet=None
        
        
        self.winPfmon=PerfmonWindows(self)
        self.winBatch=BatchWindows(self)
        self.winChart=ChartWindows(self)
        self.top=TopWindows(self)
                
        self.show()

        #Actions
        
        #Project
            #Menu
        self.ui.actionOpen.triggered.connect(self.openPrj)
        self.ui.actionSave.triggered.connect(self.savePrj)
        self.ui.actionSave_As.triggered.connect(self.saveAsPrj)
            #buttons
        self.ui.pushButton_LoadRef.clicked.connect(self.setRefFileName)
        self.ui.pushButton_LoadTarget.clicked.connect(self.setTargetFileName)
        self.ui.pushButton_calcDiff.clicked.connect(self.calcDiff)
        #Sheet/Chart 
        
        #Perf/Batches
        
        #self.ui.treeView_charts.selectionModel().selectionChanged.connect(self.updatePerfBatch_chart)


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
            self.refPerfFile=fileName
            self.top.loadDataFromFile(fileName,SheetForm.REFER)
            sheet=self.top.addSheet('DefaultSheet')
            self.top.reloadData(SheetForm.REFER)
            self.top.selectSheet(sheet)


    def setTargetFileName(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self,
                "Get Target Perfmon", self.ui.label_TargetFile.text(),
                "All Files (*);;Text Files (*.txt)", options=options)
        if fileName:
            self.ui.label_TargetFile.setText(fileName)
            self.TargetPerfFile=fileName
            self.top.loadDataFromFile(fileName,SheetForm.TARGET)
            sheet=self.top.addSheet('DefaultSheet')
            self.top.reloadData(SheetForm.TARGET)
            self.top.selectSheet(sheet)
            
    def calcDiff(self):
        pass
        #self.top.loadDataFromFile(self.refPerfFile,self.TargetPerfFile)


    def sheetSelected(self,sheet):
        self.winChart.setSheet(sheet)
        self.winPfmon.setSheet(sheet)
        self.winBatch.setSheet(sheet)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = TheMainWindow()
    sys.exit(app.exec_())


