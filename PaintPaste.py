from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QFileDialog
from PyQt5.QtGui import QPainter, QColor, QImage, QPen, QIcon
from PyQt5.QtCore import Qt, QPoint, QRectF, QPointF
import os
import sys
import sqlite3

from LoginWindow import Ui_LoginWindow
from PaintWindow import Ui_PaintWindow

# Сохраняем имя пользователя, если он залогинился
USERNAME = ''


class Launch(QWidget):
    'Класс для запуска Paint окна, если пользователь залогинился'

    def show_paint_window(self):
        'Функция для скрытия LoginWindow и показа PaintWindow'
        
        login_window.hide()
        self.paint_window = Paint()
        self.paint_window.show()
        self.app = QApplication(sys.argv)
        self.app.setWindowIcon(QIcon('./icons/paint-can.png'))


class Login(QMainWindow, Ui_LoginWindow):
    'Класс для работы окна входа в аккаунт или регистрации нового'
    
    def __init__(self):
        super().__init__()
        
        # Подключение Ui
        self.ui = Ui_LoginWindow()
        self.ui.setupUi(self)
        
        self.ui.label_loggined.hide()

        self.con = sqlite3.connect('users.db')
        self.cur = self.con.cursor()
        
        # Создание БД
        self.cur.execute('''
            CREATE TABLE IF NOT EXISTS user_list(
                id INTEGER PRIMARY KEY,
                username TEXT UNIQUE,
                password TEXT
            )''')
        self.con.commit()
        
        self.cur.execute('''
            INSERT OR IGNORE INTO user_list(username, password)
            VALUES (?, ?), (?, ?)
        ''', ('admin', 'admin', 'user', 'qwerty123'))
        self.con.commit()
        
        # Создание папок для хранения картинок пользователей
        if not os.path.isdir('user_images'):
            os.mkdir('user_images')
            os.makedirs('user_images/admin')
            os.makedirs('user_images/user')
        
        self.initUi()
    
    def initUi(self):
        # Подключение функционала виджетов
        self.setWindowTitle('LoginWindow') 
        self.ui.btn_login.clicked.connect(self.login)
        self.ui.btn_register.clicked.connect(self.register)

    def login(self):
        'Вход в аккаунт'

        global USERNAME
        username = self.ui.lineEdit_username.text()
        password = self.ui.lineEdit_password.text()

        # Проверка на наличие в БД строки с введенными в виджеты lineEdit 
        # именем пользоателя и паролем
        self.id = self.cur.execute("""SELECT id FROM user_list
            WHERE username = 
            ? AND password = ?""", (username, password)
        ).fetchall()
        if self.id:
            # Пользователь залогинился
            USERNAME = username
            self.ui.label_loggined.show()
            
            Launch.show_paint_window(self) # Открытие Paint окна
            
        else:
            # Пользователь не залогинился
            
            # Проверка наличия введенного никнейма в БД и вывод
            # соответствующего вердикта
            all = self.cur.execute(
                """SELECT * FROM user_list WHERE username = ?""", (username,)
            ).fetchall()
            if len(all) != 0:
                self.ui.label_verdict.setText('Incorect password')
            else:
                self.ui.label_verdict.setText('Username not found')

    def register(self):
        'Регистрация новых пользователей'

        username = self.ui.lineEdit_username.text()
        password = self.ui.lineEdit_password.text()
        if len(username) == 0:
            # Проверка на ненулевую длиину имени пользоателя
            self.ui.label_verdict.setText('Username can\'t be empty')
        else:
            all = self.cur.execute(
                """SELECT * FROM user_list WHERE username = ?""", (username,)
            ).fetchall()
            if len(all) != 0:
                # Проверка на наличие в БД имени пользоателя,
                # которое хотят зарегистрировать
                self.ui.label_verdict.setText('Username is taken')
            elif not password:
                # Проверка на ненулевую длиину пароля
                self.ui.label_verdict.setText('Password can\'t be empty')
            elif username[-1] in '. ':
                # Проверка на то что имя пользователя не заканчивается
                # на точку или пробел
                self.ui.label_verdict.setText('Username can\'t end with "." or " "')
            else:
                # Проверка на то что имя пользователя не содержит некоторые символы
                good = True
                for char in username:
                    if char in '\/:*?"<>|+':
                        good = False
                        break
                if not good:
                    self.ui.label_verdict.setText(
                        'You can\'t use "\/:*?"<>|+" in "\n" username')
                if good:
                    # Новый пользователь зарегистрирован
                    self.ui.label_verdict.setText('You are registred. Now login')
                    self.cur.execute(
                        '''INSERT INTO user_list(username, password) VALUES(?, ?)''',
                    (username, password))
                    self.con.commit()
                    
                    os.makedirs(f'user_images/{username}')


