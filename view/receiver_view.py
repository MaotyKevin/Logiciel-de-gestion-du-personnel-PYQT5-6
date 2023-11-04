import sys
import pika
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextEdit
from PyQt5.QtCore import QTimer

class MessageReceiver(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.setupRabbitMQ()

    def initUI(self):
        self.setWindowTitle('Message Receiver')
        self.setGeometry(100, 100, 400, 300)

        self.message_display = QTextEdit(self)
        self.message_display.setReadOnly(True)

        layout = QVBoxLayout()
        layout.addWidget(self.message_display)
        self.setLayout(layout)

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
