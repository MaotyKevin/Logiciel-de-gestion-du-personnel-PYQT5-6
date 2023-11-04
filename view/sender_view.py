import sys
import pika
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextEdit, QPushButton, QLineEdit
from PyQt5.QtCore import QCoreApplication

class MessageSender(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.setupRabbitMQ()

    def initUI(self):
        self.setWindowTitle('Message Sender')
        self.setGeometry(100, 100, 400, 300)

        self.message_input = QLineEdit(self)
        self.send_button = QPushButton('Send', self)

        layout = QVBoxLayout()
        layout.addWidget(self.message_input)
        layout.addWidget(self.send_button)
        self.setLayout(layout)

        self.send_button.clicked.connect(self.sendMessage)

    def setupRabbitMQ(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host='127.0.0.1'))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue='hello')

    def sendMessage(self):
        message = self.message_input.text()
        if message:
            self.channel.basic_publish(exchange='', routing_key='hello', body=message)
            print(f"Sent: {message}")  # For debugging
            self.message_input.clear()

    def closeEvent(self, event):
        self.connection.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    sender = MessageSender()
    sender.show()
    sys.exit(app.exec_())
