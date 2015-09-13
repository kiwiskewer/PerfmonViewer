from PyQt5.QtWidgets import QWidget
from SpreadSheet_rc import Ui_Form_SpreadSheet
from PyQt5.QtGui import QStandardItemModel
from PyQt5.QtCore import Qt,QModelIndex
from ChartSheet import ChartSheet
class BatchPfmonTable(QWidget):
    
    def __init__ (self,parent):
        self.sel=0
        self.parent=parent
        QWidget.__init__(self)
        self.ui=Ui_Form_SpreadSheet()
        self.ui.setupUi(self)
        self.modelTable=[None]*3

        self.updateAllTables(parent)
        self.ui.pushButton_showRefer.clicked.connect(self.showRef)
        self.ui.pushButton_showTarget.clicked.connect(self.showTarget)
        self.ui.pushButton_showDiff.clicked.connect(self.showDiff)

    def updateTable(self,sel):
        if not self.parent.counters[sel]:
            return
        counters=self.parent.sheet.counters
        batches=self.parent.sheet.batches
        values=self.parent.counters[sel]
        num_b=len(batches)
        rows=len(counters)
        self.modelTable[sel] = QStandardItemModel(rows,num_b+1, self)
        model=self.modelTable[sel]
        model.setHeaderData(0, Qt.Horizontal,'Counters')
     
        x=1
        for h in batches:
            model.setHeaderData(x, Qt.Horizontal,str(h))
            x+=1
        #self.ui.tableView_pfmonBatchTable.setModel(self.model)
            
        x=1
        y=0
        for cnt in counters:
            model.insertRows(y, 1, QModelIndex())
            #self.model.insertRow(y,1)
            model.setData(model.index(y,0, QModelIndex()),cnt)
            for b in batches:
                model.setData(model.index(y,x,QModelIndex()),int(values[cnt][b]))               
                x+=1
            y+=1
            x=1

    def updateAllTables(self,parent):
        for i in range(3):
            self.updateTable(i)
        self.ui.tableView_pfmonBatchTable.setModel(self.modelTable[self.sel])
    
    def showRef(self):
        self.showIt(0)

    def showTarget(self):
        self.showIt(1)
    def showDiff(self):
        self.showIt(2)

    def showIt(self,i):
        self.ui.tableView_pfmonBatchTable.setModel(self.modelTable[i])
