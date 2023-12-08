import sys , os
from PyQt5.QtWidgets import QApplication,QStackedWidget, QDialog, QVBoxLayout, QWidget, QLabel, QLineEdit, QPushButton, QComboBox, QFileDialog,QScrollArea , QDateEdit , QMessageBox , QSizePolicy , QHBoxLayout , QTableWidget , QTableWidgetItem , QSpacerItem , QHeaderView , QInputDialog
from PyQt5.QtGui import QImage, QPixmap, QFont, QPainter 
from PyQt5.QtCore import Qt , QDate, pyqtSignal , QRect , QSize 

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from controller.personnel_complete_controller import Complete_controller

class EmployeeCompleteTabTwo(QWidget):
    def __init__(self , badge):
        super().__init__()
        self.badge = badge
        self.controller = Complete_controller(db_path='data\my_database.sqlite')
        self.perso , self.equipe , self.categ , self.sc , self.affect , self.equipement , self.visite = self.controller.get_complete_info(self.badge)

        self.trio = (self.equipe , self.categ , self.sc)

        self.UI()

    def UI(self):
        persoHeader = (["Nom" , "Prenom" , "Sexe" , "CIN" , "Date CIN" , "Lieu CIN" , "Contact" , "Date de naissance" , "Lieu de naissance" , "Adresse"])

        EquipeCategorieSCHeader = (["Equipe" , "Categorie" , "Sous-categorie"])

        EquipementHeader = (["DateEquipement" , "Casque" , "Haut" , "Lunette" , "Chaussure"])

        VisiteHeader = (["DU" , "Visite medicale", "Accueil securite" , "MSB" , "Consignation" , "MS" , "VE_OMSI"])

        AffectationHeader = (["Fonction" , "2e fonction" , "Debut" , "Fin" , "Cause de depart"])

        self.persoTable = self.createTable(self.perso , persoHeader)

        self.EquipeCategorieSC = self.createTable(self.trio , EquipeCategorieSCHeader )

        self.equipementTable = self.createTable(self.equipement , EquipementHeader)

        self.visiteTable = self.createTable(self.visite , VisiteHeader)

        self.affectationTable = self.createTable(self.affect , AffectationHeader)

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.persoTable)
        main_layout.addWidget(self.EquipeCategorieSC)
        main_layout.addWidget(self.equipementTable)
        main_layout.addWidget(self.visiteTable)
        main_layout.addWidget(self.affectationTable)

        self.setLayout(main_layout)

        self.persoTable.setEditTriggers(QTableWidget.DoubleClicked | QTableWidget.EditKeyPressed)
        self.persoTable.cellDoubleClicked.connect(self.edit_cell_personnel)

        self.equipementTable.setEditTriggers(QTableWidget.DoubleClicked | QTableWidget.EditKeyPressed)
        self.equipementTable.cellDoubleClicked.connect(self.edit_cell_equipement)

        self.visiteTable.setEditTriggers(QTableWidget.DoubleClicked | QTableWidget.EditKeyPressed)
        self.visiteTable.cellDoubleClicked.connect(self.edit_cell_visite)

        self.affectationTable.setEditTriggers(QTableWidget.DoubleClicked | QTableWidget.EditKeyPressed)
        self.affectationTable.cellDoubleClicked.connect(self.edit_cell_affectation)

        self.EquipeCategorieSC.setEditTriggers(QTableWidget.DoubleClicked | QTableWidget.EditKeyPressed)
        self.EquipeCategorieSC.cellDoubleClicked.connect(self.edit_cell_equipe_categorie_sc)




    def createTable(self , tableData , headers):
        table_widget = QTableWidget(self)
        self.populateTable(table_widget, tableData , headers)
        return table_widget 

    def populateTable(self , table , tableData , headers):
        table.setRowCount(0)
        table.setColumnCount(len(tableData))
        table.setHorizontalHeaderLabels(headers)
        header_style = """
            QHeaderView::section {
                background-color: #102429;
                color: white;
                padding: 4px;
                border: 1px solid #7ed957;
                border-radius: 0px;
                font-weight:bold;
            }
        """
        table.horizontalHeader().setStyleSheet(header_style)

        table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        table.insertRow(0)
        for col_num, item in enumerate(tableData):
            if isinstance(item, tuple):
                for sub_col_num, sub_item in enumerate(item):
                    table.setItem(0, col_num + sub_col_num, QTableWidgetItem(str(sub_item)))
            else:
                table.setItem(0, col_num, QTableWidgetItem(str(item)))

    def edit_cell_personnel(self, row, col):
        if col < len(self.perso):
            current_item = self.persoTable.item(row, col)
            if current_item is not None and current_item.flags() & Qt.ItemIsEditable:
                new_value, ok = QInputDialog.getText(self, 'Fenetre de modification', f'Valeur actuelle :  {current_item.text()}')
                if ok:
                    current_item.setText(new_value)
                    self.register_update_personnel(row, col, new_value)

    def register_update_personnel(self, row, col, new_value):
        field_names = ["Nom", "Prenom", "Sexe", "CIN", "Date_CIN", "Lieu_CIN", "Contact",
                       "Date_Naissance", "Lieu_Naissance", "Adresse"]

        field_name = field_names[col]
        self.controller.update_personnelTable(self.badge, field_name, new_value)

