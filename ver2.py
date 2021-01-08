import sys

from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QTabWidget
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QComboBox
from PyQt5.QtWidgets import QDoubleSpinBox
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QFormLayout
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QGroupBox
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QVBoxLayout

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        tabs = QTabWidget()
        tabs.addTab(TabData(), 'Data')
        tabs.addTab(TabCompare(), 'Comparison')

        self.setCentralWidget(tabs)

        self.setWindowTitle('EBW DB Program by IWA')
        self.show()

class TabData(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        tapdatagrid = QGridLayout()
        tapdatagrid.addWidget(self.groupsetup(), 0, 0)
        tapdatagrid.addWidget(self.grouptestinput(), 1, 0)
        tapdatagrid.addWidget(self.groupcosmetic(), 0, 1)
        tapdatagrid.addWidget(self.grouptestoutput(), 1, 1)
        tapdatagrid.addWidget(self.groupimage(), 0, 2, 2, 2)
        tapdatagrid.addWidget(self.saveButton(),2,3,1,1)

        self.setLayout(tapdatagrid)

    def groupset(self):
        group_setup = QGroupBox('Setup')
        flay_setup = QFormLayout
        group_setup.setLayout(flay_setup)


        array_use = ["Plate", "Tube"]
        self.cb_use = QComboBox()
        self.cb_use.addItems(array_use)

        arrya_weldtype = ["BOP", "Butt", "Lap"]
        self.cb_weldtype = QComboBox()
        self.cb_weldtype.addItems(arrya_weldtype)

        #값을 반환해야 하는 위젯들은 미리 선언해준다.
        self.setup_name = QLineEdit()
        self.setup_company =QLineEdit()

        self.setup_material = QLineEdit()

        self.setup_thickness = QLineEdit()
        self.setup_backth= QLineEdit()

        flay_setup.addRow("Name: ", self.setup_name)
        flay_setup.addRow("Company: ", self.setup_company)
        flay_setup.addRow("Use: ", self.cb_use)
        flay_setup.addRow("Material: ", self.setup_material)
        flay_setup.addRow("Weld Type: ", self.cb_weldtype)
        flay_setup.addRow("Thickness(mm): ", self.setup_thickness)
        flay_setup.addRow("Backing Thickness(mm): ", self.setup_backth)

        return group_setup

    def grouptestinput(self):
        group_testinput = QGroupBox('Test Input')  # groupbox 변수 정의
        flay_testinput = QFormLayout()  # groupbox 형식 변수 정의
        group_testinput.setLayout(flay_testinput)  # groupbox 변수의 형식 입력

        self.array_sc = ["o", "|", "-", "∩", "∪", "oval"]
        self.cb_inputsc = QComboBox()
        self.cb_inputsc.addItems(self.array_sc)

        hlay_sc = QHBoxLayout()
        self.input_sclength1 = QLineEdit()
        self.input_sclength2 = QLineEdit()
        hlay_sc.addWidget(self.input_sclength1)
        hlay_sc.addWidget(self.input_sclength2)

        self.input_fobs = QLineEdit()
        self.input_wd = QLineEdit()
        self.input_bw = QLineEdit()
        self.input_fw = QLineEdit()
        self.input_velocity = QLineEdit()


        flay_testinput.addRow("Fobs(mA): ", self.input_fobs)
        flay_testinput.addRow("WD(mm): ", self.input_wd)
        flay_testinput.addRow("Bw(mA): ", self.input_bw)
        flay_testinput.addRow("Fw(mA): ", self.input_fw)
        flay_testinput.addRow("Velocity(mm/min): ", self.input_velocity)
        flay_testinput.addRow("S.C(mA): ",self.cb_inputsc)
        flay_testinput.addRow(hlay_sc)
        return group_testinput

    def groupcosmetic(self):
        group_cosmetic = QGroupBox('Cosmetic Input')  # groupbox 변수 정의
        flay_cosmetic = QFormLayout()  # groupbox 형식 변수 정의
        group_cosmetic.setLayout(flay_cosmetic)  # groupbox 변수의 형식 입력

        self.cb_cosmeticsc=QComboBox()
        self.cb_cosmeticsc.addItems(self.array_sc)

        hlay_sc = QHBoxLayout()
        self.output_sclength1 = QLineEdit()
        self.output_sclength2 = QLineEdit()
        hlay_sc.addWidget(self.output_sclength1)
        hlay_sc.addWidget(self.output_sclength2)

        self.cosmetic_fobs = QLineEdit()
        self.cosmetic_wd = QLineEdit()
        self.cosmetic_bw = QLineEdit()
        self.cosmetic_fw = QLineEdit()
        self.cosmetic_velocity = QLineEdit()

        flay_cosmetic.addRow("Fobs(mA): ", self.cosmetic_fobs)
        flay_cosmetic.addRow("WD(mm): ", self.cosmetic_wd)
        flay_cosmetic.addRow("Bw(mA): ", self.cosmetic_bw)
        flay_cosmetic.addRow("Fw(mA): ", self.cosmetic_fw)
        flay_cosmetic.addRow("Velocity(mm/min): ", self.cosmetic_velocity)
        flay_cosmetic.addRow("S.C(mA): ",self.cb_cosmeticsc)
        flay_cosmetic.addRow(hlay_sc)
        return group_cosmetic

    def grouptestoutput(self):
        group_testoutput = QGroupBox("Output")
        flay_testoutput = QFormLayout()
        group_testoutput.setLayout(flay_testoutput)

                   



    def groupimage(self):

    def saveButton(self):
        lay_sB = QHBoxLayout()
        lay_sB.addWidget()

class TabCompare(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        name = QLabel('Name:')
        nameedit = QLineEdit()
        age = QLabel('Age:')
        ageedit = QLineEdit()
        nation = QLabel('Nation:')
        nationedit = QLineEdit()

        vbox = QVBoxLayout()
        vbox.addWidget(name)
        vbox.addWidget(nameedit)
        vbox.addWidget(age)
        vbox.addWidget(ageedit)
        vbox.addWidget(nation)
        vbox.addWidget(nationedit)
        vbox.addStretch()

        self.setLayout(vbox)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec_())



