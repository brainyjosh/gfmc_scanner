import sys
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtGui import QIcon
import json
import csv

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'CEPH Zone 1 Publicity Team'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        # self.openFileNameDialog()
        self.openFileNamesDialog()
        # self.saveFileDialog()
        
        # self.show()
 
    
    def openFileNamesDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        files, _ = QFileDialog.getOpenFileNames(self,"QFileDialog.getOpenFileNames()", "","All Files (*);;Python Files (*.py)", options=options)
        # newfiles = json.dumps(files)
        if files:
            # lenght = len(newfiles)
            for path in files:
               
                # print('hello world')
                    from google.cloud import vision
                    import io
                    client = vision.ImageAnnotatorClient()

                    with io.open(path, 'rb') as image_file:
                        content = image_file.read()

                    image = vision.types.Image(content=content)

                    response = client.text_detection(image=image)
                    texts = response.full_text_annotation
                    string = texts.text.split("\n")

                    # for x in string:
                    #     with open('csvfile.csv', "w") as csv_file:
                    #             writer = csv.writer(csv_file, delimiter=',')
                    #             writer.writerow(x)
                    
                    # with open("csvfile.csv", "w") as file:
                    #     writer = csv.writer(file)
                    #     writer.writerows(string)

                    
                    import csv

                    with open('csvfile.csv', mode='w') as employee_file:
                        employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

                        employee_writer.writerow(string)
                        # employee_writer.writerow(['Erica Meyers', 'IT', 'March'])

                    print('Image Details:')
                    print(texts.text)
                    # for text in texts:
                    #     result = '\n"{}"'.format(text.description)
                    #     print(type(text))
                        # vertices = (['({},{})'.format(vertex.x, vertex.y)
                        #             for vertex in text.bounding_poly.vertices])

                        # print('bounds: {}'.format(','.join(vertices)))

                    if response.error.message:
                        raise Exception(
                            '{}\nFor more info on error messages, check: '
                            'https://cloud.google.com/apis/design/errors'.format(
                                response.error.message))
                                            # print(text)
                                # for lenght in newfiles:
                                #     print(newfiles)
                        
                        # def saveFileDialog(self):

                        # for x in string:
                            
                        #     options = QFileDialog.Options()
                        #     options |= QFileDialog.DontUseNativeDialog
                        #     fileName, _ = QFileDialog.getSaveFileName(self,"QFileDialog.getSaveFileName()","","All Files (*);;Text Files (*.txt)", options=options)
                        #     if fileName:
                        #         print(fileName)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
