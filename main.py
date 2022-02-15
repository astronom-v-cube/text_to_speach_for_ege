# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design_3.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(960, 320)
        self.setWindowIcon(QIcon('icon.ico'))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.group_speed = QtWidgets.QGroupBox(self.centralwidget)
        self.group_speed.setGeometry(QtCore.QRect(10, 10, 121, 291))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.group_speed.setFont(font)
        self.group_speed.setObjectName("group_speed")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.group_speed)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 20, 101, 256))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.radioButton = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButton.setObjectName("radioButton")
        self.verticalLayout.addWidget(self.radioButton)
        self.radioButton_2 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButton_2.setObjectName("radioButton_2")
        self.verticalLayout.addWidget(self.radioButton_2)
        self.radioButton_3 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButton_3.setChecked(True)
        self.radioButton_3.setObjectName("radioButton_3")
        self.verticalLayout.addWidget(self.radioButton_3)
        self.radioButton_4 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButton_4.setObjectName("radioButton_4")
        self.verticalLayout.addWidget(self.radioButton_4)
        self.radioButton_5 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButton_5.setObjectName("radioButton_5")
        self.verticalLayout.addWidget(self.radioButton_5)
        self.radioButton_6 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButton_6.setObjectName("radioButton_6")
        self.verticalLayout.addWidget(self.radioButton_6)
        self.radioButton_7 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButton_7.setObjectName("radioButton_7")
        self.verticalLayout.addWidget(self.radioButton_7)
        self.radioButton_8 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButton_8.setObjectName("radioButton_8")
        self.verticalLayout.addWidget(self.radioButton_8)
        self.radioButton_9 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButton_9.setObjectName("radioButton_9")
        self.verticalLayout.addWidget(self.radioButton_9)
        self.radioButton_10 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButton_10.setObjectName("radioButton_10")
        self.verticalLayout.addWidget(self.radioButton_10)
        self.group_accent = QtWidgets.QGroupBox(self.centralwidget)
        self.group_accent.setGeometry(QtCore.QRect(150, 10, 71, 91))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.group_accent.setFont(font)
        self.group_accent.setObjectName("group_accent")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.group_accent)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 20, 51, 61))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.radioButton_11 = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setItalic(False)
        font.setStrikeOut(False)
        self.radioButton_11.setFont(font)
        self.radioButton_11.setChecked(True)
        self.radioButton_11.setObjectName("radioButton_11")
        self.verticalLayout_2.addWidget(self.radioButton_11)
        self.radioButton_12 = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        self.radioButton_12.setObjectName("radioButton_12")
        self.verticalLayout_2.addWidget(self.radioButton_12)
        self.group_text_editor = QtWidgets.QGroupBox(self.centralwidget)
        self.group_text_editor.setGeometry(QtCore.QRect(280, 10, 671, 281))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.group_text_editor.setFont(font)
        self.group_text_editor.setObjectName("group_text_editor")
        self.textEdit = QtWidgets.QTextEdit(self.group_text_editor)
        self.textEdit.setGeometry(QtCore.QRect(10, 20, 651, 251))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(140, 240, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.group_file_name = QtWidgets.QGroupBox(self.centralwidget)
        self.group_file_name.setGeometry(QtCore.QRect(140, 120, 131, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.group_file_name.setFont(font)
        self.group_file_name.setObjectName("group_file_name")
        self.lineEdit = QtWidgets.QLineEdit(self.group_file_name)
        self.lineEdit.setGeometry(QtCore.QRect(10, 20, 111, 31))
        self.lineEdit.setObjectName("lineEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 961, 21))
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
        self.group_speed.setTitle(_translate("MainWindow", "Скорость"))
        self.radioButton.setText(_translate("MainWindow", "0.8"))
        self.radioButton_2.setText(_translate("MainWindow", "0.9"))
        self.radioButton_3.setText(_translate("MainWindow", "1"))
        self.radioButton_4.setText(_translate("MainWindow", "1.1"))
        self.radioButton_5.setText(_translate("MainWindow", "1.2"))
        self.radioButton_6.setText(_translate("MainWindow", "1.3"))
        self.radioButton_7.setText(_translate("MainWindow", "1.4"))
        self.radioButton_8.setText(_translate("MainWindow", "1.5"))
        self.radioButton_9.setText(_translate("MainWindow", "1.75"))
        self.radioButton_10.setText(_translate("MainWindow", "2"))
        self.group_accent.setTitle(_translate("MainWindow", "Акцент"))
        self.radioButton_11.setText(_translate("MainWindow", "UK"))
        self.radioButton_12.setText(_translate("MainWindow", "US"))
        self.group_text_editor.setTitle(_translate("MainWindow", "Текст"))
        self.pushButton.setText(_translate("MainWindow", "Сохранить"))
        self.group_file_name.setTitle(_translate("MainWindow", "Имя файла"))


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.create_mp3)

    def create_mp3(self):

        from gtts import gTTS
        import ffmpeg

        pronunciation_UK = 'co.uk'  
        pronunciation_US = 'com'

        if self.radioButton.isChecked():
            speed = 0.8
        elif self.radioButton_2.isChecked():
            speed = 0.9
        elif self.radioButton_3.isChecked():
            speed = 1
        elif self.radioButton_4.isChecked():
            speed = 1.1
        elif self.radioButton_5.isChecked():
            speed = 1.2
        elif self.radioButton_6.isChecked():
            speed = 1.3
        elif self.radioButton_7.isChecked():
            speed = 1.4
        elif self.radioButton_8.isChecked():
            speed = 1.5
        elif self.radioButton_9.isChecked():
            speed = 1.75
        elif self.radioButton_10.isChecked():
            speed = 2
        
        if self.radioButton_11.isChecked():
            pronunciation = pronunciation_UK
        elif self.radioButton_12.isChecked():
            pronunciation = pronunciation_US

        text = self.textEdit.toPlainText()
        name = self.lineEdit.text()

        tts = gTTS(text, lang = 'en', tld = pronunciation)
        tts.save(f'{name}.mp3')
        
"""         (
            ffmpeg
            .input(f'{name}.mp3')
            .output(f'{name}.mp3', atempo=speed)
            .run()
        ) """

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    m = MainWindow()
    m.show()
    sys.exit(app.exec_())