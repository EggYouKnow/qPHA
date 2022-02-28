# main

import sys
import PyQt5
from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow
import pathlib

import Ui_FLIPPED
from _functions import *

class MainDialog(QMainWindow):
    def __init__(self, parent=None):
        super(QMainWindow, self).__init__(parent)
        self.ui = Ui_FLIPPED.Ui_MainWindow()
        self.ui.setupUi(self)
        QMainWindow.setWindowTitle(self, 'qPHAcells(beta) v0.2')
        QMainWindow.setWindowIcon(self, QIcon('Green_PHA.ico'))

        # data
        self.ui.actionImport_Data.triggered.connect(self.open_file)
        self.ui.actionSave_Data.triggered.connect(self.save_file)
        self.ui.actionClear.triggered.connect(self.clear_all)
        self.fit_dt = 'None'

        # fit
        self.param = []
        self.ui.RunFit.clicked.connect(self.fit)

        # predict
        self.ui.RunPrediction.clicked.connect(self.predict)

    def open_file(self):
        fileName, fileType = QtWidgets.QFileDialog.getOpenFileName(self, "Load File", str(pathlib.Path.cwd()),
                                                                   "CSV Files(*.csv)")
        if 'csv' in fileType:
            self.ui.FilePath.setText(fileName)
            self.fit_dt, self.pred_dt = load_data(fileName)
        else:
            self.ui.FilePath.setText(
                'Please select a .csv file! [Files -> import data]')

    def fit(self):
        funcname = self.ui.comboBox.currentText()

        if self.fit_dt == 'None':
            self.ui.FitResults.setText('Please Import Data!')
            return None

        if funcname == 'Linear' and self.fit_dt != 'None':
            self.param, r_2 = fit_surface(self.fit_dt, funcname)
            output = 'PHA (%) = a*(OD-b1)/(k*(FI-b2)-(OD-b1))'
            output = output+'\n'+'||a=%.2E|b1=%.2E|b2=%.2E|k=%.2E||' %(self.param[0], self.param[1], self.param[2], self.param[3])
            output = output + '\n'+'> R_squared=%.2f <' % r_2

        elif funcname == 'Exponential' and self.fit_dt != 'None':
            self.param, r_2 = fit_surface(self.fit_dt, funcname)
            output = 'OD = b1 + a*(FI-b2)*PHA(%)/[exp(k*PHA(%))+c]'
            output = output+'\n'+'||a=%.2E|b1=%.2E|b2=%.2E|k=%.2E|c=%.2E||' \
                % (self.param[0], self.param[1], self.param[2], self.param[3], self.param[4])
            output = output + '\n'+'> R_squared=%.2f <' % r_2

        self.ui.FitResults.setText(output)

    def predict(self):
        funcname = self.ui.comboBox.currentText()

        if self.fit_dt == 'None':
            self.ui.PredictResults.setText('Please Import Data!')
            return None

        if funcname == 'Linear' and len(self.param) != 4:
            self.pred_dt['Pha(%)'] = pred_PHA(self.pred_dt, funcname, [])
            self.ui.FitResults.setText(
                'Using default parameters of linear function!')
        elif funcname == 'Exponential' and len(self.param) != 5:
            self.pred_dt['Pha(%)'] = pred_PHA(self.pred_dt, funcname, [])
            self.ui.FitResults.setText(
                'Using default parameters of exponential function!')
        else:
            self.pred_dt['Pha(%)'] = pred_PHA(
                self.pred_dt, funcname, self.param)

        output = 'OD600 |  FI  | PHA (%) |'
        for i in range(len(self.pred_dt['Pha(%)'])):
            output = output + "\n" + "%.1f | %.1f | %.2f |" \
                % (self.pred_dt["OD"][i], self.pred_dt["FI"][i], self.pred_dt["Pha(%)"][i])

        self.ui.PredictResults.setText(output)

    def save_file(self):
        dirpath, _ = QtWidgets.QFileDialog.getSaveFileName(self, "New File", str(pathlib.Path.cwd()),
                                                           "CSV Files(*.csv)")

        if 'csv' in dirpath:
            save_array = np.zeros((len(self.pred_dt['OD']), 3))
            save_array[:, 0] = self.pred_dt['OD']
            save_array[:, 1] = self.pred_dt['FI']
            save_array[:, 2] = self.pred_dt['Pha(%)']
            np.savetxt(dirpath, save_array,
                       delimiter=',', fmt='%.2f',
                       header="OD,FI,PHA (%)", comments="")

    def clear_all(self):
        self.param = []
        self.pred_dt = []
        self.fit_dt = 'None'

        self.ui.FitResults.setText('')
        self.ui.PredictResults.setText('')
        self.ui.FilePath.setText(
            'Please select a .csv file! [Files -> import data]')



if __name__ == "__main__":
    app = QApplication(sys.argv)
    mDlg = MainDialog()
    mDlg.show()
    sys.exit(app.exec_())

