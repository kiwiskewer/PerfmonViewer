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
        self.verticalLayout = QtWidgets.QVBoxLayout(Form_SpreadSheet)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.tableView_pfmonBatchTable = QtWidgets.QTableView(Form_SpreadSheet)
        self.tableView_pfmonBatchTable.setSortingEnabled(True)
        self.tableView_pfmonBatchTable.setObjectName("tableView_pfmonBatchTable")
        self.gridLayout.addWidget(self.tableView_pfmonBatchTable, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_showRefer = QtWidgets.QPushButton(Form_SpreadSheet)
        self.pushButton_showRefer.setObjectName("pushButton_showRefer")
        self.horizontalLayout.addWidget(self.pushButton_showRefer)
        self.pushButton_showTarget = QtWidgets.QPushButton(Form_SpreadSheet)
        self.pushButton_showTarget.setObjectName("pushButton_showTarget")
        self.horizontalLayout.addWidget(self.pushButton_showTarget)
        self.pushButton_showDiff = QtWidgets.QPushButton(Form_SpreadSheet)
        self.pushButton_showDiff.setObjectName("pushButton_showDiff")
        self.horizontalLayout.addWidget(self.pushButton_showDiff)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Form_SpreadSheet)
        QtCore.QMetaObject.connectSlotsByName(Form_SpreadSheet)

    def retranslateUi(self, Form_SpreadSheet):
        _translate = QtCore.QCoreApplication.translate
        Form_SpreadSheet.setWindowTitle(_translate("Form_SpreadSheet", "Form"))
        self.pushButton_showRefer.setText(_translate("Form_SpreadSheet", "Reference"))
        self.pushButton_showTarget.setText(_translate("Form_SpreadSheet", "Target"))
        self.pushButton_showDiff.setText(_translate("Form_SpreadSheet", "Diff"))

