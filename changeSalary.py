# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'changeSalary.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(300, 263)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 265, 185))
        self.layoutWidget.setObjectName("layoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.layoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setHorizontalSpacing(50)
        self.formLayout.setVerticalSpacing(10)
        self.formLayout.setObjectName("formLayout")
        self.firstNameLabel = QtWidgets.QLabel(self.layoutWidget)
        self.firstNameLabel.setObjectName("firstNameLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.firstNameLabel)
        self.firstNameLabel_2 = QtWidgets.QLabel(self.layoutWidget)
        self.firstNameLabel_2.setObjectName("firstNameLabel_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.firstNameLabel_2)
        self.lastNameLabel = QtWidgets.QLabel(self.layoutWidget)
        self.lastNameLabel.setObjectName("lastNameLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lastNameLabel)
        self.lastNameLabel_2 = QtWidgets.QLabel(self.layoutWidget)
        self.lastNameLabel_2.setObjectName("lastNameLabel_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lastNameLabel_2)
        self.currentSalaryLabel = QtWidgets.QLabel(self.layoutWidget)
        self.currentSalaryLabel.setObjectName("currentSalaryLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.currentSalaryLabel)
        self.currentSalaryLabel_2 = QtWidgets.QLabel(self.layoutWidget)
        self.currentSalaryLabel_2.setObjectName("currentSalaryLabel_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.currentSalaryLabel_2)
        self.newSalaryLabel = QtWidgets.QLabel(self.layoutWidget)
        self.newSalaryLabel.setObjectName("newSalaryLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.newSalaryLabel)
        self.newSalaryLineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.newSalaryLineEdit.setObjectName("newSalaryLineEdit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.newSalaryLineEdit)
        self.reasonLabel = QtWidgets.QLabel(self.layoutWidget)
        self.reasonLabel.setObjectName("reasonLabel")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.reasonLabel)
        self.salaryLineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.salaryLineEdit.setObjectName("salaryLineEdit")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.salaryLineEdit)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(100, 220, 75, 23))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.firstNameLabel.setText(_translate("MainWindow", "First Name"))
        self.firstNameLabel_2.setText(_translate("MainWindow", "Shameel"))
        self.lastNameLabel.setText(_translate("MainWindow", "Last Name"))
        self.lastNameLabel_2.setText(_translate("MainWindow", "Uddin"))
        self.currentSalaryLabel.setText(_translate("MainWindow", "Current Salary"))
        self.currentSalaryLabel_2.setText(_translate("MainWindow", "99"))
        self.newSalaryLabel.setText(_translate("MainWindow", "New Salary"))
        self.reasonLabel.setText(_translate("MainWindow", "Reason"))
        self.salaryLineEdit.setPlaceholderText(_translate("MainWindow", "Optional"))
        self.pushButton.setText(_translate("MainWindow", "Save"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
