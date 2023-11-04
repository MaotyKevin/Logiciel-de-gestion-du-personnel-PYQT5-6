import sys
import pika
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextEdit , QHBoxLayout , QLabel , QPushButton , QMessageBox
from PyQt5.QtCore import QTimer 
from PyQt5.QtGui import QIcon

class ClientHeader(QWidget):
    def __init__(self , main_window):
        super().__init__()
        self.setFixedHeight(80)
        self.header_label = QLabel("LOGO HERE")
        self.header_label.setStyleSheet("color: white; font-weight: bolder")

        self.main_window = main_window

        self.logout_button = QPushButton("  LOGOUT")
        self.logout_button.setIcon(QIcon("assets\pic\logout.png"))
        self.logout_button.setStyleSheet("background-color: white; color: black; padding: 10px 20px; border: none; border-radius: 5px;")
        self.logout_button.clicked.connect(self.logout)

        header_layout = QHBoxLayout()  # Horizontal layout for the header content
        header_layout.addWidget(self.header_label)
        header_layout.addStretch(1)  # Add a stretch to push the message button to the right
        header_layout.addWidget(self.logout_button)

        centre = QWidget()
        centre.setLayout(header_layout)
        centre.setStyleSheet("background-color: #734001; border-radius: 4px;")
        layout = QVBoxLayout()  # Vertical layout for top alignment
        layout.addWidget(centre)
        self.setLayout(layout)

    def logout(self):
        confirmation = QMessageBox.question(self, "Confirmation" , "Etes-vous sur de vouloir vous deconnecter ?",QMessageBox.Yes | QMessageBox.No)
        if confirmation == QMessageBox.Yes:
            self.main_window.show_login_view()

class MessageReceiver(QWidget):
    def __init__(self , main_window):
        super().__init__()
        self.main_window = main_window
        self.initUI()
        self.setupRabbitMQ()

    def initUI(self):
        self.setWindowTitle('Client')
        self.setGeometry(100, 100, 400, 300)

        self.cliHeader = ClientHeader(self.main_window)

        main_layout = QVBoxLayout()  
        
              

        self.message_display = QTextEdit(self)
        self.message_display.setReadOnly(True)

        layout = QVBoxLayout()
        layout.addWidget(self.message_display)
        

        main_layout.addWidget(self.cliHeader)
        main_layout.addLayout(layout)
        self.setLayout(main_layout)
        

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.checkForMessages)
        self.timer.start(1000)  # Adjust the interval as needed (in milliseconds)

    def setupRabbitMQ(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host='127.0.0.1'))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue='hello' , durable=False)
        self.channel.queue_purge(queue='hello')

    def checkForMessages(self):
        method_frame, header_frame, body = self.channel.basic_get(queue='hello')
        if method_frame:
            message = f"Received: {body.decode('utf-8')}"
            print(message)  # For debugging
            self.updateDisplay(message)

    def updateDisplay(self, message):
        current_text = self.message_display.toPlainText()
        self.message_display.setPlainText(current_text + message + '\n')

    def closeEvent(self, event):
        self.timer.stop()
        self.connection.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    receiver = MessageReceiver()
    receiver.show()
    sys.exit(app.exec_())
