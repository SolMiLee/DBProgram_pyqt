from PyQt5 import QtCore, QtGui, QtWidgets
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("BiPolar Power Supply Testing")
        tab_widget = QtWidgets.QTabWidget()
        self.setCentralWidget(tab_widget)

        pstest_widget = QtWidgets.QWidget()
        tab_widget.addTab(pstest_widget, "PS Tests")
        pstest_vlay = QtWidgets.QVBoxLayout(pstest_widget)
        for i in range(1, 9):
            title = "PS{}".format(i)
            group_box = MainWindow.create_pstest_element(title)
            pstest_vlay.addWidget(group_box)
        self.PSFStart_btn = QtWidgets.QPushButton("Start")
        self.PSFStop_btn = QtWidgets.QPushButton("Stop")
        pstest_vlay.addWidget(self.PSFStart_btn)
        pstest_vlay.addWidget(self.PSFStop_btn)
        pstest_vlay.addStretch()

        pscalib_widget = QtWidgets.QWidget()
        tab_widget.addTab(pscalib_widget, "PS Calib")
        pscalib_vlay = QtWidgets.QVBoxLayout(pscalib_widget)
        group_box = MainWindow.create_pscalib_element("PS")
        self.PSCalibStart_btn = QtWidgets.QPushButton("Calib Start")
        self.PSCalibStop_btn = QtWidgets.QPushButton("Calib Stop")
        pscalib_vlay.addWidget(group_box)
        pscalib_vlay.addWidget(self.PSCalibStart_btn)
        pscalib_vlay.addWidget(self.PSCalibStop_btn)
        pscalib_vlay.addStretch()
    @staticmethod
    def create_pstest_element(title):
        group_box = QtWidgets.QGroupBox(title)
        grid = QtWidgets.QGridLayout()
        group_box.setLayout(grid)
        serial_label = QtWidgets.QLabel("Serial No:")
        serial_lineedit = QtWidgets.QLineEdit("XXXX")
        chipid_label = QtWidgets.QLabel("Chip ID:")
        chipid_lineedit = QtWidgets.QLineEdit("XXXX")
        rd_group = QtWidgets.QButtonGroup()
        rdbtn_FCB15 = QtWidgets.QRadioButton("FCB-15")
        rdbtn_DCB15 = QtWidgets.QRadioButton("DCB-15")
        grid.addWidget(serial_label, 0, 0)
        grid.addWidget(serial_lineedit, 0, 1)
        grid.addWidget(rdbtn_FCB15, 0, 2)
        grid.addWidget(rdbtn_DCB15, 0, 3)
        grid.addWidget(chipid_label, 1, 0)
        grid.addWidget(chipid_lineedit, 1, 1)
        return group_box
    @staticmethod
    def create_pscalib_element(title):
        group_box = QtWidgets.QGroupBox(title)
        flay = QtWidgets.QFormLayout()
        group_box.setLayout(flay)
        serial_lineedit = QtWidgets.QLineEdit("XXXX")
        chipid_lineedit = QtWidgets.QLineEdit("XXXX")
        qrcode_lineedit = QtWidgets.QLineEdit("XXXX")
        range_lineedit = QtWidgets.QLineEdit("1.0")
        offset_lineedit = QtWidgets.QLineEdit("0.0", readOnly=True)
        gain_lineedit = QtWidgets.QLineEdit("1.0", readOnly=True)
        flay.addRow("Serial No:", serial_lineedit)
        flay.addRow("Chip ID:", chipid_lineedit)
        flay.addRow("QR Code:", qrcode_lineedit)
        flay.addRow("Current Range:", range_lineedit)
        flay.addRow("PS Offset:", offset_lineedit)
        flay.addRow("PS Gain:", gain_lineedit)
        return group_box
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())