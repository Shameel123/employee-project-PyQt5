# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'salary_position.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 414)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(144, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        self.salaryLogLabel = QtWidgets.QLabel(self.centralwidget)
        self.salaryLogLabel.setObjectName("salaryLogLabel")
        self.gridLayout.addWidget(self.salaryLogLabel, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(145, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 2, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(144, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 0, 3, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 4, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(172, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 0, 5, 1, 2)
        self.salaryTableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.salaryTableWidget.setObjectName("salaryTableWidget")
        self.salaryTableWidget.setColumnCount(0)
        self.salaryTableWidget.setRowCount(0)
        self.gridLayout.addWidget(self.salaryTableWidget, 1, 0, 1, 3)
        self.positionTableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.positionTableWidget.setObjectName("positionTableWidget")
        self.positionTableWidget.setColumnCount(0)
        self.positionTableWidget.setRowCount(0)
        self.gridLayout.addWidget(self.positionTableWidget, 1, 3, 1, 4)
        spacerItem4 = QtWidgets.QSpacerItem(144, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 2, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 2, 1, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(145, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 2, 2, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(144, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem6, 2, 3, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 2, 4, 1, 2)
        spacerItem7 = QtWidgets.QSpacerItem(144, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem7, 2, 6, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.salaryLogLabel.setText(_translate("MainWindow", "Salary Log"))
        self.label_2.setText(_translate("MainWindow", "Position Log"))
        self.pushButton.setText(_translate("MainWindow", "Change Salary"))
        self.pushButton_2.setText(_translate("MainWindow", "Change Position"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
