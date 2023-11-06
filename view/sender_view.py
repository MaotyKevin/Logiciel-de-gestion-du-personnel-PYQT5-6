import sys
import pika
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QListWidget, QPushButton, QLineEdit, QListWidgetItem, QSplitter
from PyQt5.QtCore import Qt


class MessageSender(QWidget):
    def __init__(self , db_path, logged_username , sampleUsers):
        super().__init__()
        self.db_path = db_path
        self.sampleUsers = sampleUsers
        self.logged_username = logged_username
        self.initUI(self.sampleUsers)
        self.setupRabbitMQ(self.sampleUsers)

    def initUI(self , sampleUsers):
        self.setWindowTitle('Messenger App')
        self.setGeometry(100, 100, 400, 500)

        splitter = QSplitter(Qt.Horizontal)

        self.user_list = QListWidget(self)
        self.message_lists = {username: QListWidget(self) for username in self.sampleUsers}
        self.message_input = QLineEdit(self)
        self.send_button = QPushButton('Send', self)

        splitter.addWidget(self.user_list)
        for message_list in self.message_lists.values():
            splitter.addWidget(message_list)

        layout = QVBoxLayout()
        layout.addWidget(splitter)
        layout.addWidget(self.message_input)
        layout.addWidget(self.send_button)
        self.setLayout(layout)

        self.user_list.addItems(sampleUsers)

        self.send_button.clicked.connect(self.sendMessage)

        self.user_list.itemClicked.connect(self.showChatZone)

        # Initially hide all chat zones except the first one (index 0)
        for index, message_list in enumerate(self.message_lists.values()):
            if index != 0:
                message_list.hide()

    def setupRabbitMQ(self, sampleUsers):
        self.rabbitmq_connections = {username: pika.BlockingConnection(pika.ConnectionParameters(host='127.0.0.1')) for username in sampleUsers}
        self.rabbitmq_channels = {username: connection.channel() for username, connection in self.rabbitmq_connections.items()}

        for username in sampleUsers:
            self.rabbitmq_channels[username].queue_declare(queue=f'{username}')

    def sendMessage(self):
        message = self.message_input.text()
        if message:
            # Get the currently selected username
            current_username = self.user_list.currentItem().text()
            message_list = self.message_lists[current_username]
            self.rabbitmq_channels[current_username].basic_publish(exchange='', routing_key=current_username, body=message)
            self.displayMessage(message_list, message, outgoing=True)  # Display sent message
            self.message_input.clear()

    def displayMessage(self, message_list, message, outgoing=False):
        item = QListWidgetItem(message_list)
        item.setText(message)
        if outgoing:
            item.setTextAlignment(Qt.AlignRight)
            item.setForeground(Qt.blue)  # Customize the color for outgoing messages
        else:
            item.setTextAlignment(Qt.AlignLeft)

    def showChatZone(self, item):
        current_username = item.text()
        for username, message_list in self.message_lists.items():
            if username == current_username:
                message_list.show()
            else:
                message_list.hide()

    def closeEvent(self, event):
        for connection in self.rabbitmq_connections.values():
            connection.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    db_path = 'data/my_database.sqlite'
    logged = 'Kevin'
    sender = MessageSender(db_path , logged)
    sender.show()
    sys.exit(app.exec_())
