import sys
import pymysql
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QLineEdit, QPushButton, QTableWidgetItem, \
    QTableWidget, QMessageBox, QInputDialog, QDialog, QTextEdit
from PyQt5.QtGui import QFont
import logging


class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Логін")

        self.label_username = QLabel("Нікнейм:", self)
        self.label_username.setGeometry(50, 50, 70, 20)
        self.label_username.setFont(QFont("Arial", 12))

        self.input_username = QLineEdit(self)
        self.input_username.setGeometry(130, 50, 100, 20)

        self.label_password = QLabel("Пароль:", self)
        self.label_password.setGeometry(50, 80, 70, 20)
        self.label_password.setFont(QFont("Arial", 12))

        self.input_password = QLineEdit(self)
        self.input_password.setGeometry(130, 80, 100, 20)
        self.input_password.setEchoMode(QLineEdit.Password)

        self.button_login = QPushButton("Вхід", self)
        self.button_login.setGeometry(120, 120, 60, 30)
        self.button_login.clicked.connect(self.login)

        self.label_register_fullname = QLabel("Імʼя:", self)
        self.label_register_fullname.setGeometry(30, 150, 100, 20)
        self.label_register_fullname.setFont(QFont("Arial", 12))

        self.input_register_fullname = QLineEdit(self)
        self.input_register_fullname.setGeometry(150, 150, 100, 20)

        self.label_register_address = QLabel("Адреса:", self)
        self.label_register_address.setGeometry(30, 180, 100, 20)
        self.label_register_address.setFont(QFont("Arial", 12))

        self.input_register_address = QLineEdit(self)
        self.input_register_address.setGeometry(150, 180, 100, 20)

        self.label_register_phone = QLabel("Телефон:", self)
        self.label_register_phone.setGeometry(30, 210, 100, 20)
        self.label_register_phone.setFont(QFont("Arial", 12))

        self.input_register_phone = QLineEdit(self)
        self.input_register_phone.setGeometry(150, 210, 100, 20)

        self.label_register_username = QLabel("Новий Нікнейм:", self)
        self.label_register_username.setGeometry(30, 240, 100, 20)
        self.label_register_username.setFont(QFont("Arial", 12))

        self.input_register_username = QLineEdit(self)
        self.input_register_username.setGeometry(150, 240, 100, 20)

        self.label_register_password = QLabel("Пароль:", self)
        self.label_register_password.setGeometry(30, 270, 100, 20)
        self.label_register_password.setFont(QFont("Arial", 12))

        self.input_register_password = QLineEdit(self)
        self.input_register_password.setGeometry(150, 270, 100, 20)
        self.input_register_password.setEchoMode(QLineEdit.Password)

        self.button_register = QPushButton("Зараєструватись", self)
        self.button_register.setGeometry(90, 300, 140, 30)
        self.button_register.clicked.connect(self.register)

        self.setFixedSize(300, 400)

    def login(self):
        username = self.input_username.text()
        password = self.input_password.text()

        db = pymysql.connect(
            host="localhost",
            user="root",
            password="Kp549259#",
            database="AvariinaSlujba")
        cursor = db.cursor()

        query = f"SELECT * FROM Client WHERE login='{username}' AND password_='{password}'"
        cursor.execute(query)
        result = cursor.fetchone()
        if result:
            client_id = result[0]
            self.open_client_main_window(client_id)
            self.close()
            return

        query = f"SELECT * FROM Manager WHERE login='{username}' AND password_='{password}'"
        cursor.execute(query)
        result = cursor.fetchone()
        if result:
            manager_id = result[0]
            self.open_manager_main_window(manager_id)
            self.close()
            return

        query = f"SELECT * FROM Brigade WHERE login='{username}' AND password_='{password}'"
        cursor.execute(query)
        result = cursor.fetchone()
        if result:
            brigade_id = result[0]
            self.open_brigade_main_window(brigade_id)
            self.close()
            return

        error_message = QLabel("Неправильне імʼя або пароль", self)
        error_message.setGeometry(70, 330, 200, 20)
        error_message.setFont(QFont("Arial", 12))
        error_message.setStyleSheet("color: red")
        error_message.show()

    def open_client_main_window(self, client_id):
        self.client_main_window = ClientMainWindow(client_id)
        self.client_main_window.show()

    def open_manager_main_window(self, manager_id):
        self.manager_main_window = ManagerMainWindow(manager_id)
        self.manager_main_window.show()

    def open_brigade_main_window(self, brigade_id):
        self.brigade_main_window = BrigadeMainWindow(brigade_id)
        self.brigade_main_window.show()

    def register(self):
        fullname = self.input_register_fullname.text()
        address = self.input_register_address.text()
        phone = self.input_register_phone.text()
        username = self.input_register_username.text()
        password = self.input_register_password.text()

        db = pymysql.connect(
            host="localhost",
            user="root",
            password="Kp549259#",
            database="AvariinaSlujba")
        cursor = db.cursor()

        query = "SELECT MAX(id) FROM Client"
        cursor.execute(query)
        result = cursor.fetchone()
        if result[0]:
            client_id = result[0] + 1
        else:
            client_id = 1

        query = f"INSERT INTO Client (id, Full_Name, Address, Phone_Number, login, password_) VALUES ({client_id}, '{fullname}', '{address}', '{phone}', '{username}', '{password}')"
        cursor.execute(query)
        db.commit()

        success_message = QLabel("Реєстрація успішна!", self)
        success_message.setGeometry(70, 360, 200, 20)
        success_message.setFont(QFont("Arial", 12))
        success_message.setStyleSheet("color: green")
        success_message.show()


