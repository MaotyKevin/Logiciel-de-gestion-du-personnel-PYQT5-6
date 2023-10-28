import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton

class Header(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Create widgets for your header
        header_label = QLabel("Your Application Name")

        # Create a layout for the header
        header_layout = QHBoxLayout()
        header_layout.addWidget(header_label)

        self.setLayout(header_layout)

class SideNavBar(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Create widgets for your side navigation bar
        button1 = QPushButton("Menu Item 1")
        button2 = QPushButton("Menu Item 2")
        button3 = QPushButton("Menu Item 3")

        # Create a layout for the side navigation bar
        side_layout = QVBoxLayout()
        side_layout.addWidget(button1)
        side_layout.addWidget(button2)
        side_layout.addWidget(button3)

        self.setLayout(side_layout)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create instances of your header, side navigation bar
        header = Header()
        side_nav_bar = SideNavBar()

        # Create a central widget to hold the layouts
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Create a layout for the central widget
        central_layout = QHBoxLayout(central_widget)
        central_layout.addWidget(side_nav_bar)
        central_layout.addWidget(header)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
