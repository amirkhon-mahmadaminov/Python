import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QFormLayout, QLabel, QPushButton, QWidget, \
    QListWidget, QMessageBox, QSpinBox, QHBoxLayout
from PyQt5.QtCore import QTimer, Qt


# Database setup

def setup_database():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users
                      (id INTEGER PRIMARY KEY, timer INTEGER, price INTEGER, total_time INTEGER)''')

    try:
        cursor.execute("ALTER TABLE users ADD COLUMN total_time INTEGER")
    except sqlite3.OperationalError as e:
        if "duplicate column" in str(e):  # The column already exists
            pass
        else:
            raise  # Raise the error if it's a different error

    conn.commit()
    return conn





class MainWindow(QMainWindow):
    def __init__(self, conn):
        super().__init__()
        self.conn = conn
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Computer Club Application')

        main_layout = QVBoxLayout()

        layout = QHBoxLayout()

        form_layout = QVBoxLayout()

        input_layout = QFormLayout()
        self.timer_input = QSpinBox()
        self.timer_input.setRange(1, 1000)
        input_layout.addRow("Время", self.timer_input)

        self.price_input = QSpinBox()
        self.price_input.setRange(1, 1000)
        input_layout.addRow("Цена за минуту", self.price_input)

        self.timer_input.valueChanged.connect(self.update_total)
        self.price_input.valueChanged.connect(self.update_total)

        self.total_label = QLabel("Общая сумма: 0")
        input_layout.addRow(self.total_label)

        form_layout.addLayout(input_layout)


        save_button = QPushButton("Сохранить")
        save_button.clicked.connect(self.save)
        form_layout.addWidget(save_button)

        delete_button = QPushButton("Удалить")
        delete_button.clicked.connect(self.delete_user)
        form_layout.addWidget(delete_button)

        layout.addLayout(form_layout)

        self.user_list = QListWidget()
        layout.addWidget(self.user_list)
        main_layout.addLayout(layout)

        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

        self.update_user_list()
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_time_remaining)
        self.timer.start(60000)  # Update every second

    def save(self):
        timer = self.timer_input.value()
        price = self.price_input.value()
        total_time = timer

        with self.conn:
            try:
                self.conn.execute("INSERT INTO users (timer, price, total_time) VALUES (?, ?, ?)",
                                  (timer, price, total_time))
                self.conn.commit()
                QMessageBox.information(self, "Пользователь добавлен", "Пользователь успешно добавлен.")
                self.update_user_list()
            except sqlite3.Error as e:
                QMessageBox.warning(self, "Ошибка добавления пользователя", f"Пользователь не добавлен: {str(e)}")

    def update_total(self):
        total = self.timer_input.value() * self.price_input.value()
        self.total_label.setText(f"Общая сумма: {total}")

    def delete_user(self):
        current_row = self.user_list.currentRow()
        if current_row == -1:
            QMessageBox.warning(self, "Ошибка удаления пользователя", "Пожалуйста, выберите пользователя для удаления.")
            return

        user_id = int(self.user_list.item(current_row).text().split()[2][:-1])
        with self.conn:
            try:
                self.conn.execute("DELETE FROM users WHERE id = ?", (user_id,))
                self.conn.commit()
                QMessageBox.information(self, "Пользователь удален", "Пользователь успешно удален.")
                self.update_user_list()
            except sqlite3.Error as e:
                QMessageBox.warning(self, "Ошибка удаления пользователя", f"Пользователь не удален: {str(e)}")

    def update_user_list(self):
        self.user_list.clear()
        cursor = self.conn.cursor()

        for row in cursor.execute("SELECT id, timer, price, total_time FROM users"):
            self.user_list.addItem(
                f"User ID: {row[0]}, Время: {row[1]} минут, Цена за минуту: {row[2]} so'm, Общее время: {row[3]} минут, Осталось времени: {row[1]} минут")

    def update_time_remaining(self):
        cursor = self.conn.cursor()

        for idx, item in enumerate(self.user_list.findItems('*', Qt.MatchWildcard)):
            row = cursor.execute("SELECT id, timer, price FROM users WHERE id = ?", (idx + 1,)).fetchone()
            if row[1] > 0:
                row = (row[0], row[1] - 1, row[2])
                self.conn.execute("UPDATE users SET timer = ? WHERE id = ?", (row[1], row[0]))
                self.conn.commit()
                item.setText(
                    f"User ID: {row[0]}, Время: {row[1]} минут, Цена за минуту: {row[2]} so'm, Осталось времени: {row[1]} минут")


app = QApplication(sys.argv)
conn = setup_database()
main_window = MainWindow(conn)
main_window.show()
sys.exit(app.exec_())