class BrigadeMainWindow(QWidget):
    def __init__(self, brigade_id):
        super().__init__()
        self.setWindowTitle("Вікно бригади")
        self.setGeometry(100, 100, 300, 200)

        self.label_brigade_id = QLabel(f"Brigade ID: {brigade_id}", self)
        self.label_brigade_id.setGeometry(50, 50, 200, 20)
        self.label_brigade_id.setFont(QFont("Arial", 12))

        self.button_table3 = QPushButton("Brigade Table", self)
        self.button_table3.setGeometry(100, 100, 110, 30)
        self.button_table3.clicked.connect(lambda: self.view_table("Brigade"))

        self.button_table4 = QPushButton("Request Table", self)
        self.button_table4.setGeometry(100, 150, 110, 30)
        self.button_table4.clicked.connect(lambda: self.view_table("Request"))

        self.button_table5 = QPushButton("Object Table", self)
        self.button_table5.setGeometry(100, 200, 110, 30)
        self.button_table5.clicked.connect(lambda: self.view_table("Object"))

        self.button_table7 = QPushButton("Job Table", self)
        self.button_table7.setGeometry(100, 250, 110, 30)
        self.button_table7.clicked.connect(lambda: self.view_table("Job"))

        self.button_table8 = QPushButton("Material Table", self)
        self.button_table8.setGeometry(100, 300, 110, 30)
        self.button_table8.clicked.connect(lambda: self.view_table("Material"))

        self.button_logout = QPushButton("Logout", self)
        self.button_logout.setGeometry(100, 350, 110, 30)
        self.button_logout.clicked.connect(self.logout)

        self.adjustSize()

    def view_table(self, table_name):
        db = pymysql.connect(
            host="localhost",
            user="root",
            password="Kp549259#",
            database="AvariinaSlujba"
        )
        cursor = db.cursor()

        cursor.execute(f"SHOW COLUMNS FROM {table_name}")
        columns = cursor.fetchall()
        column_names = [column[0] for column in columns]

        columns_to_hide = ["id", "login", "password_"]
        visible_columns = [column for column in column_names if column not in columns_to_hide]

        query = f"SELECT {', '.join(visible_columns)} FROM {table_name}"
        cursor.execute(query)
        result = cursor.fetchall()

        table_widget = QTableWidget(len(result), len(visible_columns), self)
        table_widget.setGeometry(250, 50, 500, 300)

        for i, row in enumerate(result):
            for j, value in enumerate(row):
                item = QTableWidgetItem(str(value))
                table_widget.setItem(i, j, item)

        table_widget.setHorizontalHeaderLabels(visible_columns)

        table_widget.show()
        table_widget.show()
        table_widget.show()
        cursor.close()
        db.close()

    def logout(self):
        self.close()
        login_window.show()