class Paint(QMainWindow, Ui_PaintWindow):
    'Класс ддя работы главного окна для рисования'
    
    def __init__(self):
        super().__init__()
        
        # Список названий цветов для показа пользователю и список их названий в Qt
        self.color_names = ['Black','White', 'Dark Gray', 'Gray', 'Light Gray',
            'Red', 'Green', 'Blue', 'Cyan', 'Magenta', 'Yellow', 'Dark Red',
            'Dark Green', 'Dark Blue', 'Dark Cyan', 'Dark Magenta', 'Dark Yellow']
        
        self.color_values = ['black', 'white', 'darkGray', 'gray', 'lightGray',
            'red', 'green', 'blue', 'cyan', 'magenta', 'yellow', 'darkRed',
            'darkGreen', 'darkBlue', 'darkCyan', 'darkMagenta', 'darkYellow']
        
        # Подключение Ui
        self.ui = Ui_PaintWindow()
        self.ui.setupUi(self)

        self.initUi()
        
        self.image_create()
        
        # Установка инструмента на кисть
        self.instrument = 'Brush'
    
    def initUi(self):
        'Подключение виджетов к их функциям'
        
        self.ui.comboBox_BrushSize.currentTextChanged.connect(self.brush_size_change)
        self.ui.comboBox_BrushColor.currentTextChanged.connect(self.brush_color_change)
        self.ui.BrushButton.clicked.connect(self.set_brush)
        self.ui.PenButton.clicked.connect(self.set_pencil)
        self.ui.EraserButton.clicked.connect(self.set_eraser)
        self.ui.DropperButton.clicked.connect(self.set_dropper)
        self.ui.LineButton.clicked.connect(self.set_line)
        self.ui.CircleButton.clicked.connect(self.set_circle)
        self.ui.RectangleButton.clicked.connect(self.set_rectangle)
        self.ui.ClearButton.clicked.connect(self.clear_all)
        self.ui.actionOpen.triggered.connect(self.open_file)
        self.ui.actionSaveImageAs.triggered.connect(self.save_file)
        self.ui.actionSave_to_my_files.triggered.connect(self.save_to_user_images)
        self.ui.actionOpen_from_my_files.triggered.connect(self.open_from_user_images)
        
    def image_create(self):
        'Создание холста для рисования'
        
        self.setMouseTracking = True
        self.image = QImage(self.size(), QImage.Format_ARGB32)
        self.image.fill(Qt.white)
        self.drawing = False
        self.brushSize = 4
        self.brushColor = Qt.black
        self.start_pos = QPointF()
        self.end_pos = QPointF()
        self.lastPoint = QPoint()
        self.ui.comboBox_BrushColor.setCurrentIndex(1)
        self.ui.comboBox_BrushSize.setCurrentIndex(1)
        self.ui.label_CurentColor.setStyleSheet('QLabel { background-color: %s; }' % '#000000')

    def brush_size_change(self):
        'Измениение размера кисти'
        
        px = int(self.ui.comboBox_BrushSize.currentText()[:-2])
        self.brushSize = px
    
    def brush_color_change(self):
        'Измененение цвета кисти'
        
        color = self.color_values[self.color_names.index(self.ui.comboBox_BrushColor.currentText())]
        self.brushColor = eval(f'Qt.{color}')
    
    def set_brush(self):
        'Изменение инструмента на кисть'
        
        self.instrument = 'Brush'
    
    def set_pencil(self):
        'Изменение инструмента на кисть'
        
        self.instrument = 'Pen'
        self.brushSize = 2
        self.ui.comboBox_BrushSize.setCurrentIndex(0)
    
    def set_eraser(self):
        'Изменение инструмента на ластик'
        
        self.instrument = 'Eraser'
        self.brushColor = Qt.white
        self.brushSize = 8
        self.ui.comboBox_BrushSize.setCurrentIndex(2)
    
    def set_dropper(self):
        'Изменение инструмента на пипетку'
        
        self.instrument = 'Dropper'
        
    def set_line(self):
        'Изменение инструмента на прямую линию'
        
        self.instrument = 'Line'
    
    def set_rectangle(self):
        'Изменение инструмента на прямоугольник'
        
        self.instrument = 'Rectangle'

    def set_circle(self):
        'Изменение инструмента на круг'
        
        self.instrument = 'Circle'
    
    def clear_all(self):
        'Очистка холста'
        
        self.image.fill(Qt.white)
        self.update()
        
    def open_file(self):
        'Октрытие файла и его отображение на холсте'
        
        file_name = QFileDialog.getOpenFileName(
            self, 'Select File', '',
            'Images(*.png *.jpg *.jpeg);;PNG(*.png);;JPEG(*.jpg *.jpeg);;All Files(*.*)')[0]
        if file_name:
            self.image.load(file_name)
    
    def save_file(self):
        'Сохранение файла'
        
        file_name = QFileDialog.getSaveFileName(
            self, 'Save file', '',
            'Images(*.png *.jpg *.jpeg);;PNG(*.png);;JPEG(*.jpg *.jpeg);;All Files(*.*)')[0]
        if file_name:
            self.image.save(file_name)
    
    def save_to_user_images(self):
        'Сохранение файла в папку пользователя'
        
        file_name = QFileDialog.getSaveFileName(
            self, 'Save to my Images', f'./user_images/{USERNAME}',
            'Images(*.png *.jpg *.jpeg);;PNG(*.png);;JPEG(*.jpg *.jpeg);;All Files(*.*)')[0]
        if file_name:
            self.image.save(file_name)
    
    def open_from_user_images(self):
        'Октрытие файла из папки пользователя и его отображение на холсте'
        
        file_name = QFileDialog.getOpenFileName(
            self, 'Select File', f'./user_images/{USERNAME}',
            'Images(*.png *.jpg *.jpeg);;PNG(*.png);;JPEG(*.jpg *.jpeg);;All Files(*.*)')[0]
        if file_name:
            self.image.load(file_name)
        
    def draw(self, canvas):
        'Функция принимает картинку с холста и отрисовывает на нем что-то в зависимости от выбраного инструмента'
        
        painter = QPainter(canvas)
        painter.setPen(QPen(self.brushColor, self.brushSize, Qt.SolidLine))
        if self.instrument == 'Line':
            painter.drawLine(self.start_pos, self.end_pos)
        elif self.instrument == 'Circle':
            painter.drawEllipse(QRectF(self.start_pos, self.end_pos))
        elif self.instrument == 'Rectangle':
            painter.drawRect(QRectF(self.start_pos, self.end_pos))
    
    def paintEvent(self, event):
        'Переопределение функции paintEvent'
        
        canvasPainter = QPainter(self)
        canvasPainter.drawImage(self.image.rect(), self.image)
        self.draw(self)
        
    def mousePressEvent(self, event):
        'Переопределение функции mousePressEvent в зависимости от выбранного инструмента'
        
        if self.instrument in ['Brush', 'Eraser', 'Pen']:
            if event.button() == Qt.LeftButton:
                self.drawing = True
                self.lastPoint = event.pos()
        elif self.instrument == 'Dropper':
            c = self.image.pixel(event.pos())
            hex = QColor(c).name()
            self.ui.label_CurentColor.setStyleSheet('QLabel { background-color: %s; }' % hex)
            self.brushColor = QColor(hex)
        else:
            self.start_pos = event.pos()
    
    def mouseMoveEvent(self, event):
        'Переопределение функции mouseMoveEvent в зависимости от выбранного инструмента'
        
        if self.instrument in ['Brush', 'Eraser', 'Pen']:
            if (event.buttons() and Qt.LeftButton) and self.drawing:
                painter = QPainter(self.image)
                painter.setPen(QPen(self.brushColor, self.brushSize,
                                Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))
                painter.drawLine(self.lastPoint, event.pos())
                self.lastPoint = event.pos()
        else:
            if event.buttons() and Qt.LeftButton :
                self.end_pos = event.pos()
        self.update()
            
    def mouseReleaseEvent(self, event):
        'Переопределение функции mouseReleaseEvent в зависимости от выбранного инструмента'
        
        if self.instrument in ['Brush', 'Eraser', 'Pen']:
            if event.button() == Qt.LeftButton:
                self.drawing = False
        else:
            self.end_pos = event.pos()
            self.draw(self.image)
        self.update()
            

if __name__ == '__main__':
    App = QApplication(sys.argv)
    App.setWindowIcon(QIcon('./icons/paint-can.png'))
    login_window = Login()
    login_window.show()
    sys.exit(App.exec_())

#  _____        __         ____      ____    ___ ___    _____      
# |___ / _   _ / /_   __ _|  _ \ ___| __ )  |_ _|_ _|__|_   _| __  
#   |_ \| | | | '_ \ / _` | |_) / _ \  _ \   | | | |/ _ \| || '_ \ 
#  ___) | |_| | (_) | (_| |  __/  __/ |_) |  | | | |  __/| || |_) |
# |____/ \__, |\___/ \__,_|_|   \___|____/  |___|___\___||_|| .__/ 
#        |___/                                              |_|    

#  ______   _ ____ _____  ____ 
# |__  / | | | __ )___ / / ___|
#   / /| | | |  _ \ |_ \| |    
#  / /_| |_| | |_) |__) | |___ 
# /____|\___/|____/____/ \____|
