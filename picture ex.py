import sys
from PyQt5.QtWidgets import QLabel, QMainWindow,QApplication,QWidget,QLineEdit,QPushButton,QBoxLayout,QFileDialog
from PyQt5.QtGui import QPixmap

class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.pb = QPushButton("Pixmap")
        self.lb_1 = QLabel()
        self.init_ui()

    def init_ui(self):
        layout = QBoxLayout(QBoxLayout.TopToBottom)
        self.setLayout(layout)

        layout.addWidget(self.pb)
        layout.addWidget(self.lb_1)

        self.pb.clicked.connect(self.save)

    def save(self):
        fname = QFileDialog.getOpenFileName(self, 'Open File')
        pixmap = QPixmap(fname[0])

        self.lb_1.setPixmap(pixmap)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Window()
    form.show()
    exit(app.exec_())