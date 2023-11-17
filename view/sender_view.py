import sys
import pika
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QListWidget, QPushButton, QLineEdit, QListWidgetItem, QSplitter
from PyQt5.QtCore import Qt

class MessageSender(QWidget):
    def __init__(self, db_path, logged_username, sampleUsers):
        super().__init__()
        self.db_path = db_path
        self.sampleUsers = sampleUsers
        self.logged_username = logged_username
        self.initUI([data[1] for data in sampleUsers])
        self.setupRabbitMQ([data[0] for data in sampleUsers])

    def initUI(self, sampleUserName ):
        self.setWindowTitle('Messenger App')
        self.setGeometry(100, 100, 400, 500)

        splitter = QSplitter(Qt.Horizontal)
      

        self.user_list = QListWidget(self)
        self.message_lists = {user[0]: QListWidget(self) for user in self.sampleUsers}
        
        self.message_input = QLineEdit(self)
        self.message_input.setStyleSheet("""
            QLineEdit {
                border: 2px solid #734001; /* Blue border */
                border-radius: 10px; /* Rounded corners */
                padding: 8px; /* Add padding */
                background-color: #FFFFFF; /* White background */
            }
        """)

        self.send_button = QPushButton('Send', self)

        splitter.addWidget(self.user_list)
        for message_list in self.message_lists.values():
            splitter.addWidget(message_list)
            message_list.setStyleSheet("margin: 5px; padding: 5px; font-weight:bolder;")

        layout = QVBoxLayout()
        layout.addWidget(splitter)
        layout.addWidget(self.message_input)
        layout.addWidget(self.send_button)
        self.setLayout(layout)

        self.user_list.addItems(sampleUserName)

        self.send_button.clicked.connect(self.sendMessage)

        self.user_list.itemClicked.connect(self.showChatZone)

        # Initially hide all chat zones except the first one (index 0)
        for index, message_list in enumerate(self.message_lists.values()):
            if index != 0:
                message_list.hide()

        self.user_list.setStyleSheet(
                                  "QListWidget QScrollBar"
                                  "{"
                                  "background : #734001;"
                                  "}"
                                  "QListView::item"
                                  "{"
                                  "font-weight: bolder;"
                                  "padding:5px;"
                                  "}"
                                  "QListView::item:selected"
                                  "{"
                                  "border : 1px solid white;"
                                  "background : #734001;"
                                  "}"
                                  )
        


    def setupRabbitMQ(self, sampleUsersList):

        # Use user IDs as queue identifiers
        self.rabbitmq_connections = {user: pika.BlockingConnection(pika.ConnectionParameters(host='localhost')) for user in sampleUsersList}
        self.rabbitmq_channels = {user: connection.channel() for user, connection in self.rabbitmq_connections.items()}

        for user in sampleUsersList:
            self.rabbitmq_channels[user].queue_declare(queue=f'{user}')  # Use user IDs as queue names

    def sendMessage(self ):
        message = self.message_input.text()
        if message:
            # Get the currently selected username
            current_user = self.sampleUsers[self.user_list.currentRow()]
            current_user_id, current_username = current_user[0], current_user[1]
            message_list = self.message_lists[current_user_id]  # Use the user ID


            sent_message = f"ADMIN : {message}\n"
            print(f"Send -> {sent_message}")

            self.rabbitmq_channels[current_user_id].basic_publish(exchange='', routing_key=str(current_user_id), body=sent_message)  # Use user ID as routing key

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
        for user_id, message_list in self.message_lists.items():
            if user_id == self.sampleUsers[self.user_list.currentRow()][0]:
                message_list.show()
            else:
                message_list.hide()

    def closeEvent(self, event):
        for connection in self.rabbitmq_connections.values():
            connection.close()

    def updateData(self , userMajList):
        # Update other data as needed
        self.sampleUsers = userMajList
        # Update the user list widget to reflect the changes
        self.user_list.clear()
        self.user_list.addItems([data[1] for data in self.sampleUsers])

if __name__ == '__main__':
    app = QApplication(sys.argv)
    db_path = 'data/my_database.sqlite'
    logged = 'Kevin'
    # Sample users list as (ID, Username) tuples
    sample_users = [(1, 'User1'), (2, 'User2'), (3, 'User3')]  # Replace with your actual sample users
    sender = MessageSender(db_path, logged, sample_users)
    sender.show()
    sys.exit(app.exec_())
