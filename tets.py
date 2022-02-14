import sys
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(368, 182)
        MainWindow.setMouseTracking(False)
        MainWindow.setAcceptDrops(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.project_name = QtWidgets.QTextEdit(self.centralwidget)
        self.project_name.setEnabled(True)
        self.project_name.setGeometry(QtCore.QRect(140, 10, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.project_name.setFont(font)
        self.project_name.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.project_name.setMouseTracking(False)
        self.project_name.setTabletTracking(False)
        self.project_name.setAcceptDrops(True)
        self.project_name.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.project_name.setInputMethodHints(QtCore.Qt.ImhMultiLine)
        self.project_name.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.project_name.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.project_name.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.project_name.setTabChangesFocus(False)
        self.project_name.setUndoRedoEnabled(True)
        self.project_name.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.project_name.setReadOnly(False)
        self.project_name.setOverwriteMode(False)
        self.project_name.setAcceptRichText(True)
        self.project_name.setObjectName("project_name")
        self.label_name = QtWidgets.QLabel(self.centralwidget)
        self.label_name.setGeometry(QtCore.QRect(10, 10, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_name.setFont(font)
        self.label_name.setObjectName("label_name")
        self.label_token = QtWidgets.QLabel(self.centralwidget)
        self.label_token.setGeometry(QtCore.QRect(10, 50, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_token.setFont(font)
        self.label_token.setObjectName("label_token")
        self.vk_token = QtWidgets.QTextEdit(self.centralwidget)
        self.vk_token.setGeometry(QtCore.QRect(80, 50, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.vk_token.setFont(font)
        self.vk_token.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.vk_token.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.vk_token.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.vk_token.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.vk_token.setObjectName("vk_token")
        self.radio_group = QtWidgets.QRadioButton(self.centralwidget)
        self.radio_group.setGeometry(QtCore.QRect(10, 90, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.radio_group.setFont(font)
        self.radio_group.setObjectName("radio_group")
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(260, 100, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setUnderline(False)
        font.setKerning(True)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
        self.button_start = QtWidgets.QPushButton(self.centralwidget)
        self.button_start.setGeometry(QtCore.QRect(10, 130, 351, 23))
        self.button_start.setObjectName("button_start")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setEnabled(False)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 368, 21))
        self.menubar.setDefaultUp(False)
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Шаблон Чат-Бота ВК"))
        self.label_name.setText(_translate("MainWindow", "Имя проекта"))
        self.label_token.setText(_translate("MainWindow", "Токен"))
        self.radio_group.setText(_translate("MainWindow", "Группа"))
        self.radioButton_2.setText(_translate("MainWindow", "Аккаунт"))
        self.button_start.setText(_translate("MainWindow", "Сделать шаблон бота"))


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.button_start.clicked.connect(self.create_bot)

    def create_bot(self):
        project_name = self.project_name.toPlainText()
        vk_token = self.vk_token.toPlainText()
        if not project_name:
            print("Введите имя проекта.")
            return
        if not vk_token:
            print("Введите токен апи.")
            return

        if self.radio_group.isChecked():
           print("Выбрана: radio_group")
        elif self.radioButton_2.isChecked():
           print("Выбрана: radioButton_2")    
        else:
           print("Ничего не выбрано.")             


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    m = MainWindow()
    m.show()
    sys.exit(app.exec_())