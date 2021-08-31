# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'f:\00-CQB Work\04 - TDPHA\Main-5-APP_for_use\FLIPPED.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(566, 521)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.FilePath = QtWidgets.QTextBrowser(self.centralwidget)
        self.FilePath.setObjectName("FilePath")
        self.verticalLayout.addWidget(self.FilePath)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.verticalLayout.addWidget(self.comboBox)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.FitResults = QtWidgets.QTextBrowser(self.centralwidget)
        self.FitResults.setObjectName("FitResults")
        self.verticalLayout.addWidget(self.FitResults)
        self.RunFit = QtWidgets.QPushButton(self.centralwidget)
        self.RunFit.setObjectName("RunFit")
        self.verticalLayout.addWidget(self.RunFit)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.PredictResults = QtWidgets.QTextBrowser(self.centralwidget)
        self.PredictResults.setObjectName("PredictResults")
        self.verticalLayout.addWidget(self.PredictResults)
        self.RunPrediction = QtWidgets.QPushButton(self.centralwidget)
        self.RunPrediction.setObjectName("RunPrediction")
        self.verticalLayout.addWidget(self.RunPrediction)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 566, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.actionImport_Data = QtWidgets.QAction(MainWindow)
        self.actionImport_Data.setObjectName("actionImport_Data")
        self.actionSave_Data = QtWidgets.QAction(MainWindow)
        self.actionSave_Data.setObjectName("actionSave_Data")
        self.actionClear_All = QtWidgets.QAction(MainWindow)
        self.actionClear_All.setObjectName("actionClear_All")
        self.actionClear = QtWidgets.QAction(MainWindow)
        self.actionClear.setObjectName("actionClear")
        self.menu.addAction(self.actionImport_Data)
        self.menu.addAction(self.actionSave_Data)
        self.menu.addAction(self.actionClear)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Data Path -&gt;</span></p></body></html>"))
        self.FilePath.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:11.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Please import data for fitting and predicting!</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">[Files-&gt;import data]</p></body></html>"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Select Function Type -&gt;</span></p></body></html>"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Linear"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Exponential"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Parameter Estimation</span></p></body></html>"))
        self.RunFit.setText(_translate("MainWindow", "Run Estimation"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Prediction of PHA (%)</span></p></body></html>"))
        self.RunPrediction.setText(_translate("MainWindow", "Run Predction"))
        self.menu.setTitle(_translate("MainWindow", "Files"))
        self.actionImport_Data.setText(_translate("MainWindow", "Import Data"))
        self.actionSave_Data.setText(_translate("MainWindow", "Save Data"))
        self.actionClear_All.setText(_translate("MainWindow", "Clear All"))
        self.actionClear.setText(_translate("MainWindow", "Clear All"))