# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainmenu.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from manageEmployee import EmployeeWindow
from charts import ChartsWindow

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(300, 386)
        MainWindow.setMinimumSize(QtCore.QSize(250, 200))
        MainWindow.setMaximumSize(QtCore.QSize(300, 400))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        self.manageEmployeeButton = QtWidgets.QPushButton(self.centralwidget)
        self.manageEmployeeButton.setMinimumSize(QtCore.QSize(200, 30))
        self.manageEmployeeButton.setObjectName("manageEmployeeButton")
        self.gridLayout.addWidget(self.manageEmployeeButton, 1, 0, 1, 1)
        self.viewChartsButton = QtWidgets.QPushButton(self.centralwidget)
        self.viewChartsButton.setMinimumSize(QtCore.QSize(200, 30))
        self.viewChartsButton.setObjectName("viewChartsButton")
        self.gridLayout.addWidget(self.viewChartsButton, 2, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 3, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Main Menu"))
        self.manageEmployeeButton.setText(_translate("MainWindow", "Manage Employees"))
        self.viewChartsButton.setText(_translate("MainWindow", "View Charts"))


#---------------------------


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.manageEmployeeButton.clicked.connect(self.manage_employees_button_clicked)
        self.ui.viewChartsButton.clicked.connect(self.view_charts_button_clicked)

    def manage_employees_button_clicked(self):
        #print("Manage Employee Clicked!")
        self.hide()
        self.employeeWindow = EmployeeWindow(self)
        self.employeeWindow.show()

    def view_charts_button_clicked(self):
        #print("view Charts Clicked!")
        self.hide()
        self.chartsWindow = ChartsWindow(self)
        self.chartsWindow.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
