import sys , os
from PyQt5.QtWidgets import QApplication,QStackedWidget, QDialog, QVBoxLayout, QWidget, QLabel, QLineEdit, QPushButton, QComboBox, QFileDialog,QScrollArea , QDateEdit , QMessageBox , QSizePolicy , QHBoxLayout , QTableWidget , QTableWidgetItem , QSpacerItem
from PyQt5.QtGui import QImage, QPixmap, QFont, QPainter 
from PyQt5.QtCore import Qt , QDate, pyqtSignal , QRect , QSize 
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle

from controller.personnel_card_controller import PersonnelController

class EmployeeDetailsTabOne(QWidget):
    def __init__(self , badge):
        super().__init__()
        self.badge = badge
        self.controller = PersonnelController(db_path='data\my_database.sqlite')
        employee_data = self.controller.get_employee_details(self.badge)
        self.defUI(employee_data)

    def defUI(self , employee_data):
        mainLayout = QVBoxLayout()

        if employee_data:
            Fonction , Badge , Photo , Nom ,  Prenom , Date_Naissance , Lieu_Naissance , CIN  , Date_CIN , Lieu_CIN , Adresse , Contact , DateDebut , VE_OMSI , DateFin , CauseDepart , DateEquipement , Casque , Haut , Lunette , Chaussure  = employee_data



            self.FonctionLabel = QLineEdit(f"Fonction : {Fonction}")
            self.FonctionLabel.setReadOnly(True)
            self.styleLineEdit(self.FonctionLabel)

            self.BadgeLabel = QLineEdit(f"Badge : {Badge}")
            self.BadgeLabel.setReadOnly(True)
            self.styleLineEdit(self.BadgeLabel)

#__________________________________________________________

            self.NomLabel = QLineEdit(f"Nom : {Nom}")
            self.NomLabel.setReadOnly(True)
            self.styleLineEdit(self.NomLabel)

            self.prenomLabel = QLineEdit(f"Prenom : {Prenom}")
            self.prenomLabel.setReadOnly(True)
            self.styleLineEdit(self.prenomLabel)

            self.DateNaissanceLabel = QLineEdit(f"Date de naissance : {Date_Naissance}")
            self.DateNaissanceLabel.setReadOnly(True)
            self.styleLineEdit(self.DateNaissanceLabel)

            self.CINLabel = QLineEdit(f"CIN : {CIN}")
            self.CINLabel.setReadOnly(True)
            self.styleLineEdit(self.CINLabel)

#________________________________________________________

            self.LieuNaissanceLabel = QLineEdit(f"Lieu de naissance : {Lieu_Naissance}")
            self.LieuNaissanceLabel.setReadOnly(True)
            self.styleLineEdit(self.LieuNaissanceLabel)

            self.DateCINLabel = QLineEdit(f"Date CIN : {Date_CIN}")
            self.DateCINLabel.setReadOnly(True)
            self.styleLineEdit(self.DateCINLabel)

            self.LieuCINLabel = QLineEdit(f"Lieu CIN : {Lieu_CIN}")
            self.LieuCINLabel.setReadOnly(True)
            self.styleLineEdit(self.LieuCINLabel)

#__________________________________________________

            if Photo:
                pixmap = QPixmap()
                pixmap.loadFromData(Photo)
                if not pixmap.isNull():
                    self.photo_label = QLabel()
                    self.photo_label.setPixmap(pixmap)
                    self.photo_label.setPixmap(pixmap.scaled(QSize(300, 300), Qt.KeepAspectRatio))

#________________________________________________________ 

            self.AdresseLabel = QLineEdit(f"Adresse : {Adresse}")
            self.AdresseLabel.setReadOnly(True)
            self.styleLineEdit(self.AdresseLabel)

            self.ContactLabel = QLineEdit(f"Contact : {Contact}")
            self.ContactLabel.setReadOnly(True)
            self.styleLineEdit(self.ContactLabel)

#____________________________________________________________

            self.DateEntreeLabel = QLineEdit(f"Date de debut : {DateDebut}")
            self.DateEntreeLabel.setReadOnly(True)
            self.styleLineEdit(self.DateEntreeLabel)

            self.VE_OMSILabel = QLineEdit(f"VE-OMSI : {VE_OMSI}")
            self.VE_OMSILabel.setReadOnly(True)
            self.styleLineEdit(self.VE_OMSILabel)

            self.DateFinLabel = QLineEdit(f"Date de fin : {DateFin}")
            self.DateFinLabel.setReadOnly(True)
            self.styleLineEdit(self.DateFinLabel)

            self.CauseDepartLabel = QLineEdit(f"Cause de depart : {CauseDepart}")
            self.CauseDepartLabel.setReadOnly(True)
            self.styleLineEdit(self.CauseDepartLabel)

