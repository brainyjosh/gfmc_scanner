# Primidac
# Brainy


from PyQt5 import QtCore, QtGui, QtWidgets
from filed import App

class Ui_MainWindow(object):
    def filemanager(self):
        self.window = QtWidgets.QWidget()
        self.ui = App()
        # self.ui.initUI(self.window)
        # self.window.show()
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 700)
        MainWindow.setMaximumSize(QtCore.QSize(640, 700))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(220, 30, 181, 41))
        self.label.setStyleSheet("font: 75 24pt \"Monospace\";")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 80, 621, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.filemanager)
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(20, 120, 601, 271))
        self.graphicsView.setObjectName("graphicsView")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(270, 400, 100, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 25))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen_FIle = QtWidgets.QAction(MainWindow)
        self.actionOpen_FIle.setObjectName("actionOpen_FIle")
        self.actionQR_code = QtWidgets.QAction(MainWindow)
        self.actionQR_code.setObjectName("actionQR_code")
        self.actionAbout_Image_OCR = QtWidgets.QAction(MainWindow)
        self.actionAbout_Image_OCR.setObjectName("actionAbout_Image_OCR")
        self.actionAbout_Us = QtWidgets.QAction(MainWindow)
        self.actionAbout_Us.setObjectName("actionAbout_Us")
        self.menuMenu.addAction(self.actionOpen_FIle)
        self.menuMenu.addAction(self.actionQR_code)
        self.menuAbout.addAction(self.actionAbout_Image_OCR)
        self.menuAbout.addAction(self.actionAbout_Us)
        self.menubar.addAction(self.menuMenu.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "GFMC Portal"))
        self.label.setText(_translate("MainWindow", "GFMC Portal"))
        self.pushButton.setText(_translate("MainWindow", "Select File"))
        self.pushButton_2.setText(_translate("MainWindow", "Run"))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))
        self.actionOpen_FIle.setText(_translate("MainWindow", "Open FIle"))
        self.actionQR_code.setText(_translate("MainWindow", "QR code"))
        self.actionAbout_Image_OCR.setText(_translate("MainWindow", "About Image OCR"))
        self.actionAbout_Us.setText(_translate("MainWindow", "About Us"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