class ManagerMainWindow(QWidget):
    def __init__(self, manager_id):
        super().__init__()
        self.setWindowTitle("Вікно Керівника")
        self.setGeometry(100, 100, 300, 400)
        self.manager_id = manager_id

        self.label_manager_id = QLabel(f"Manager ID: {manager_id}", self)
        self.label_manager_id.setGeometry(50, 50, 200, 20)
        self.label_manager_id.setFont(QFont("Arial", 12))

        self.button_table1 = QPushButton("Manager Table", self)
        self.button_table1.setGeometry(100, 100, 110, 30)
        self.button_table1.clicked.connect(lambda: self.view_table("Manager"))

        self.button_table2 = QPushButton("Client Table", self)
        self.button_table2.setGeometry(100, 150, 110, 30)
        self.button_table2.clicked.connect(lambda: self.view_table("Client"))

        self.button_table3 = QPushButton("Brigade Table", self)
        self.button_table3.setGeometry(100, 200, 110, 30)
        self.button_table3.clicked.connect(lambda: self.view_table("Brigade"))

        self.button_table4 = QPushButton("Request Table", self)
        self.button_table4.setGeometry(100, 250, 110, 30)
        self.button_table4.clicked.connect(lambda: self.view_table("Request"))

        self.button_table5 = QPushButton("Object Table", self)
        self.button_table5.setGeometry(100, 300, 110, 30)
        self.button_table5.clicked.connect(lambda: self.view_table("Object"))

        self.button_table6 = QPushButton("Finance Table", self)
        self.button_table6.setGeometry(100, 350, 110, 30)
        self.button_table6.clicked.connect(lambda: self.view_table("Finance"))

        self.button_table7 = QPushButton("Job Table", self)
        self.button_table7.setGeometry(100, 400, 110, 30)
        self.button_table7.clicked.connect(lambda: self.view_table("Job"))

        self.button_table8 = QPushButton("Material Table", self)
        self.button_table8.setGeometry(100, 450, 110, 30)
        self.button_table8.clicked.connect(lambda: self.view_table("Material"))

        self.button_view_log = QPushButton("Переглянути журнал", self)
        self.button_view_log.setGeometry(70, 500, 170, 30)
        self.button_view_log.clicked.connect(self.view_log)
        self.button_view_log.setVisible(manager_id == 1)

        self.button_logout = QPushButton("Logout", self)
        self.button_logout.setGeometry(100, 550, 110, 30)
        self.button_logout.clicked.connect(self.logout)

        self.logger = logging.getLogger('manager_changes')
        self.logger.setLevel(logging.INFO)

        file_handler = logging.FileHandler('manager_changes.log')
        formatter = logging.Formatter('%(asctime)s - %(message)s')
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)

        self.adjustSize()

    def view_table(self, table_name):
        db = pymysql.connect(
            host="localhost",
            user="root",
            password="Kp549259#",
            database="AvariinaSlujba"
        )
        cursor = db.cursor()

        cursor.execute(f"SHOW COLUMNS FROM {table_name}")
        columns = cursor.fetchall()
        column_names = [column[0] for column in columns]

        columns_to_hide = ["login", "password_"]
        visible_columns = [column for column in column_names if column not in columns_to_hide]

        query = f"SELECT {', '.join(visible_columns)} FROM {table_name}"
        cursor.execute(query)
        result = cursor.fetchall()

        table_widget = QTableWidget(len(result), len(visible_columns), self)
        table_widget.setGeometry(250, 50, 500, 300)

        for i, row in enumerate(result):
            for j, value in enumerate(row):
                item = QTableWidgetItem(str(value))
                table_widget.setItem(i, j, item)

        table_widget.setHorizontalHeaderLabels(visible_columns)

        button_save = QPushButton("Зберегти", self)
        button_save.setGeometry(295, 370, 110, 30)
        button_save.clicked.connect(lambda: self.save_changes(table_widget, table_name, visible_columns))

        table_widget.show()
        button_save.show()

        button_delete = QPushButton("Видалити рядок", self)
        button_delete.setGeometry(430, 370, 140, 30)
        button_delete.clicked.connect(lambda: self.delete_row(table_widget, table_name))

        table_widget.show()
        button_save.show()
        button_delete.show()

        button_add_row = QPushButton("Додати рядок", self)
        button_add_row.setGeometry(595, 370, 110, 30)
        button_add_row.clicked.connect(lambda: self.add_row(table_name))

        table_widget.show()
        button_save.show()
        button_delete.show()
        button_add_row.show()

        cursor.close()
        db.close()

    def save_changes(self, table_widget, table_name, column_names):
        db = pymysql.connect(
            host="localhost",
            user="root",
            password="Kp549259#",
            database="AvariinaSlujba"
        )
        cursor = db.cursor()

        try:

            db.begin()

            for i in range(table_widget.rowCount()):
                row_values = []
                for j in range(table_widget.columnCount()):
                    item = table_widget.item(i, j)
                    if item is not None:
                        row_values.append(item.text())
                    else:
                        row_values.append('')

                set_values = ", ".join([f"{column_names[j]}='{row_values[j]}'" for j in range(len(column_names))])
                query = f"UPDATE {table_name} SET {set_values} WHERE id={i + 1}"
                print(f"Executing query: {query}")
                cursor.execute(query)

                self.logger.info(f"Manager {self.manager_id} змінив рядок {i + 1} у таблиці {table_name}")

            db.commit()

            QMessageBox.information(self, "Зберегти", "Зміни успішно збережено!")

        except Exception as e:

            db.rollback()
            QMessageBox.critical(self, "Помилка збереження змін", f"Не вдалося зберегти зміни: {str(e)}")

        finally:

            cursor.close()
            db.close()

    def delete_row(self, table_widget, table_name):

        selected_row = table_widget.currentRow()

        if selected_row >= 0:
            item = table_widget.item(selected_row, 0)
            if item is not None:
                row_id = item.text()

                db = pymysql.connect(
                    host="localhost",
                    user="root",
                    password="Kp549259#",
                    database="AvariinaSlujba"
                )
                cursor = db.cursor()

                try:

                    query = f"DELETE FROM {table_name} WHERE id={row_id}"
                    cursor.execute(query)
                    db.commit()

                    table_widget.removeRow(selected_row)

                    self.logger.info(f"Manager {self.manager_id} видалив рядок з таблиці {table_name}")

                    QMessageBox.information(self, "Видалити рядок", "Рядок успішно видалено!")
                except Exception as e:
                    print(f"Error occurred: {str(e)}")
                    db.rollback()
                    QMessageBox.critical(self, "Помилка видалення рядка", f"Не вдалося видалити рядок: {str(e)}")
                finally:
                    cursor.close()
                    db.close()
            else:
                QMessageBox.warning(self, "Видалити рядок", "No row selected!")
        else:
            QMessageBox.warning(self, "Видалити рядок", "No row selected!")

    def add_row(self, table_name):
        db = pymysql.connect(
            host="localhost",
            user="root",
            password="Kp549259#",
            database="AvariinaSlujba"
        )
        cursor = db.cursor()

        cursor.execute(f"SELECT MAX(id) FROM {table_name}")
        max_id = cursor.fetchone()[0]
        new_id = max_id + 1 if max_id is not None else 1

        cursor.execute(f"SHOW COLUMNS FROM {table_name}")
        columns = cursor.fetchall()
        column_names = [column[0] for column in columns]

        input_values = [str(new_id)]
        for column in column_names[1:]:
            value, ok = QInputDialog.getText(self, f"Enter {column}", f"Enter {column}")
            if ok:
                input_values.append(value)
            else:
                input_values.append('')

        placeholders = ', '.join(['%s'] * len(input_values))
        query = f"INSERT INTO {table_name} VALUES ({placeholders})"
        cursor.execute(query, input_values)
        db.commit()

        try:

            self.logger.info(f"Manager {self.manager_id} додав новий рядок до таблиці {table_name}")

            QMessageBox.information(self, "Додати рядок", "Рядок успішно додано!")

        except Exception as e:
            QMessageBox.critical(self, "Помилка додавання рядка", f"Не вдалося додати рядок: {str(e)}")

        cursor.close()
        db.close()
        self.adjustSize()

    def view_log(self):
        with open('manager_changes.log', 'r') as log_file:
            log_content = log_file.read()

        log_dialog = QDialog(self)
        log_dialog.setWindowTitle("Журнал змін")
        log_dialog.setGeometry(200, 200, 600, 400)

        log_text = QTextEdit(log_content, log_dialog)
        log_text.setGeometry(10, 10, 580, 380)

        log_dialog.exec()

    def logout(self):
        self.close()
        login_window.show()


