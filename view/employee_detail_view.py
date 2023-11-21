import sys , os
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from PyQt5.QtWidgets import QPushButton,QApplication,QWidget, QLabel, QVBoxLayout , QTabWidget , QScrollArea , QHBoxLayout , QFileDialog , QMessageBox
from PyQt5.QtGui import QDesktopServices
from PyQt5.QtCore import Qt , QUrl
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from controller.personnel_card_controller import PersonnelController
from view.employeeDetailTabOne_view import EmployeeDetailsTabOne , EmployeeDetailsTabOneContent


class EmployeeTabForm(QTabWidget):
    def __init__(self , badge):
        super().__init__()
        
        self.badge = badge
        self.tab1 = EmployeeDetailsTabOne(self.badge)
        self.tab2 = QWidget()

        self.addTab(self.tab1 , "Fiche Individuelle")
        self.addTab(self.tab2 , "Fiche Complete")

        self.setStyleSheet(
            "QTabBar::tab {"
            "    font-weight: bold;"
            "    width: 150px;"
            "}"
            "QTabBar::tab:!selected {"
            "    background-color: #7ed957;"
            "    color: #102429;   "
            "}"
        )
        

class EmployeeDetailsForm(QWidget):
    def __init__(self, badge , main_window):
        super().__init__()
        self.badge = badge
        self.main_window = main_window
        self.employeeTabForm = EmployeeTabForm(self.badge)
        self.controller = self.employeeTabForm.tab1.controller

        self.initUI()

    def initUI(self):

        scroll_area = QScrollArea()
        scroll_area.setWidget(self.employeeTabForm)  # Set the QTabWidget as the widget within the scroll area
        scroll_area.setWidgetResizable(True) 
        scroll_area.setStyleSheet(
            """
            QScrollArea {
                border: 1px solid #CCCCCC;
            }
            
            QScrollBar:vertical {
                border: 1px solid #734001;
                background: #102429;
                width: 12px;
                margin: 0px;
            }
            
            QScrollBar:horizontal {
                border: 1px solid #734001;
                background: #102429;
                height: 12px;
                margin: 0px;
            }
            
            QScrollBar::handle:vertical {
                background: #102429;
                min-height: 20px;
                border-radius: 6px;
            }
            
            QScrollBar::handle:horizontal {
                background: #102429;
                min-width: 20px;
                border-radius: 6px;
            }
            
            QScrollBar::add-line, QScrollBar::sub-line {
                background: none;
            }
            """
        )

        top_right_layout = QHBoxLayout()  # Create a layout for the top right corner
        top_right_layout.addStretch(1)

        container = QWidget()
        container_layout = QVBoxLayout()

        export_pdf_button = QPushButton("Export PDF")
        export_pdf_button.setCursor(Qt.PointingHandCursor)
        export_pdf_button.setStyleSheet("background-color: #7ed957; color: #102429; padding: 10px 20px; border: none; border-radius: 5px; font-weight:bold;")
        export_pdf_button.clicked.connect(self.export_pdf)


        previous_button = QPushButton("Retour a la liste")
        previous_button.setCursor(Qt.PointingHandCursor)
        previous_button.setStyleSheet("background-color: #102429; color: white; padding: 10px 20px; border: none; border-radius: 5px;font-weight:bold;")
        previous_button.clicked.connect(self.show_previous_cards)

        top_right_layout.addWidget(export_pdf_button)
        top_right_layout.addWidget(previous_button)
        
        container_layout.addLayout(top_right_layout)
        container_layout.addWidget(scroll_area)

        
        
        # Add the "Previous" button to the container

        

        container.setLayout(container_layout)

        layout = QVBoxLayout()
        layout.addWidget(container)  # Add the container widget to the layout
        self.setLayout(layout)

    def show_previous_cards(self):
        # Use the reference to the main window to switch back to the list of cards
        if self.main_window:
            self.main_window.return_to_last_displayed_page(self)
        else:
            self.main_window.setupUI()
            self.main_window.setCentralWidget(self.main_window.container)

    def export_pdf(self):
        # Get the content of EmployeeDetailsTabOne
        employee_data = self.controller.get_employee_details(self.badge)
        tab_one_content = EmployeeDetailsTabOneContent(employee_data)

        file_path, _ = QFileDialog.getSaveFileName(self, "Save PDF", f"{self.badge}.pdf", "PDF files (*.pdf)")

        if file_path:
            

            # Generate the PDF
            with open(file_path, 'wb') as pdf_file:
                pdf = canvas.Canvas(pdf_file, pagesize=letter)
                tab_one_content.draw_pdf(pdf)
                pdf.save()
                pdf

            QMessageBox.information(self, "Export Successful", "PDF exported successfully!")

            self.show_pdf(file_path)

    def show_pdf(self, file_path):
        # Open the PDF file with the default PDF viewer
        QDesktopServices.openUrl(QUrl.fromLocalFile(file_path))

