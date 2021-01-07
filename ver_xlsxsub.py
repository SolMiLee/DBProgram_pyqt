import sys

import openpyxl
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QHBoxLayout

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 200, 200)
        winlay = QVBoxLayout()

        lb1 = QLabel("값1")
        lbe1 = QLineEdit(self)
        self.lbe1 =lbe1

        btn1 = QPushButton("이미지")
        btn1.clicked.connect(self.ImagebuttonClicked)
        self.lbl_im = QLabel()

        btn_exsave = QPushButton("Existing File")
        btn_exsave.clicked.connect(self.savebtnEXfile)

        winlay.addWidget(lb1)
        winlay.addWidget(self.lbe1)
        winlay.addWidget(btn1)
        winlay.addWidget(self.lbl_im)
        winlay.addWidget(btn_exsave)

        winlay.addStretch(4)

        centralWidget = QWidget()
        centralWidget.setLayout(winlay)
        self.setCentralWidget(centralWidget)
        self.show()

    def ImagebuttonClicked(self):
        self.fname = QFileDialog.getOpenFileName(self, 'Open File')
        fnim = self.fname[0]
        self.fnim = fnim
        pixmap = QPixmap(self.fname[0])
        self.lbl_im.setPixmap(pixmap)
        gogo
        # print(self.fnim)
        # C:/Users/IWA-LSM/Desktop/EBW/DBProgram_pyqt/input.PNG

    def savebtnEXfile(self):
        fname_ex = QFileDialog.getOpenFileName(self,'')
        fnameee_ex=fname_ex[0]
        self.fnameee_ex = fnameee_ex
        wb_ex = openpyxl.Workbook('%s'%self.fnameee_ex)