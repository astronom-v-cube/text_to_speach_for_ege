from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(993, 404)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(200, 290, 131, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(360, 0, 621, 381))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 181, 341))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.groupBox)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 20, 141, 311))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        self.radioButton_3.setObjectName("radioButton_3")
        self.verticalLayout_2.addWidget(self.radioButton_3)
        self.radioButton_4 = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        self.radioButton_4.setObjectName("radioButton_4")
        self.verticalLayout_2.addWidget(self.radioButton_4)
        self.radioButton_5 = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        self.radioButton_5.setObjectName("radioButton_5")
        self.verticalLayout_2.addWidget(self.radioButton_5)
        self.radioButton_7 = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        self.radioButton_7.setObjectName("radioButton_7")
        self.verticalLayout_2.addWidget(self.radioButton_7)
        self.radioButton_6 = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        self.radioButton_6.setObjectName("radioButton_6")
        self.verticalLayout_2.addWidget(self.radioButton_6)
        self.radioButton_21 = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        self.radioButton_21.setObjectName("radioButton_21")
        self.verticalLayout_2.addWidget(self.radioButton_21)
        self.radioButton_22 = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        self.radioButton_22.setObjectName("radioButton_22")
        self.verticalLayout_2.addWidget(self.radioButton_22)
        self.radioButton_23 = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        self.radioButton_23.setObjectName("radioButton_23")
        self.verticalLayout_2.addWidget(self.radioButton_23)
        self.radioButton_24 = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        self.radioButton_24.setObjectName("radioButton_24")
        self.verticalLayout_2.addWidget(self.radioButton_24)
        self.radioButton_25 = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        self.radioButton_25.setObjectName("radioButton_25")
        self.verticalLayout_2.addWidget(self.radioButton_25)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(220, 10, 91, 111))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.groupBox_2)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 20, 51, 81))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.radioButton_2 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButton_2.setObjectName("radioButton_2")
        self.verticalLayout.addWidget(self.radioButton_2)
        self.radioButton = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButton.setObjectName("radioButton")
        self.verticalLayout.addWidget(self.radioButton)
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(200, 140, 151, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit.setGeometry(QtCore.QRect(10, 20, 131, 31))
        self.lineEdit.setObjectName("lineEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 993, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Text to speach"))
        self.pushButton.setText(_translate("MainWindow", "Сохранить"))
        self.groupBox.setTitle(_translate("MainWindow", "Скорость воспроизведения"))
        self.radioButton_3.setText(_translate("MainWindow", "0,75"))
        self.radioButton_4.setText(_translate("MainWindow", "0,9"))
        self.radioButton_5.setText(_translate("MainWindow", "1"))
        self.radioButton_7.setText(_translate("MainWindow", "1,1"))
        self.radioButton_6.setText(_translate("MainWindow", "1,2"))
        self.radioButton_21.setText(_translate("MainWindow", "1,3"))
        self.radioButton_22.setText(_translate("MainWindow", "1,4"))
        self.radioButton_23.setText(_translate("MainWindow", "1,5"))
        self.radioButton_24.setText(_translate("MainWindow", "1,75"))
        self.radioButton_25.setText(_translate("MainWindow", "2"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Акцент"))
        self.radioButton_2.setText(_translate("MainWindow", "US"))
        self.radioButton.setText(_translate("MainWindow", "UK "))
        self.groupBox_3.setTitle(_translate("MainWindow", "Имя файла"))

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.create_mp3)

    def create_mp3(self):

        text = self.textEdit.toPlainText() 

        if self.radioButton_3.isChecked():
            speed = 0.75
            print("Выбрана: radioButton_3")
        elif self.radioButton_4.isChecked():
            speed = 0.9
            print("Выбрана: radioButton_4")
        elif self.radioButton_5.isChecked():
            speed = 1
            print("Выбрана: radioButton_5")
        elif self.radioButton_6.isChecked():
            speed = 1.1
            print("Выбрана: radioButton_6")
        elif self.radioButton_21.isChecked():
            speed = 1.2
            print("Выбрана: radioButton_21")
        elif self.radioButton_22.isChecked():
            speed = 1.3
            print("Выбрана: radioButton_22")
        elif self.radioButton_23.isChecked():
            speed = 1.4
            print("Выбрана: radioButton_23")
        elif self.radioButton_25.isChecked():
            speed = 1.5
            print("Выбрана: radioButton_25")
        elif self.radioButton_26.isChecked():
            speed = 1.75
            print("Выбрана: radioButton_26")
        elif self.radioButton_27.isChecked():
            speed = 2
            print("Выбрана: radioButton_27")
    



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
