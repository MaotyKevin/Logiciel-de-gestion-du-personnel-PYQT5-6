import sys 
from PyQt5.QtWidgets import QApplication
from view.principale_view import MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    db_path = 'data/my_database.sqlite'
    window = MainWindow(db_path)
    window.showMaximized()
    sys.exit(app.exec_())
