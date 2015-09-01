from utility import *
from collections import defaultdict
from SheetForm import SheetForm
from BatchPfmonTable import BatchPfmonTable
class ChartWindows:
    def __init__(self,parent):
        self.curSheet=False
        self.curChart=False
        self.charts=defaultdict(SheetForm)
        self.parent=parent
        self.chartsView=parent.ui.treeView_charts
        view_name=('Charts',)
        self.chartsModel=createModelOnView(parent,self.chartsView,0,0,view_name)
        parent.ui.pushButton_addChart.clicked.connect(self.addChart)
        parent.ui.pushButton_delChart.clicked.connect(self.delChart)
        parent.ui.pushButton_showChart.clicked.connect(self.showChart)
        parent.ui.treeView_charts.selectionModel().selectionChanged.connect(self.setCurChart)
    def setSheet(self,sheet):
        self.curSheet=sheet

    def addChart(self):
        if not self.curSheet:
            return
        name='chart:'+self.curSheet.name
        chart=SheetForm(name,self.parent,self.curSheet)

        self.charts[name]=chart
        self.curChart=chart
        
        self.chartsModel.insertRow(0)
        self.chartsModel.setData(self.chartsModel.index(0,0),name)
    def delChart(self):
        pass
    def setCurChart(self):
        index=self.chartsView.selectedIndexes()
        if not index:
            return
        n=(self.chartsModel.itemData(index[0]))[0]
        self.curChart=self.charts[n]

    def showChart(self):
        self.parent.curTable=BatchPfmonTable()
        self.parent.curTable.show()
        pass
