# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'changePosition.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(345, 264)
        MainWindow.setWindowIcon(QtGui.QIcon("icon.ico"))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setHorizontalSpacing(50)
        self.formLayout.setVerticalSpacing(10)
        self.formLayout.setObjectName("formLayout")
        self.firstNameLabel = QtWidgets.QLabel(self.centralwidget)
        self.firstNameLabel.setObjectName("firstNameLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.firstNameLabel)
        self.firstNameLabel_2 = QtWidgets.QLabel(self.centralwidget)
        self.firstNameLabel_2.setObjectName("firstNameLabel_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.firstNameLabel_2)
        self.lastNameLabel = QtWidgets.QLabel(self.centralwidget)
        self.lastNameLabel.setObjectName("lastNameLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lastNameLabel)
        self.lastNameLabel_2 = QtWidgets.QLabel(self.centralwidget)
        self.lastNameLabel_2.setObjectName("lastNameLabel_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lastNameLabel_2)
        self.currentPositionLabel = QtWidgets.QLabel(self.centralwidget)
        self.currentPositionLabel.setObjectName("currentPositionLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.currentPositionLabel)
        self.currentPositionLabel_2 = QtWidgets.QLabel(self.centralwidget)
        self.currentPositionLabel_2.setObjectName("currentPositionLabel_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.currentPositionLabel_2)
        self.salaryLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.salaryLineEdit.setPlaceholderText("")
        self.salaryLineEdit.setObjectName("salaryLineEdit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.salaryLineEdit)
        self.reasonLabel = QtWidgets.QLabel(self.centralwidget)
        self.reasonLabel.setObjectName("reasonLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.reasonLabel)
        self.gridLayout.addLayout(self.formLayout, 0, 0, 1, 3)
        spacerItem = QtWidgets.QSpacerItem(117, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(117, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)



        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        app.aboutToQuit.connect(self.closeEvent)



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.firstNameLabel.setText(_translate("MainWindow", "First Name"))
        self.firstNameLabel_2.setText(_translate("MainWindow", "Shameel"))
        self.lastNameLabel.setText(_translate("MainWindow", "Last Name"))
        self.lastNameLabel_2.setText(_translate("MainWindow", "Uddin"))
        self.currentPositionLabel.setText(_translate("MainWindow", "Current Position"))
        self.currentPositionLabel_2.setText(_translate("MainWindow", "Jr. InfoSec Officer"))
        self.reasonLabel.setText(_translate("MainWindow", "New Position"))
        self.pushButton.setText(_translate("MainWindow", "Save"))


    def closeEvent(self):
        #Your code here

        print("Shameel!")
        # import sys
        # sys.exit(0)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