#_____________________________________________

    def edit_cell_equipement(self, row, col):
        if col < len(self.equipement):
            current_item = self.equipementTable.item(row, col)
            if current_item is not None and current_item.flags() & Qt.ItemIsEditable:
                new_value, ok = QInputDialog.getText(self, 'Fenetre de modification', f'Valeur actuelle :  {current_item.text()}')
                if ok:
                    current_item.setText(new_value)
                    self.register_update_equipement(row, col, new_value)

    def register_update_equipement(self, row, col, new_value):
        field_names = ["DateEquipement", "Casque", "Haut", "Lunette", "Chaussure"]

        field_name = field_names[col]
        self.controller.update_EquipementTable(self.badge, field_name, new_value)

#_______________________________________________

    def edit_cell_visite(self, row, col):
        if col < len(self.visite):
            current_item = self.visiteTable.item(row, col)
            if current_item is not None and current_item.flags() & Qt.ItemIsEditable:
                new_value, ok = QInputDialog.getText(self, 'Fenetre de modification', f'Valeur actuelle :  {current_item.text()}')
                if ok:
                    current_item.setText(new_value)
                    self.register_update_visite(row, col, new_value)

    def register_update_visite(self, row, col, new_value):
        field_names = ["DU", "DateVisiteMedicale", "DateAccueilSecurite", "MSB", "Consignation" , "MS" , "VE_OMSI"]

        field_name = field_names[col]
        self.controller.update_visiteTable(self.badge, field_name, new_value)

#_________________________________________

    def edit_cell_affectation(self, row, col):
        if col < len(self.affect):
            current_item = self.affectationTable.item(row, col)
            if current_item is not None and current_item.flags() & Qt.ItemIsEditable:
                new_value, ok = QInputDialog.getText(self, 'Fenetre de modification', f'Valeur actuelle :  {current_item.text()}')
                if ok:
                    current_item.setText(new_value)
                    self.register_update_affectation(row, col, new_value)

    def register_update_affectation(self, row, col, new_value):
        field_names = ["Fonction", "DeuxiemeFonction", "DateDebut", "DateFin", "CauseDepart"]

        field_name = field_names[col]
        self.controller.update_affectationTable(self.badge, field_name, new_value)

#_________________________________________

    def edit_cell_equipe_categorie_sc(self, row, col):
        if col < len(self.trio):
            current_item = self.EquipeCategorieSC.item(row, col)
            if current_item is not None and current_item.flags() & Qt.ItemIsEditable:
                combo_box = QComboBox(self)
                combo_box.addItems(self.get_data_from_database(col))  # Update this line to fetch data from the database
                combo_box.setCurrentText(current_item.text())

                self.EquipeCategorieSC.setCellWidget(row, col, combo_box)

                # Connect the combo box's currentIndexChanged signal to a slot function
                combo_box.currentIndexChanged.connect(
                    lambda index, row=row, col=col, combo_box=combo_box: self.combo_box_changed(row, col, combo_box.currentText()))

    def get_data_from_database(self, col):
        # Implement a method to fetch data from the database based on the column (col)
        # Return a list of options for the QComboBox
        # Example:
        if col == 0:  # Equipe column
            return self.controller.recuperer_donnees_equipe()  # Replace with the actual method to fetch equipe names
        elif col == 1:  # Categorie column
            return self.controller.recuperer_donnees_categorie()  # Replace with the actual method to fetch categorie names
        elif col == 2:  # Sous-categorie column
            return self.controller.recuperer_donnees_SC()  # Replace with the actual method to fetch sous-categorie names
        else:
            return []
        
    def combo_box_changed(self, row, col, new_value):
        # Handle the combo box value change
        # Update the database, print a message, or perform any other desired actions
        self.EquipeCategorieSC.setItem(row, col, QTableWidgetItem(new_value))
        field_names = ["id_equipe", "id_categorie", "id_sousCategorie"]
        field_name = field_names[col]
        table_name = ["Personnel", "Affectation", "Affectation"][col]

        if col == 0 :
            new_valueID = self.controller.recuperer_id_equipe(new_value)
            self.controller.update_generic_table(table_name , field_name , new_valueID , badge=self.badge)

        elif col == 1 :
            new_valueID = self.controller.recuperer_id_categorie(new_value)
            self.controller.update_generic_table(table_name , field_name , new_valueID , badge=self.badge)

        elif col == 2:
            new_valueID = self.controller.recuperer_id_SC(new_value)
            self.controller.update_generic_table(table_name , field_name , new_valueID , badge=self.badge)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    badge = "5443"  # Replace with an actual badge value
    employee_complete_tab = EmployeeCompleteTabTwo(badge)
    employee_complete_tab.show()
    sys.exit(app.exec_())