class ClientMainWindow(QWidget):
    def __init__(self, client_id):
        super().__init__()
        self.setWindowTitle("Вікно клієнта")
        self.setGeometry(100, 100, 300, 200)

        self.label_brigade_id = QLabel(f"Client ID: {client_id}", self)
        self.label_brigade_id.setGeometry(50, 50, 200, 20)
        self.label_brigade_id.setFont(QFont("Arial", 12))

        self.button_logout = QPushButton("Logout", self)
        self.button_logout.setGeometry(100, 100, 100, 30)
        self.button_logout.clicked.connect(self.logout)

        self.button_table3 = QPushButton("Brigade Table", self)
        self.button_table3.setGeometry(100, 150, 110, 30)
        self.button_table3.clicked.connect(lambda: self.view_table("Brigade"))

        self.button_table4 = QPushButton("Request Table", self)
        self.button_table4.setGeometry(100, 200, 110, 30)
        self.button_table4.clicked.connect(lambda: self.view_table("Request"))

        self.button_table5 = QPushButton("Object Table", self)
        self.button_table5.setGeometry(100, 250, 110, 30)
        self.button_table5.clicked.connect(lambda: self.view_table("Object"))

        self.adjustSize()

    def view_table(self, table_name):
        db = pymysql.connect(
            host="localhost",
            user="root",
            password="Kp549259#",
            database="AvariinaSlujba"
        )
        cursor = db.cursor()

        cursor.execute(f"SHOW COLUMNS FROM {table_name}")
        columns = cursor.fetchall()
        column_names = [column[0] for column in columns]

        columns_to_hide = ["id", "login", "password_"]
        visible_columns = [column for column in column_names if column not in columns_to_hide]

        query = f"SELECT {', '.join(visible_columns)} FROM {table_name}"
        cursor.execute(query)
        result = cursor.fetchall()

        table_widget = QTableWidget(len(result), len(visible_columns), self)
        table_widget.setGeometry(250, 50, 500, 300)

        for i, row in enumerate(result):
            for j, value in enumerate(row):
                item = QTableWidgetItem(str(value))
                table_widget.setItem(i, j, item)

        table_widget.setHorizontalHeaderLabels(visible_columns)

        table_widget.show()
        table_widget.show()
        table_widget.show()
        cursor.close()
        db.close()

    def logout(self):
        self.close()
        login_window.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    login_window = LoginWindow()
    login_window.show()
sys.exit(app.exec_())


