import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTabWidget, QWidget, QVBoxLayout, QLabel

class Admin_crud(QTabWidget):
    def __init__(self):
        super().__init__()

        # Create tabs
        tab1 = QWidget()
        tab2 = QWidget()
        

        # Add tabs to the tab widget
        self.addTab(tab1, "Tab 1")
        self.addTab(tab2, "Tab 2")
        

        # Customize the contents of each tab
        self.setupTab1(tab1)
        self.setupTab2(tab2)
        

    def setupTab1(self, tab):
        layout = QVBoxLayout()
        label = QLabel("This is the content of Tab 1.")
        layout.addWidget(label)
        tab.setLayout(layout)

    def setupTab2(self, tab):
        layout = QVBoxLayout()
        label = QLabel("This is the content of Tab 2.")
        layout.addWidget(label)
        tab.setLayout(layout)


