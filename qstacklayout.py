import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import * 
from PyQt5.QtCore import QDate 

class Main(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QGrid")

        # create widgets
        self.cmbSelector = QComboBox()
        self.cmbSelector.addItems(["General", "Species", "Location", "Surveys"])
        self.cmbSelector.currentIndexChanged.connect(self.evt_cmbSelector_changed)

        self.wdgGeneral = QWidget()
        self.wdgSpecies = QWidget()
        self.wdgLocation = QWidget()
        self.wdgSurveys = QWidget()
       

        ## general widgets
        self.lblNestID = QLabel("34")
        self.dteFound = QDateTimeEdit(QDate(2016, 5, 13))
        self.dteLast = QDateTimeEdit(QDate(2020,4,14))
        self.chkActive = QCheckBox()

        ## species widgets
        self.cmbSpecies = QComboBox()
        self.cmbSpecies.addItem("Red-tailed Hawk", 800)
        self.cmbSpecies.addItem("Swainsons Hawk", 400)
        self.cmbSpecies.addItem("Other", 1600)

        self.ledSpecies = QLineEdit()
        self.spbBuffer = QSpinBox()
        self.spbBuffer.setValue(800)

        # location Widgets
        self.spbLatitude = QDoubleSpinBox()
        self.spbLongitute = QDoubleSpinBox()

        # survey widget
        self.lstSurveys = QListWidget()
        self.lstSurveys.addItem("03/24/2020 - MSM - INACTIVE")
        self.lstSurveys.addItem("03/30/2020 - MSM - INACTIVE")
        self.lstSurveys.addItem("04/07/2020 - MSM - INACTIVE")
        self.lstSurveys.addItem("04/14/2020 - MSM - ACTIVE!!")
        self.btnAddSurvey = QPushButton("Add Survey")

        # layouts
        self.setup_layouts()

       

    def setup_layouts(self):
        self.lyt_main = QHBoxLayout()
        self.lyt_left = QVBoxLayout()
        self.lyt_right = QStackedLayout()

        self.lyt_main.addLayout(self.lyt_left)
        self.lyt_main.addLayout(self.lyt_right)

        self.lyt_left.addWidget(self.cmbSelector)
        self.lyt_left.addStretch() 

        # add stacked widgets to  rightlayout
        self.lyt_right.addWidget(self.wdgGeneral)
        self.lyt_right.addWidget(self.wdgSpecies)
        self.lyt_right.addWidget(self.wdgLocation)
        self.lyt_right.addWidget(self.wdgSurveys)


        ### setup general widget
        self.lyt_general = QFormLayout()
        self.lyt_general.addRow("Nest ID:", self.lblNestID )
        self.lyt_general.addRow("Date FOund: ", self.dteFound)
        self.lyt_general.addRow("Date Last Surveyed: ", self.dteLast)
        self.lyt_general.addRow("Currently Active", self.chkActive)
        self.wdgGeneral.setLayout(self.lyt_general)

        # setup location widget
        self.lyt_location = QFormLayout()
        self.lyt_location.addRow("Latitute:", self.spbLatitude)
        self.lyt_location.addRow("Longitude:", self.spbLongitute)
        self.wdgLocation.setLayout(self.lyt_location)

        # setup species widget
        self.lyt_species = QFormLayout()
        self.lyt_species.addRow("Species: ", self.cmbSpecies) 
        self.lyt_species.addRow("Species: ", self.ledSpecies)
        self.lyt_species.addRow("Buffer: ", self.spbBuffer)
        self.spbBuffer.setSuffix(" m")
        self.wdgSpecies.setLayout(self.lyt_species)

        # setup surveys widget
        self.lyt_surveys = QVBoxLayout()
        self.lyt_surveys.addWidget(self.lstSurveys)
        self.lyt_surveys.addWidget(self.btnAddSurvey)
      
        self.wdgSurveys.setLayout(self.lyt_surveys)


        self.setLayout(self.lyt_main)


    def evt_cmbSelector_changed(self, idx):
        self.lyt_right.setCurrentIndex(idx)





if __name__ == "__main__":
    app =QApplication(sys.argv)
    main=Main()
    main.show()

    sys.exit(app.exec_())
