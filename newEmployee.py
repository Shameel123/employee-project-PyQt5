# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newEmployee.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(283, 232)
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
        self.firstNameLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.firstNameLineEdit.setObjectName("firstNameLineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.firstNameLineEdit)
        self.lastNameLabel = QtWidgets.QLabel(self.centralwidget)
        self.lastNameLabel.setObjectName("lastNameLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lastNameLabel)
        self.lastNameLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lastNameLineEdit.setObjectName("lastNameLineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lastNameLineEdit)
        self.birthdayLabel = QtWidgets.QLabel(self.centralwidget)
        self.birthdayLabel.setObjectName("birthdayLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.birthdayLabel)
        self.toolButton = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton.setText("")
        self.toolButton.setObjectName("toolButton")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.toolButton)
        self.departmentLabel = QtWidgets.QLabel(self.centralwidget)
        self.departmentLabel.setObjectName("departmentLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.departmentLabel)
        self.deparmentLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.deparmentLineEdit.setObjectName("deparmentLineEdit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.deparmentLineEdit)
        self.salaryLabel = QtWidgets.QLabel(self.centralwidget)
        self.salaryLabel.setObjectName("salaryLabel")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.salaryLabel)
        self.salaryLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.salaryLineEdit.setObjectName("salaryLineEdit")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.salaryLineEdit)
        self.positionLabel = QtWidgets.QLabel(self.centralwidget)
        self.positionLabel.setObjectName("positionLabel")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.positionLabel)
        self.positionLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.positionLineEdit.setObjectName("positionLineEdit")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.positionLineEdit)
        self.gridLayout.addLayout(self.formLayout, 0, 0, 1, 3)
        spacerItem = QtWidgets.QSpacerItem(84, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(88, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.firstNameLabel.setText(_translate("MainWindow", "First Name"))
        self.lastNameLabel.setText(_translate("MainWindow", "Last Name"))
        self.birthdayLabel.setText(_translate("MainWindow", "Birthday"))
        self.departmentLabel.setText(_translate("MainWindow", "Department"))
        self.salaryLabel.setText(_translate("MainWindow", "Salary"))
        self.positionLabel.setText(_translate("MainWindow", "Position"))
        self.pushButton.setText(_translate("MainWindow", "Save"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
