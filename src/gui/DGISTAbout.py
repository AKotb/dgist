from PyQt5.QtWidgets import (QMessageBox)


class DGISTAbout:
    def __init__(self):
        super(DGISTAbout, self).__init__()


def about(QMainWindow):
    QMessageBox.about(QMainWindow, " About DGIST",
                      "<p><b>DGIST</b> is an open-source multi-platform toolbox for "
                      "viewing, processing and archiving remotely sensed raster/vector data. "
                      "It offers a comprehensive, growing set of geospatial data analysis and processing methods "
                      "such as monitoring temporal changes using different techniques. </p>"
                      "NARSS <b>DGIST</b> Version <b>1.0</b>")