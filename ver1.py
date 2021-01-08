import sys

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
from PyQt5.QtWidgets import QTabWidget
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QWidget

"""
    QMainWindow에서는 Qlayout사용 불가
    자체 Layout만 사용가능
"""


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        tabs = QTabWidget()
        tabs.addTab(Tabdata(), 'Data')
        tabs.addTab(Tabcompare(), 'Comparison')

        btn_save = QPushButton('Save', self)
        btn_save.clicked.connect(self.SelectFileSave)

        # tab and button display
        win_vbox = QVBoxLayout()
        win_vbox.addWidget(tabs)
        win_vbox.addWidget(btn_save)

        self.setLayout(win_vbox)

        self.setWindowTitle('EBW DB Program by IWA')
        self.show()

    """
    저장 버튼을 누르면 새로운 파일로 데이터를 저장할 것인지 
    기존의 파일에 저장할 것인지 선택하는 창을 띄워야한다.
    """
    # def SelectFileSave(self):
    #     self.dialog.setWindowTitle('어떤 파일에 저장하시겠습니까?')
    #     btn_newfile = QPushButton("New File", self)
    #     btn_existfile = QPushButton("Existing File", self)
    #     self.show()
    #
    # # def newdatafile(self):


"""
첫번째 탭은 데이터를 입력하는 곳입니다.
해당 시편의 정보, 실험값, 실험 결과 값등과 시편의 이미지를 입력합니다.
"""


class Tabdata(QWidget):
    def __init__(self):
        super().__init__()

        self.btn_open = QPushButton("Open")
        self.lb_beadimage = QLabel()

        self.initUI()

    # 해당 탭의 Layout을 설정하는 함수입니다.
    def initUI(self):
        tapdatagrid = QGridLayout()
        tapdatagrid.addWidget(self.groupsetup(), 0, 0)
        tapdatagrid.addWidget(self.grouptestinput(), 1, 0)
        tapdatagrid.addWidget(self.groupcosmetic(), 0, 1)
        tapdatagrid.addWidget(self.grouptestoutput(), 1, 1)
        tapdatagrid.addWidget(self.groupimage(),0,2,2,2)

        self.setLayout(tapdatagrid)

    # 첫번째 그룹은 시편의 정보를 입력하는 곳입니다.
    def groupsetup(self):
        group_setup = QGroupBox('Setup')  # groupbox 변수 정의
        flay_setup = QFormLayout()  # groupbox 형식 변수 정의
        group_setup.setLayout(flay_setup)  # groupbox 변수의 형식 입력

        use_combo = QComboBox()
        use_combo.addItems({"Plate", "Tube"})

        weldtype_combo = QComboBox()
        weldtype_combo.addItems({"BOP", "Butt", "Lap"})

        setup_name = flay_setup.addRow("Name: ", QLineEdit())
        setup_company = flay_setup.addRow("Company: ", QLineEdit())
        setup_use = flay_setup.addRow("Use: ", use_combo)
        setup_material = flay_setup.addRow("Material: ", QLineEdit())
        setup_weldtype = flay_setup.addRow("Weld Type: ", weldtype_combo)
        setup_thickness = flay_setup.addRow("Thickness(mm): ", QDoubleSpinBox())
        setup_backingth = flay_setup.addRow("Backing Thickness(mm): ", QDoubleSpinBox())
        return group_setup

    def grouptestinput(self):
        group_testinput = QGroupBox('Test Input')  # groupbox 변수 정의
        flay_testinput = QFormLayout()  # groupbox 형식 변수 정의
        group_testinput.setLayout(flay_testinput)  # groupbox 변수의 형식 입력


        # 콤보박스 아이템 변수화
        sc_combo = QComboBox()
        sc_combo.addItems({"o", "|", "-", "∩", "∪", "oval"})
        sc_hlay = QHBoxLayout()
        input_sclength1 = sc_hlay.addWidget(QDoubleSpinBox())
        input_sclength2 = sc_hlay.addWidget(QDoubleSpinBox())

        input_fobs = flay_testinput.addRow("Fobs(mA): ", QDoubleSpinBox())
        input_wd = flay_testinput.addRow("WD(mm): ", QDoubleSpinBox())
        input_bw = flay_testinput.addRow("Bw(mA): ", QDoubleSpinBox())
        input_fw = flay_testinput.addRow("Fw(mA): ", QDoubleSpinBox())
        input_velocity = flay_testinput.addRow("Velocity(mm/min): ", QDoubleSpinBox())
        flay_testinput.addRow("S.C(mA): ", sc_combo)
        flay_testinput.addRow(sc_hlay)
        return group_testinput

    def groupcosmetic(self):
        group_cosmetic = QGroupBox('Cosmetic Input')  # groupbox 변수 정의
        flay_cosmetic = QFormLayout()  # groupbox 형식 변수 정의
        group_cosmetic.setLayout(flay_cosmetic)  # groupbox 변수의 형식 입력


        # 콤보박스 아이템 변수화
        sc_combo = QComboBox()
        sc_combo.addItems({"o", "|", "-", "∩", "∪", "oval"})
        sc_hlay = QHBoxLayout()
        cosmetic_sclength1 = sc_hlay.addWidget(QDoubleSpinBox())
        cosmetic_sclength2 = sc_hlay.addWidget(QDoubleSpinBox())

        cosmetic_fobs = flay_cosmetic.addRow("Fobs(mA): ", QDoubleSpinBox())
        cosmetic_wd = flay_cosmetic.addRow("WD(mm): ", QDoubleSpinBox())
        cosmetic_bw = flay_cosmetic.addRow("Bw(mA): ", QDoubleSpinBox())
        cosmetic_fw = flay_cosmetic.addRow("Fw(mA): ", QDoubleSpinBox())
        cosmetic_velocity = flay_cosmetic.addRow("Velocity(mm/min): ", QDoubleSpinBox())
        flay_cosmetic.addRow("S.C(mA): ", sc_combo)
        flay_cosmetic.addRow(sc_hlay)
        return group_cosmetic

    def grouptestoutput(self):
        group_testoutput = QGroupBox("Output")
        flay_testoutput = QFormLayout()
        group_testoutput.setLayout(flay_testoutput)

        out_bw = flay_testoutput.addRow("Bead Width(mm): ", QDoubleSpinBox())
        out_bh = flay_testoutput.addRow("Bead Height(mm): ", QDoubleSpinBox())
        out_backw = flay_testoutput.addRow("Back Width(mm): ", QDoubleSpinBox())
        out_backh = flay_testoutput.addRow("Back Height(mm): ", QDoubleSpinBox())
        out_50w = flay_testoutput.addRow("50% Width(mm): ", QDoubleSpinBox())
        out_50w = flay_testoutput.addRow("50% Height(mm): ", QDoubleSpinBox())
        out_crack = flay_testoutput.addRow("Crack(mm): ", QDoubleSpinBox())
        out_porosity = flay_testoutput.addRow("Porosity(mm): ", QDoubleSpinBox())
        return group_testoutput

    def groupimage(self):
        group_image = QGroupBox("Image")
        flay_image = QFormLayout()
        group_image.setLayout(flay_image)

        flay_image.addWidget(self.btn_open)
        image_bead = flay_image.addWidget(self.lb_beadimage)

        self.btn_open.clicked.connect(self.openimage_clicked)

        return group_image

    def openimage_clicked(self):
        fname = QFileDialog.getOpenFileName(self, 'Open File')
        pixmap = QPixmap(fname[0])

        self.lb_beadimage.setPixmap(pixmap)


class Tabcompare(QWidget):
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
    w = Window()
    sys.exit(app.exec_())
