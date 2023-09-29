# card_view.py

from PyQt5.QtWidgets import QWidget,QGraphicsDropShadowEffect, QVBoxLayout, QLabel
from PyQt5 import QtGui

class Card(QWidget):
    def __init__(self, badge, nom, categorie,fonction, sous_categorie):
        super().__init__()

        badge_label = QLabel(f"Badge: {badge}")
        nom_label = QLabel(f"Nom: {nom}")
        fonction_label = QLabel(f"Fonction: {fonction}")
        categorie_label = QLabel(f"Categorie: {categorie}")
        sous_categorie_label = QLabel(f"Sous-Categorie: {sous_categorie}")

        card_layout = QVBoxLayout()
        card_layout.addWidget(badge_label)
        card_layout.addWidget(nom_label)
        card_layout.addWidget(fonction_label)
        card_layout.addWidget(categorie_label)
        card_layout.addWidget(sous_categorie_label)

        self.setLayout(card_layout)