#_________________________________________________________


            self.tableWidget = QTableWidget(1, 5)  # Create a table with 1 row and 5 columns

            # Set column headers
            headers = ["Date", "Chaussure", "Haut", "Casque", "Lunette"]
            self.tableWidget.setHorizontalHeaderLabels(headers)

            # Fill the table with data
            data = [DateEquipement, Chaussure, Haut, Casque, Lunette]
            for col, value in enumerate(data):
                item = QTableWidgetItem(value)
                self.tableWidget.setItem(0, col, item)

#_________________________________________________________

            Fonction_desired_width = self.FonctionLabel.fontMetrics().width(self.FonctionLabel.text()) + 20
            self.FonctionLabel.setFixedWidth(Fonction_desired_width)

            Badge_desired_width = self.BadgeLabel.fontMetrics().width(self.BadgeLabel.text()) + 20
            self.BadgeLabel.setFixedWidth(Badge_desired_width)

            Nom_desired_width = self.NomLabel.fontMetrics().width(self.NomLabel.text()) + 20
            self.NomLabel.setFixedWidth(Nom_desired_width)

            Prenom_desired_width = self.prenomLabel.fontMetrics().width(self.prenomLabel.text()) + 20
            self.prenomLabel.setFixedWidth(Prenom_desired_width)

            Date_Naissance_desired_width = self.DateNaissanceLabel.fontMetrics().width(self.DateNaissanceLabel.text()) + 20
            self.DateNaissanceLabel.setFixedWidth(Date_Naissance_desired_width)

            Lieu_Naissance_desired_width = self.LieuNaissanceLabel.fontMetrics().width(self.LieuNaissanceLabel.text()) + 20
            self.LieuNaissanceLabel.setFixedWidth(Lieu_Naissance_desired_width)

            CIN_desired_width = self.CINLabel.fontMetrics().width(self.CINLabel.text()) + 20
            self.CINLabel.setFixedWidth(CIN_desired_width)

            Date_CIN_desired_width = self.DateCINLabel.fontMetrics().width(self.DateCINLabel.text()) + 20
            self.DateCINLabel.setFixedWidth(Date_CIN_desired_width)

            Lieu_CIN_desired_width = self.LieuCINLabel.fontMetrics().width(self.LieuCINLabel.text()) + 20
            self.LieuCINLabel.setFixedWidth(Lieu_CIN_desired_width)

            Adresse_desired_width = self.AdresseLabel.fontMetrics().width(self.AdresseLabel.text()) + 20
            self.AdresseLabel.setFixedWidth(Adresse_desired_width)

            Contact_desired_width = self.ContactLabel.fontMetrics().width(self.ContactLabel.text()) + 20
            self.ContactLabel.setFixedWidth(Contact_desired_width)

            DateDebut_desired_width = self.DateEntreeLabel.fontMetrics().width(self.DateEntreeLabel.text()) + 20
            self.DateEntreeLabel.setFixedWidth(DateDebut_desired_width)

            VE_OMSI_desired_width = self.VE_OMSILabel.fontMetrics().width(self.VE_OMSILabel.text()) + 20
            self.VE_OMSILabel.setFixedWidth(VE_OMSI_desired_width)

            DateFin_desired_width = self.DateFinLabel.fontMetrics().width(self.DateFinLabel.text()) + 20
            self.DateFinLabel.setFixedWidth(DateFin_desired_width)

            CauseDepart_desired_width = self.CauseDepartLabel.fontMetrics().width(self.CauseDepartLabel.text()) + 20
            self.CauseDepartLabel.setFixedWidth(CauseDepart_desired_width)

#__________________________________________________________

            logo = QLabel()
            pixmap = QPixmap('assets\pic\logo fiche.jpg')  # Replace with the path to your image
            logo.setPixmap(pixmap)

