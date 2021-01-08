import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QComboBox
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QVBoxLayout

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.use_combo = QComboBox()
        self.use_combo.addItems({"Plate", "Tube"})
        self.use_combo.setGeometry(10, 10, 100, 30)

        self.lb_combo = QLabel()
        self.lb_combo.setGeometry(150, 10, 50, 30)

        lay = QVBoxLayout()
        lay.addWidget(self.use_combo)
        lay.addWidget(self.lb_combo)

        self.use_combo.activated[str].connect(self.onAc)

        self.setLayout(lay)
        self.show()

    def onAc(self, text):
        self.lb_combo.setText(text)
        self.lb_combo.adjustSize()
        print(self.use_combo.currentText())

        """
        use_combo.currentText() 현재 선택된 combo값을 보여줌
        """

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
