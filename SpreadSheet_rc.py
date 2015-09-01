# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SpreadSheet.ui'
#
# Created by: PyQt5 UI code generator 5.5
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form_SpreadSheet(object):
    def setupUi(self, Form_SpreadSheet):
        Form_SpreadSheet.setObjectName("Form_SpreadSheet")
        Form_SpreadSheet.resize(813, 697)
        self.gridLayout_2 = QtWidgets.QGridLayout(Form_SpreadSheet)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.tableView_pfmonBatchTable = QtWidgets.QTableView(Form_SpreadSheet)
        self.tableView_pfmonBatchTable.setSortingEnabled(True)
        self.tableView_pfmonBatchTable.setObjectName("tableView_pfmonBatchTable")
        self.gridLayout.addWidget(self.tableView_pfmonBatchTable, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(Form_SpreadSheet)
        QtCore.QMetaObject.connectSlotsByName(Form_SpreadSheet)

    def retranslateUi(self, Form_SpreadSheet):
        _translate = QtCore.QCoreApplication.translate
        Form_SpreadSheet.setWindowTitle(_translate("Form_SpreadSheet", "Form"))

