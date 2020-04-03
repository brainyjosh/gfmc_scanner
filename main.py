# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'file.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

def detect_text(path):
    """Detects text in the file."""
    # print('hello world')
    from google.cloud import vision
    import io
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations
    print('Texts:')

    for text in texts:
        print('\n"{}"'.format(text.description))

        vertices = (['({},{})'.format(vertex.x, vertex.y)
                    for vertex in text.bounding_poly.vertices])

        print('bounds: {}'.format(','.join(vertices)))

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))
                print(text)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        MainWindow.setMaximumSize(QtCore.QSize(640, 480))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(220, 30, 181, 41))
        self.label.setStyleSheet("font: 75 24pt \"Monospace\";")
        self.label.setObjectName("label")
        pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 80, 621, 31))
        self.pushButton.setObjectName("pushButton")
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
        pushButton.clicked.connect(detect_text('files/brainy.JPG'))
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Image OCR"))
        self.label.setText(_translate("MainWindow", "Image OCR"))
        self.pushButton.setText(_translate("MainWindow", "Select File"))
        self.pushButton_2.setText(_translate("MainWindow", "Run"))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))
        self.actionOpen_FIle.setText(_translate("MainWindow", "Open FIle"))
        self.actionQR_code.setText(_translate("MainWindow", "QR code"))
        self.actionAbout_Image_OCR.setText(_translate("MainWindow", "About Image OCR"))
        self.actionAbout_Us.setText(_translate("MainWindow", "About Us"))
        # btn_brow_2 = QtGui.QPushButton('Dir browser', self)
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
