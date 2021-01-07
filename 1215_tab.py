import sys
from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap


class MainWindow(QtWidgets.QMainWindow):
    """ def가 클래스 내부에서 쓰이면 메서드라고 한다.
    _붙은건 클래스 내부에서만 쓰는 함수니까 함부로 쓰지마라고 명시하는뜻
    """
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("EBW DB Program")
        tab_widget = QtWidgets.QTabWidget()
        self.setCentralWidget(tab_widget)

        # input/output tab
        ioputdata_widget = QtWidgets.QWidget()
        tab_widget.addTab(ioputdata_widget, "Input/Output data")
        ioputdata_glay = QtWidgets.QGridLayout(ioputdata_widget)

        # setup layout
        group_box1 = MainWindow.create_setup_element("Setup")
        ioputdata_glay.addWidget(group_box1, 0, 0)

        # testinput layout
        group_box2 = MainWindow.create_testinput_element("Test input")
        ioputdata_glay.addWidget(group_box2, 1, 0)

        # output_layout
        group_box5 = MainWindow.create_output_element(self)
        ioputdata_glay.addWidget(group_box5,0,1)

        # image_layout
        group_box3 = MainWindow.create_image_element(self)
        ioputdata_glay.addWidget(group_box3, 0, 2)

        # cosmetic_layout
        group_box4 = MainWindow.create_cosmetic_element(self)
        ioputdata_glay.addWidget(group_box4,1,1)

        # comparison tab
        comparison_widget = QtWidgets.QWidget()
        tab_widget.addTab(comparison_widget, "Comparison")
        comparison_glay = QtWidgets.QGridLayout(comparison_widget)

        # input_comparison_data
        group_box6 = MainWindow.create_dtcomparison_element(self)
        comparison_glay.addWidget(group_box6,0,0)

    def create_setup_element(self):
        group_box = QtWidgets.QGroupBox(self)
        flay = QtWidgets.QFormLayout()
        group_box.setLayout(flay)

        use_combo = QtWidgets.QComboBox()
        use_combo.addItems({"Plate", "Tube"})

        weldtype_combo = QtWidgets.QComboBox()
        weldtype_combo.addItems({"BOP", "Butt", "Lap"})

        flay.addRow("Name: ", QtWidgets.QLineEdit())
        flay.addRow("Company: ", QtWidgets.QLineEdit())
        flay.addRow("Use: ", use_combo)
        flay.addRow("Material: ", QtWidgets.QLineEdit())
        flay.addRow("Weld Type: ", weldtype_combo)
        flay.addRow("Thickness(mm): ", QtWidgets.QDoubleSpinBox())
        flay.addRow("Backing Thickness(mm): ", QtWidgets.QDoubleSpinBox())
        return group_box

    def create_testinput_element(self):
        group_box = QtWidgets.QGroupBox(self)
        flay = QtWidgets.QFormLayout()
        group_box.setLayout(flay)

        #콤보박스 아이템 변수화
        sc_combo = QtWidgets.QComboBox()
        sc_combo.addItems({"o", "|", "-", "∩", "∪", "oval"})
        sc_hlay = QtWidgets.QHBoxLayout()
        sc_hlay.addWidget(QtWidgets.QDoubleSpinBox())
        sc_hlay.addWidget(QtWidgets.QDoubleSpinBox())

        flay.addRow("Fobs(mA): ", QtWidgets.QDoubleSpinBox())
        flay.addRow("WD(mm): ", QtWidgets.QDoubleSpinBox())
        flay.addRow("Bw(mA): ", QtWidgets.QDoubleSpinBox())
        flay.addRow("Fw(mA): ", QtWidgets.QDoubleSpinBox())
        flay.addRow("Velocity(mm/min): ", QtWidgets.QDoubleSpinBox())
        flay.addRow("S.C(mA): ", sc_combo)
        flay.addRow(sc_hlay)
        return group_box

    def create_cosmetic_element(self):
        group_box = QtWidgets.QGroupBox("Cosmetic")
        flay = QtWidgets.QFormLayout()
        group_box.setLayout(flay)

        group_box.setCheckable(True)
        group_box.setCheckable(True)

        sc_combo = QtWidgets.QComboBox()
        sc_combo.addItems({"o", "|", "-", "∩", "∪", "oval"})
        sc_hlay = QtWidgets.QHBoxLayout()
        sc_hlay.addWidget(QtWidgets.QDoubleSpinBox())
        sc_hlay.addWidget(QtWidgets.QDoubleSpinBox())

        flay.addRow("Fobs(mA): ", QtWidgets.QDoubleSpinBox())
        flay.addRow("WD(mm): ", QtWidgets.QDoubleSpinBox())
        flay.addRow("Bw(mA): ", QtWidgets.QDoubleSpinBox())
        flay.addRow("Fw(mA): ", QtWidgets.QDoubleSpinBox())
        flay.addRow("Velocity(mm/min): ", QtWidgets.QDoubleSpinBox())
        flay.addRow("S.C(mA): ", sc_combo)
        flay.addRow(sc_hlay)
        return group_box

    def create_output_element(self):
        group_box = QtWidgets.QGroupBox("Output")
        flay = QtWidgets.QFormLayout()
        group_box.setLayout(flay)

        flay.addRow("Bead Width(mm): ", QtWidgets.QDoubleSpinBox())
        flay.addRow("Bead Height(mm): ", QtWidgets.QDoubleSpinBox())
        flay.addRow("Back Width(mm): ", QtWidgets.QDoubleSpinBox())
        flay.addRow("Back Height(mm): ", QtWidgets.QDoubleSpinBox())
        flay.addRow("50% Width(mm): ", QtWidgets.QDoubleSpinBox())
        flay.addRow("50% Height(mm): ", QtWidgets.QDoubleSpinBox())
        flay.addRow("Crack(mm): ", QtWidgets.QDoubleSpinBox())
        flay.addRow("Porosity(mm): ", QtWidgets.QDoubleSpinBox())
        return group_box

    def create_image_element(self):
        group_box = QtWidgets.QGroupBox("Image")
        flay = QtWidgets.QFormLayout()
        group_box.setLayout(flay)

        lb_image = QtWidgets.QLabel()

        btn_open = QtWidgets.QPushButton("Open")

        flay.addWidget(btn_open)
        flay.addWidget(lb_image)

        btn_open.clicked.connect(self.btnOpenRun)

        return group_box

    def btnOpenRun(self):
        fname = QtWidgets.QFileDialog.getOpenFileName(self, 'Open File')
        pixmap = QPixmap(fname[0])
        self.lbimage.setPixmap(pixmap)
        

    def create_dtcomparison_element(self):
        group_box = QtWidgets.QGroupBox()
        flay = QtWidgets.QFormLayout()
        group_box.setLayout(flay)

        use_combo = QtWidgets.QComboBox()
        use_combo.addItems({"Plate", "Tube"})

        weldtype_combo = QtWidgets.QComboBox()
        weldtype_combo.addItems({"BOP", "Butt", "Lap"})

        sc_combo = QtWidgets.QComboBox()
        sc_combo.addItems({"o", "|", "-", "∩", "∪", "oval"})
        sc_hlay = QtWidgets.QHBoxLayout()
        sc_hlay.addWidget(QtWidgets.QDoubleSpinBox())
        sc_hlay.addWidget(QtWidgets.QDoubleSpinBox())

        flay.addRow("Name: ", QtWidgets.QLineEdit())
        flay.addRow("Company: ", QtWidgets.QLineEdit())
        flay.addRow("Use: ", use_combo)
        flay.addRow("Material: ", QtWidgets.QLineEdit())
        flay.addRow("Weld Type: ", weldtype_combo)
        flay.addRow("Thickness(mm): ", QtWidgets.QDoubleSpinBox())
        flay.addRow("Backing Thickness(mm): ", QtWidgets.QDoubleSpinBox())
        flay.addRow("Fobs(mA): ", QtWidgets.QDoubleSpinBox())
        flay.addRow("WD(mm): ", QtWidgets.QDoubleSpinBox())
        flay.addRow("Bw(mA): ", QtWidgets.QDoubleSpinBox())
        flay.addRow("Fw(mA): ", QtWidgets.QDoubleSpinBox())
        flay.addRow("Velocity(mm/min): ", QtWidgets.QDoubleSpinBox())
        flay.addRow("S.C(mA): ", sc_combo)
        flay.addRow(sc_hlay)
        flay.addRow("Bead Width(mm): ", QtWidgets.QDoubleSpinBox())
        flay.addRow("Bead Height(mm): ", QtWidgets.QDoubleSpinBox())
        flay.addRow("Back Width(mm): ", QtWidgets.QDoubleSpinBox())
        flay.addRow("Back Height(mm): ", QtWidgets.QDoubleSpinBox())
        flay.addRow("50% Width(mm): ", QtWidgets.QDoubleSpinBox())
        flay.addRow("50% Height(mm): ", QtWidgets.QDoubleSpinBox())
        flay.addRow("Crack(mm): ", QtWidgets.QDoubleSpinBox())
        flay.addRow("Porosity(mm): ", QtWidgets.QDoubleSpinBox())

        return group_box

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
