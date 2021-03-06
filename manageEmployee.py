
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(651, 458)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.upperGridLayour = QtWidgets.QGridLayout()
        self.upperGridLayour.setObjectName("upperGridLayour")
        self.toolButton = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton.setObjectName("toolButton")
        self.upperGridLayour.addWidget(self.toolButton, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(588, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.upperGridLayour.addItem(spacerItem, 0, 1, 1, 1)
        self.gridLayout_4.addLayout(self.upperGridLayour, 0, 0, 1, 1)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.departmentLabel = QtWidgets.QLabel(self.widget)
        self.departmentLabel.setObjectName("departmentLabel")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.departmentLabel)
        self.departmentLineEdit = QtWidgets.QLineEdit(self.widget)
        self.departmentLineEdit.setMaximumSize(QtCore.QSize(300, 16777215))
        self.departmentLineEdit.setObjectName("departmentLineEdit")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.departmentLineEdit)
        self.salaryLabel = QtWidgets.QLabel(self.widget)
        self.salaryLabel.setObjectName("salaryLabel")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.salaryLabel)
        self.salaryLineEdit = QtWidgets.QLineEdit(self.widget)
        self.salaryLineEdit.setMaximumSize(QtCore.QSize(300, 16777215))
        self.salaryLineEdit.setObjectName("salaryLineEdit")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.salaryLineEdit)
        self.positionLabel = QtWidgets.QLabel(self.widget)
        self.positionLabel.setObjectName("positionLabel")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.positionLabel)
        self.positionLineEdit = QtWidgets.QLineEdit(self.widget)
        self.positionLineEdit.setMaximumSize(QtCore.QSize(300, 16777215))
        self.positionLineEdit.setObjectName("positionLineEdit")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.positionLineEdit)
        self.gridLayout_2.addLayout(self.formLayout_2, 0, 4, 1, 1)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.idLabel = QtWidgets.QLabel(self.widget)
        self.idLabel.setObjectName("idLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.idLabel)
        self.idLineEdit = QtWidgets.QLineEdit(self.widget)
        self.idLineEdit.setMaximumSize(QtCore.QSize(300, 16777215))
        self.idLineEdit.setObjectName("idLineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.idLineEdit)
        self.firstNameLabel = QtWidgets.QLabel(self.widget)
        self.firstNameLabel.setObjectName("firstNameLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.firstNameLabel)
        self.firstNameLineEdit = QtWidgets.QLineEdit(self.widget)
        self.firstNameLineEdit.setMaximumSize(QtCore.QSize(300, 16777215))
        self.firstNameLineEdit.setObjectName("firstNameLineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.firstNameLineEdit)
        self.lastNameLabel = QtWidgets.QLabel(self.widget)
        self.lastNameLabel.setObjectName("lastNameLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.lastNameLabel)
        self.lastNameLineEdit = QtWidgets.QLineEdit(self.widget)
        self.lastNameLineEdit.setMaximumSize(QtCore.QSize(300, 16777215))
        self.lastNameLineEdit.setObjectName("lastNameLineEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lastNameLineEdit)
        self.birthdayLabel = QtWidgets.QLabel(self.widget)
        self.birthdayLabel.setObjectName("birthdayLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.birthdayLabel)
        self.birthdayLineEdit = QtWidgets.QLineEdit(self.widget)
        self.birthdayLineEdit.setMaximumSize(QtCore.QSize(300, 16777215))
        self.birthdayLineEdit.setObjectName("birthdayLineEdit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.birthdayLineEdit)
        self.gridLayout_2.addLayout(self.formLayout, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 0, 5, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 0, 2, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem3, 0, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem4, 0, 3, 1, 1)
        self.gridLayout_4.addWidget(self.widget, 1, 0, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        spacerItem5 = QtWidgets.QSpacerItem(198, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem5, 0, 0, 1, 1)
        self.applyButton = QtWidgets.QPushButton(self.centralwidget)
        self.applyButton.setObjectName("applyButton")
        self.gridLayout_3.addWidget(self.applyButton, 0, 1, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_3.addWidget(self.pushButton_2, 0, 2, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(218, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem6, 0, 3, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_3, 2, 0, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.gridLayout_4.addWidget(self.tableWidget, 3, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.backButton = QtWidgets.QPushButton(self.centralwidget)
        self.backButton.setObjectName("backButton")
        self.gridLayout.addWidget(self.backButton, 0, 1, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(198, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem7, 0, 0, 1, 1)
        self.newButton = QtWidgets.QPushButton(self.centralwidget)
        self.newButton.setObjectName("newButton")
        self.gridLayout.addWidget(self.newButton, 0, 2, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 0, 3, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout, 4, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.toolButton.setText(_translate("MainWindow", "..."))
        self.departmentLabel.setText(_translate("MainWindow", "Department"))
        self.salaryLabel.setText(_translate("MainWindow", "Salary"))
        self.positionLabel.setText(_translate("MainWindow", "Position"))
        self.idLabel.setText(_translate("MainWindow", "ID"))
        self.firstNameLabel.setText(_translate("MainWindow", "Firt Name"))
        self.lastNameLabel.setText(_translate("MainWindow", "Last Name"))
        self.birthdayLabel.setText(_translate("MainWindow", "Birth Day"))
        self.applyButton.setText(_translate("MainWindow", "Apply"))
        self.pushButton_2.setText(_translate("MainWindow", "Reset"))
        self.backButton.setText(_translate("MainWindow", "Back"))
        self.newButton.setText(_translate("MainWindow", "New"))
        self.pushButton_3.setText(_translate("MainWindow", "Export"))

class EmployeeWindow(QtWidgets.QMainWindow):
    def __init__(self, mainMenu): #main window written here because we need to  take reference from parent class, also when we press                                   back button, we need to go to main window

        super(EmployeeWindow,self).__init__()
        self.mainMenu = mainMenu

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
