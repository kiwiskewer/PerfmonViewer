from PyQt5.QtGui import QStandardItemModel
from PyQt5.QtCore import QRegExp, QSortFilterProxyModel,Qt
from PyQt5.QtWidgets import QAbstractItemView


def createModel(parent,rows,cols,colNames):
    model=QStandardItemModel(rows, cols+1, parent)
    i=0
    for c in colNames:
        model.setHeaderData(i, Qt.Horizontal, c)
        i+=1
    proxyModel=QSortFilterProxyModel()
    proxyModel.setDynamicSortFilter(True)
    proxyModel.setSourceModel(model)
    proxyModel.setFilterKeyColumn(0)
    return proxyModel


def initView(view):
    view.setAlternatingRowColors(True)
    
    view.setSortingEnabled(True)
    view.sortByColumn(0, Qt.AscendingOrder)
    #view.setSelectionMode(QAbstractItemView.SingleSelection)

def createModelOnView(parent,view, rows,cols,colNames):
    model = createModel(parent,rows,cols,colNames)
    initView(view)
    view.setModel(model)       

    return model