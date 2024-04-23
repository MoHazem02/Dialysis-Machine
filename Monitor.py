from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1032, 452)
        MainWindow.setMinimumSize(QtCore.QSize(1032, 452))
        MainWindow.setMaximumSize(QtCore.QSize(1201, 521))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Assets/monitor.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color:#3A3B3C;\n"
"color: white;\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.DiasBloodPressureBar = QtWidgets.QProgressBar(self.groupBox)
        self.DiasBloodPressureBar.setGeometry(QtCore.QRect(270, 110, 71, 201))
        self.DiasBloodPressureBar.setStyleSheet("QProgressBar{\n"
"text-align:center;\n"
"color:rgb(54, 163, 0);\n"
"border-radius:10px;\n"
"}\n"
"QProgressBar::chunk{\n"
"background-color:rgb(80, 0, 140);\n"
"border-radius:10px;\n"
"}\n"
"")
        self.DiasBloodPressureBar.setMinimum(40)
        self.DiasBloodPressureBar.setMaximum(120)
        self.DiasBloodPressureBar.setProperty("value", 80)
        self.DiasBloodPressureBar.setTextVisible(False)
        self.DiasBloodPressureBar.setOrientation(QtCore.Qt.Vertical)
        self.DiasBloodPressureBar.setObjectName("DiasBloodPressureBar")
        self.SystBloodPressureBar = QtWidgets.QProgressBar(self.groupBox)
        self.SystBloodPressureBar.setGeometry(QtCore.QRect(30, 120, 71, 191))
        self.SystBloodPressureBar.setStyleSheet("QProgressBar{\n"
"text-align:center;\n"
"color:rgb(54, 163, 0);\n"
"border-radius:10px;\n"
"}\n"
"QProgressBar::chunk{\n"
"background-color:rgb(220, 20, 60);\n"
"border-radius:10px;\n"
"}\n"
"")
        self.SystBloodPressureBar.setMinimum(30)
        self.SystBloodPressureBar.setMaximum(180)
        self.SystBloodPressureBar.setProperty("value", 120)
        self.SystBloodPressureBar.setTextVisible(False)
        self.SystBloodPressureBar.setOrientation(QtCore.Qt.Vertical)
        self.SystBloodPressureBar.setObjectName("SystBloodPressureBar")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(30, 30, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(270, 30, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(10, 330, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(230, 330, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.SystBloodPressureLCD = QtWidgets.QLCDNumber(self.groupBox)
        self.SystBloodPressureLCD.setGeometry(QtCore.QRect(30, 70, 81, 41))
        self.SystBloodPressureLCD.setProperty("value", 120.0)
        self.SystBloodPressureLCD.setObjectName("SystBloodPressureLCD")
        self.DiasBloodPressureLCD = QtWidgets.QLCDNumber(self.groupBox)
        self.DiasBloodPressureLCD.setGeometry(QtCore.QRect(260, 60, 81, 41))
        self.DiasBloodPressureLCD.setProperty("value", 80.0)
        self.DiasBloodPressureLCD.setObjectName("DiasBloodPressureLCD")
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(160, 30, 71, 71))
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap("Assets/heart.png"))
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.BloodFlowRate = QtWidgets.QLCDNumber(self.groupBox_2)
        self.BloodFlowRate.setGeometry(QtCore.QRect(30, 60, 141, 101))
        self.BloodFlowRate.setObjectName("BloodFlowRate")
        self.increase_button = QtWidgets.QPushButton(self.groupBox_2)
        self.increase_button.setEnabled(True)
        self.increase_button.setGeometry(QtCore.QRect(130, 280, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.increase_button.setFont(font)
        self.increase_button.setStyleSheet("background-color: #00A86B;\n"
"    color: white;\n"
"    border: none;\n"
"    padding: 5px 10px;\n"
"     border: 1.2px ;\n"
"border-style: outset;\n"
"border-radius: 8px;")
        self.increase_button.setObjectName("increase_button")
        self.decrease_button = QtWidgets.QPushButton(self.groupBox_2)
        self.decrease_button.setGeometry(QtCore.QRect(30, 280, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.decrease_button.setFont(font)
        self.decrease_button.setStyleSheet("background-color: #E0115F;\n"
"    color: white;\n"
"    border: none;\n"
"    padding: 5px 10px;\n"
"     border: 1.2px ;\n"
"border-style: outset;\n"
"border-radius: 8px;")
        self.decrease_button.setObjectName("decrease_button")
        self.set_button = QtWidgets.QPushButton(self.groupBox_2)
        self.set_button.setGeometry(QtCore.QRect(30, 320, 181, 31))
        self.set_button.setMaximumSize(QtCore.QSize(200, 16777215))
        self.set_button.setStyleSheet("background-color: #784B84;\n"
"    color: white;\n"
"    border: none;\n"
"    padding: 5px 10px;\n"
"     border: 1.2px ;\n"
"border-style: outset;\n"
"border-radius: 8px;")
        self.set_button.setObjectName("set_button")
        self.DesiredBloodFlowRate = QtWidgets.QLCDNumber(self.groupBox_2)
        self.DesiredBloodFlowRate.setGeometry(QtCore.QRect(30, 180, 121, 61))
        self.DesiredBloodFlowRate.setObjectName("DesiredBloodFlowRate")
        self.BloodTemperature = QtWidgets.QLCDNumber(self.groupBox_2)
        self.BloodTemperature.setGeometry(QtCore.QRect(220, 60, 141, 101))
        self.BloodTemperature.setObjectName("BloodTemperature")
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(40, 30, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setGeometry(QtCore.QRect(230, 30, 141, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        self.label_7.setGeometry(QtCore.QRect(40, 250, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_9 = QtWidgets.QLabel(self.groupBox_2)
        self.label_9.setGeometry(QtCore.QRect(380, 80, 81, 81))
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap("Assets/thermometer.png"))
        self.label_9.setScaledContents(True)
        self.label_9.setObjectName("label_9")
        self.ConductivityLCD = QtWidgets.QLCDNumber(self.groupBox_2)
        self.ConductivityLCD.setGeometry(QtCore.QRect(220, 170, 141, 81))
        self.ConductivityLCD.setObjectName("ConductivityLCD")
        self.label_10 = QtWidgets.QLabel(self.groupBox_2)
        self.label_10.setGeometry(QtCore.QRect(240, 260, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.groupBox_2, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1032, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.SystBloodPressureBar.valueChanged['int'].connect(self.SystBloodPressureLCD.display) # type: ignore
        self.DiasBloodPressureBar.valueChanged['int'].connect(self.DiasBloodPressureLCD.display) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Dialysis Monitor"))
        self.groupBox.setTitle(_translate("MainWindow", "Pressure"))
        self.label.setText(_translate("MainWindow", "mmHg"))
        self.label_2.setText(_translate("MainWindow", "mmHg"))
        self.label_3.setText(_translate("MainWindow", "Systolic Blood Pressure"))
        self.label_4.setText(_translate("MainWindow", "Diastolic Blood Pressure"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Flow"))
        self.increase_button.setText(_translate("MainWindow", "+"))
        self.decrease_button.setText(_translate("MainWindow", "-"))
        self.set_button.setText(_translate("MainWindow", "SET"))
        self.label_5.setText(_translate("MainWindow", "Blood Flow Rate"))
        self.label_6.setText(_translate("MainWindow", "Blood Temperature"))
        self.label_7.setText(_translate("MainWindow", "Desired Flow Rate"))
        self.label_10.setText(_translate("MainWindow", "Conductivity"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