#___________________________________________________________

            vertical = QVBoxLayout()
            vertical.addWidget(logo)
            #vertical.setSpacing(5)
            vertical.setContentsMargins(0 , 0 , 0 , 0)
            vertical.addStretch(1)

            vertical1 = QVBoxLayout()
            vertical1.addWidget(self.FonctionLabel)
            vertical1.addWidget(self.BadgeLabel)
            vertical1.addWidget(self.photo_label)

            horizontal = QHBoxLayout()
            horizontal.addLayout(vertical)
            horizontal.addLayout(vertical1)

            vertical2 = QVBoxLayout()
            vertical2.addWidget(self.NomLabel)
            vertical2.addWidget(self.prenomLabel)
            vertical2.addWidget(self.DateNaissanceLabel)
            vertical2.addWidget(self.CINLabel)
            vertical2.addWidget(self.AdresseLabel)
            vertical2.addWidget(self.ContactLabel)

            vertical3 = QVBoxLayout()
            vertical3.addWidget(self.LieuNaissanceLabel)
            vertical3.addWidget(self.DateCINLabel)
            vertical3.addWidget(self.LieuCINLabel)

            horizontal1 = QHBoxLayout()
            horizontal1.addLayout(vertical2)
            horizontal1.addItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))
            horizontal1.addLayout(vertical3)
            horizontal1.addStretch(0)
            horizontal1.addSpacing(30)
       
            

            vertical4 = QVBoxLayout()
            vertical4.addWidget(self.DateEntreeLabel)
            vertical4.addWidget(self.VE_OMSILabel)
            vertical4.addWidget(self.DateFinLabel)
            vertical4.addWidget(self.CauseDepartLabel)

              
            mainLayout.addLayout(horizontal)
            mainLayout.addLayout(horizontal1)
            mainLayout.addLayout(vertical4)
            mainLayout.addWidget(self.tableWidget)
            mainLayout.setSpacing(10)
            mainLayout.addStretch(0)
            
             
        self.setLayout(mainLayout)
        

    def styleLineEdit(self, line_edit):
        # Define the CSS style for QLineEdit
        style = """
            QLineEdit {
                background-color: transparent;  /* Background color */
                color:#102429;
                border : none;
                border-bottom: 1px solid #102429;  /* Border color and thickness */
                border-radius: 5px;         /* Rounded corners */
                padding: 5px;               /* Padding inside the QLineEdit */
                
                
            }
        """
        line_edit.setStyleSheet(style)


class EmployeeDetailsTabOneContent:
    def __init__(self, employee_data):
        self.employee_data = employee_data

    def draw_pdf(self, pdf):
        if self.employee_data:
            Fonction , Badge , Photo , Nom ,  Prenom , Date_Naissance , Lieu_Naissance , CIN  , Date_CIN , Lieu_CIN , Adresse , Contact , DateDebut , VE_OMSI , DateFin , CauseDepart , DateEquipement , Casque , Haut , Lunette , Chaussure  = self.employee_data

            # Create a list to store data for the table
            table_data = [
                ["Date", "Chaussure", "Haut", "Casque", "Lunette"],
                [DateEquipement, Chaussure, Haut, Casque, Lunette]
            ]

            # Create a PDF document
            doc = SimpleDocTemplate(pdf, pagesize=letter)

            # Define style for the table
            style = TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                                ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                                ('GRID', (0, 0), (-1, -1), 1, colors.black)])

            # Create table and apply style
            table = Table(table_data)
            table.setStyle(style)

            # Add content to the PDF
            pdf_title = "Employee Details"
            pdf.drawString(100, 800, pdf_title)
            pdf.drawString(100, 780, f"Fonction: {Fonction}")
            pdf.drawString(100, 760, f"Badge: {Badge}")
            pdf.drawString(100, 740, f"Nom: {Nom}")
            pdf.drawString(100, 720, f"Prenom: {Prenom}")
            pdf.drawString(100, 700, f"Date de naissance: {Date_Naissance}")
            pdf.drawString(100, 680, f"CIN: {CIN}")
            pdf.drawString(100, 660, f"Lieu de naissance: {Lieu_Naissance}")
            pdf.drawString(100, 640, f"Date CIN: {Date_CIN}")
            pdf.drawString(100, 620, f"Lieu CIN: {Lieu_CIN}")
            pdf.drawString(100, 600, f"Adresse: {Adresse}")
            pdf.drawString(100, 580, f"Contact: {Contact}")
            pdf.drawString(100, 560, f"Date de debut: {DateDebut}")
            pdf.drawString(100, 540, f"VE-OMSI: {VE_OMSI}")
            pdf.drawString(100, 520, f"Date de fin: {DateFin}")
            pdf.drawString(100, 500, f"Cause de depart: {CauseDepart}")

            # Draw the table on the PDF
            table.wrapOn(pdf, 0, 0)
            table.drawOn(pdf, 100, 450)

            







