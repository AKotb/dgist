import cv2
from matplotlib import pyplot as plt
from Tkinter import *
from PyQt5.QtCore import QDir
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import (QFileDialog, QMainWindow, QMessageBox)
from PIL import Image


class ImageOperations(QMainWindow):
    def __init__(self):
        super(ImageOperations, self).__init__()


def open(self):
    self.fileName, _ = QFileDialog.getOpenFileName(self, "Open File", QDir.currentPath())
    #self.fileName, _ = QFileDialog.getOpenFileName(self, "Open File", "C:/Users/ahmed.kotb/PycharmProjects/DGIST/resources")
    if self.fileName:
        self.image = QImage(self.fileName)
        if self.image.isNull():
            self.statusBar().showMessage('Image Viewer cannot load file.')
            QMessageBox.information(self, "Image Viewer",
                                    "Cannot load %s." % self.fileName)
            return

        self.imageLabel.setPixmap(QPixmap.fromImage(self.image))
        self.scaleFactor = 1.0

        self.saveAct.setEnabled(True)
        self.fitToWindowAct.setEnabled(True)
        self.metadataAct.setEnabled(True)
        self.histogramAct.setEnabled(True)
        self.changeDetectionAct.setEnabled(True)
        self.reportsAct.setEnabled(True)
        self.updateActions()
        self.statusBar().showMessage('File loaded in Image Viewer.')

        if not self.fitToWindowAct.isChecked():
            self.imageLabel.adjustSize()


def save(self):
    # this is save method
    filename = QFileDialog.getSaveFileName(self, "Save", "", "All Files (*);;TIF Image (*.tif);;PNG Image (*.png);;JPG Image (*.jpg);;Text Files (*.txt)")[0]
    img = cv2.imread(self.fileName)
    cv2.imwrite(filename, img)
    self.statusBar().showMessage('Image saved into ' + filename)


def metadata(self):
    img = Image.open(self.fileName)
    print(img.getbands)
    self.statusBar().showMessage('Metadata generated.')
    root = Tk()
    root.title("Image Metadata")
    root.geometry("500x600")
    frame = Frame(root, bg="blue", width=500, height=600)
    label = Label(frame, text=img)
    frame.pack()
    label.pack()
    root.mainloop()


def histogram(self):
    self.statusBar().showMessage('Histogram generated.')
    img = cv2.imread(self.fileName)
    color = ('b', 'g', 'r')
    for i, col in enumerate(color):
        histr = cv2.calcHist([img], [i], None, [256], [0, 256])
        plt.plot(histr, color=col)
        plt.xlim([0, 256])
    plt.show()


def changeDetection(self):
    print "write Change Detection method code here"
