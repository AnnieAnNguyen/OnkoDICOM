import platform
from os.path import expanduser

from PySide6 import QtWidgets
from src.Controller.PathHandler import resource_path


class AnonymisationOptions(QtWidgets.QWidget):
    """
    Anonymisation Options for batch processing.
    """

    def __init__(self):
        """
        Initialise the class
        """
        QtWidgets.QWidget.__init__(self)

        # Create the main layout
        self.main_layout = QtWidgets.QVBoxLayout()

        self.display_section = QtWidgets.QGroupBox("Display Anonymous Options")
        self.display_layout = QtWidgets.QHBoxLayout()

        self.gender_checkbox = QtWidgets.QCheckBox("Gender")
        self.dob_checkbox = QtWidgets.QCheckBox("Date of Birth")

        self.display_layout.addWidget(self.gender_checkbox)
        self.display_layout.addWidget(self.dob_checkbox)

        self.display_section.setLayout(self.display_layout)

        self.save_section = QtWidgets.QGroupBox("Save Anonymous Options")
        self.save_layout = QtWidgets.QHBoxLayout()

        self.name_checkbox = QtWidgets.QCheckBox("Name")
        self.name_checkbox.setChecked(True)
        self.name_checkbox.setDisabled(True)
        self.id_checkbox = QtWidgets.QCheckBox("ID")
        self.id_checkbox.setChecked(True)
        self.id_checkbox.setDisabled(True)
        self.cancer_checkbox = QtWidgets.QCheckBox("Type of Cancer")
        self.date_checkbox = QtWidgets.QCheckBox("Saved Date")


        self.save_layout.addWidget(self.name_checkbox)
        self.save_layout.addWidget(self.id_checkbox)
        self.save_layout.addWidget(self.cancer_checkbox)
        self.save_layout.addWidget(self.date_checkbox)

        self.save_section.setLayout(self.save_layout)

        self.main_layout.addWidget(self.display_section)
        self.main_layout.addWidget(self.save_section)

        self.setLayout(self.main_layout)
