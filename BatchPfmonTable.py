from PyQt5.QtWidgets import QWidget
from SpreadSheet_rc import Ui_Form_SpreadSheet
from PyQt5.QtGui import QStandardItemModel
from PyQt5.QtCore import Qt,QModelIndex
from SheetForm import SheetForm
class BatchPfmonTable(QWidget):
    
    def __init__ (self,sheet):
        self.group=SheetForm.REFER 
        QWidget.__init__(self)
        self.ui=Ui_Form_SpreadSheet()
        self.ui.setupUi(self)
        self.updateTable(sheet)
        
    def updateTable(self,sheet):
        counters=sheet.selCounters[self.group]
        batches=sheet.selBatches[self.group]
        values=sheet.orgCounters[self.group]
        num_b=len(batches)
        rows=len(counters)
        self.model = QStandardItemModel(rows,num_b+1, self)
        self.model.setHeaderData(0, Qt.Horizontal,'Counters')
        
        x=1
        for h in batches:
            self.model.setHeaderData(x, Qt.Horizontal,str(h))
            x+=1
        #self.ui.tableView_pfmonBatchTable.setModel(self.model)
            
        x=1
        y=0
        for cnt in counters:
            self.model.insertRows(y, 1, QModelIndex())
            #self.model.insertRow(y,1)
            self.model.setData(self.model.index(y,0, QModelIndex()),cnt)
            for b in range(num_b):
                self.model.setData(self.model.index(y,x,QModelIndex()),int(values[cnt][b]))
                
                x+=1
            y+=1
            x=1
  
        self.ui.tableView_pfmonBatchTable.setModel(self.model)

