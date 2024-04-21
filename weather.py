from PyQt5 import QtCore, QtGui, QtWidgets
import requests
from googletrans import Translator
import pickle



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 700)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        MainWindow.setFont(font)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color: rgb(30, 144, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.icon = QtWidgets.QLabel(self.centralwidget)
        self.icon.setGeometry(QtCore.QRect(90, 60, 161, 161))
        self.icon.setText("")
        self.icon.setPixmap(QtGui.QPixmap("img/sun.png"))
        self.icon.setScaledContents(True)
        self.icon.setObjectName("icon")
        self.weather = QtWidgets.QLabel(self.centralwidget)
        self.weather.setGeometry(QtCore.QRect(40, 250, 261, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.weather.setFont(font)
        self.weather.setStyleSheet(" border: 2px solid #00BFFF; \n"
" border-radius: 10px; \n"
" background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #00BFFF, stop: 1 #1E90FF); \n"
" color: white;\n")
        self.weather.setAlignment(QtCore.Qt.AlignCenter)
        self.weather.setObjectName("weather")
        self.temp = QtWidgets.QLabel(self.centralwidget)
        self.temp.setGeometry(QtCore.QRect(330, 40, 241, 161))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.temp.setFont(font)
        self.temp.setStyleSheet(" border: 2px solid #00BFFF; \n"
" border-radius: 10px; \n"
" background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #00BFFF, stop: 1 #1E90FF); \n"
" color: white; ")
        self.temp.setTextFormat(QtCore.Qt.AutoText)
        self.temp.setScaledContents(False)
        self.temp.setAlignment(QtCore.Qt.AlignCenter)
        self.temp.setObjectName("temp")
        self.curs_dollara_label = QtWidgets.QLabel(self.centralwidget)
        self.curs_dollara_label.setGeometry(QtCore.QRect(30, 390, 261, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.curs_dollara_label.setFont(font)
        self.curs_dollara_label.setStyleSheet("border: 2px solid #00BFFF; \n"
" border-radius: 10px; \n"
" background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #00BFFF, stop: 1 #1E90FF); \n"
" color: white; ")
        self.curs_dollara_label.setAlignment(QtCore.Qt.AlignCenter)
        self.curs_dollara_label.setObjectName("curs_dollara_label")
        self.curs_euro_label = QtWidgets.QLabel(self.centralwidget)
        self.curs_euro_label.setGeometry(QtCore.QRect(320, 390, 261, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.curs_euro_label.setFont(font)
        self.curs_euro_label.setStyleSheet("border: 2px solid #00BFFF; \n"
" border-radius: 10px; \n"
" background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #00BFFF, stop: 1 #1E90FF); \n"
" color: white; ")
        self.curs_euro_label.setAlignment(QtCore.Qt.AlignCenter)
        self.curs_euro_label.setObjectName("curs_euro_label")
        self.curs_dollara = QtWidgets.QLabel(self.centralwidget)
        self.curs_dollara.setGeometry(QtCore.QRect(30, 460, 261, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.curs_dollara.setFont(font)
        self.curs_dollara.setStyleSheet("color: rgb(255, 255, 255);")
        self.curs_dollara.setAlignment(QtCore.Qt.AlignCenter)
        self.curs_dollara.setObjectName("curs_dollara")
        self.curs_euro = QtWidgets.QLabel(self.centralwidget)
        self.curs_euro.setGeometry(QtCore.QRect(320, 460, 261, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.curs_euro.setFont(font)
        self.curs_euro.setStyleSheet("color: rgb(255, 255, 255);")
        self.curs_euro.setAlignment(QtCore.Qt.AlignCenter)
        self.curs_euro.setObjectName("curs_euro")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 370, 601, 16))
        self.frame.setStyleSheet("QFrame {\n"
"    border: none;\n"
"    border-top: 2px solid white; \n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.rub_input_fo_dollar = QtWidgets.QLineEdit(self.centralwidget)
        self.rub_input_fo_dollar.setGeometry(QtCore.QRect(30, 560, 261, 31))
        self.rub_input_fo_dollar.setStyleSheet(" border: 2px solid #00BFFF; \n"
" border-radius: 10px; \n"
" background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #00BFFF, stop: 1 #1E90FF); \n"
" color: white; ")
        self.rub_input_fo_dollar.setObjectName("rub_input_fo_dollar")
        self.rub_input_fo_dollar.setAlignment(QtCore.Qt.AlignCenter)
        self.output_dollar = QtWidgets.QLabel(self.centralwidget)
        self.output_dollar.setGeometry(QtCore.QRect(30, 640, 261, 31))
        self.output_dollar.setStyleSheet(" border: 2px solid #00BFFF; \n"
" border-radius: 10px;\n"
" background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #00BFFF, stop: 1 #1E90FF); \n"
" color: white; ")
        self.output_dollar.setObjectName("output_dollar")
        self.output_dollar.setAlignment(QtCore.Qt.AlignCenter)
        self.rub_input_fo_euro = QtWidgets.QLineEdit(self.centralwidget)
        self.rub_input_fo_euro.setGeometry(QtCore.QRect(320, 560, 261, 31))
        self.rub_input_fo_euro.setStyleSheet(" border: 2px solid #00BFFF; \n"
" border-radius: 10px; \n"
" background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #00BFFF, stop: 1 #1E90FF); \n"
" color: white; ")
        self.rub_input_fo_euro.setObjectName("rub_input_fo_euro")
        self.rub_input_fo_euro.setAlignment(QtCore.Qt.AlignCenter)
        self.output_euro = QtWidgets.QLabel(self.centralwidget)
        self.output_euro.setGeometry(QtCore.QRect(320, 640, 261, 31))
        self.output_euro.setStyleSheet(" border: 2px solid #00BFFF; \n"
" border-radius: 10px; \n"
" background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #00BFFF, stop: 1 #1E90FF); \n"
" color: white; ")
        self.output_euro.setObjectName("output_euro")
        self.output_euro.setAlignment(QtCore.Qt.AlignCenter)
        self.rubli_label_1 = QtWidgets.QLabel(self.centralwidget)
        self.rubli_label_1.setGeometry(QtCore.QRect(30, 530, 261, 21))
        self.rubli_label_1.setStyleSheet(" border: 2px solid #00BFFF; \n"
" border-radius: 10px; /* Скругляем углы */\n"
" background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #00BFFF, stop: 1 #1E90FF); \n"
" color: white; ")
        self.rubli_label_1.setAlignment(QtCore.Qt.AlignCenter)
        self.rubli_label_1.setObjectName("rubli_label_1")
        self.dollars_label = QtWidgets.QLabel(self.centralwidget)
        self.dollars_label.setGeometry(QtCore.QRect(30, 610, 261, 21))
        self.dollars_label.setStyleSheet(" border: 2px solid #00BFFF; \n"
" border-radius: 10px; \n"
" background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #00BFFF, stop: 1 #1E90FF); \n"
" color: white; ")
        self.dollars_label.setAlignment(QtCore.Qt.AlignCenter)
        self.dollars_label.setObjectName("dollars_label")
        self.rubli_label_2 = QtWidgets.QLabel(self.centralwidget)
        self.rubli_label_2.setGeometry(QtCore.QRect(320, 530, 261, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.rubli_label_2.setFont(font)
        self.rubli_label_2.setStyleSheet(" border: 2px solid #00BFFF; \n"
" border-radius: 10px; \n"
" background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #00BFFF, stop: 1 #1E90FF); \n"
" color: white; ")
        self.rubli_label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.rubli_label_2.setObjectName("rubli_label_2")
        self.euro_label = QtWidgets.QLabel(self.centralwidget)
        self.euro_label.setGeometry(QtCore.QRect(320, 610, 261, 21))
        self.euro_label.setStyleSheet(" border: 2px solid #00BFFF; \n"
" border-radius: 10px; \n"
" background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #00BFFF, stop: 1 #1E90FF); \n"
" color: white; ")
        self.euro_label.setAlignment(QtCore.Qt.AlignCenter)
        self.euro_label.setObjectName("euro_label")
        self.city = QtWidgets.QLineEdit(self.centralwidget)
        self.city.setGeometry(QtCore.QRect(40, 10, 261, 31))
        self.city.setStyleSheet(" border: 2px solid #00BFFF; \n"
" border-radius: 10px; \n"
" background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #00BFFF, stop: 1 #1E90FF); \n"
" color: white; ")
        self.city.setObjectName("city")
        self.city.setAlignment(QtCore.Qt.AlignCenter)
        self.btn_city = QtWidgets.QPushButton(self.centralwidget)
        self.btn_city.setGeometry(QtCore.QRect(50, 20, 10, 10))
        self.btn_city.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.btn_city.setText("")
        self.btn_city.setObjectName("btn_city")
        self.temp_fills_like = QtWidgets.QLabel(self.centralwidget)
        self.temp_fills_like.setGeometry(QtCore.QRect(330, 210, 241, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.temp_fills_like.setFont(font)
        self.temp_fills_like.setStyleSheet(" border: 2px solid #00BFFF; \n"
" border-radius: 10px; \n"
" background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #00BFFF, stop: 1 #1E90FF); \n"
" color: white; ")
        self.temp_fills_like.setTextFormat(QtCore.Qt.AutoText)
        self.temp_fills_like.setScaledContents(False)
        self.temp_fills_like.setAlignment(QtCore.Qt.AlignCenter)
        self.temp_fills_like.setObjectName("temp_fills_like")
        self.visibility = QtWidgets.QLabel(self.centralwidget)
        self.visibility.setGeometry(QtCore.QRect(70, 300, 201, 41))
        self.visibility.setStyleSheet(" border: 2px solid #00BFFF; \n"
" border-radius: 10px; \n"
" background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #00BFFF, stop: 1 #1E90FF); \n"
" color: white; ")
        self.visibility.setAlignment(QtCore.Qt.AlignCenter)
        self.visibility.setObjectName("visibility")
        self.wind_speed = QtWidgets.QLabel(self.centralwidget)
        self.wind_speed.setGeometry(QtCore.QRect(330, 270, 241, 21))
        self.wind_speed.setStyleSheet(" border: 2px solid #00BFFF; \n"
" border-radius: 10px; \n"
" background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #00BFFF, stop: 1 #1E90FF); \n"
" color: white; ")
        self.wind_speed.setAlignment(QtCore.Qt.AlignCenter)
        self.wind_speed.setObjectName("wind_speed")
        self.wind_deg = QtWidgets.QLabel(self.centralwidget)
        self.wind_deg.setGeometry(QtCore.QRect(330, 300, 241, 21))
        self.wind_deg.setStyleSheet(" border: 2px solid #00BFFF; \n"
" border-radius: 10px; \n"
" background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #00BFFF, stop: 1 #1E90FF); \n"
" color: white; ")
        self.wind_deg.setAlignment(QtCore.Qt.AlignCenter)
        self.wind_deg.setObjectName("wind_deg")
        self.wind_gust = QtWidgets.QLabel(self.centralwidget)
        self.wind_gust.setGeometry(QtCore.QRect(330, 330, 241, 21))
        self.wind_gust.setStyleSheet(" border: 2px solid #00BFFF; \n"
" border-radius: 10px; \n"
" background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #00BFFF, stop: 1 #1E90FF); \n"
" color: white; ")
        self.wind_gust.setAlignment(QtCore.Qt.AlignCenter)
        self.wind_gust.setObjectName("wind_gust")

        self.btn_dol = QtWidgets.QPushButton(self.centralwidget)
        self.btn_dol.setGeometry(QtCore.QRect(40, 570, 10, 10))
        self.btn_dol.setObjectName("btn_dol")
        self.btn_dol.setStyleSheet('background-color: white;')

        self.btn_eur = QtWidgets.QPushButton(self.centralwidget)
        self.btn_eur.setGeometry(QtCore.QRect(330, 570, 10, 10))
        self.btn_eur.setObjectName("btn_dol")
        self.btn_eur.setStyleSheet('background-color: white;')

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.translator = Translator()
        self.course()
        self.get_weather()
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.weather.setText(_translate("MainWindow", "Ясно"))
        self.temp.setText(_translate("MainWindow", "<html><head/><body><p>15<span style=\" vertical-align:super;\">o</span></p><p><span style=\" font-size:14pt;\">мин.:   макс.:</span></p></body></html>"))
        self.curs_dollara_label.setText(_translate("MainWindow", "Курс доллара к рублю"))
        self.curs_euro_label.setText(_translate("MainWindow", "Курс евро к рублю"))
        self.curs_dollara.setText(_translate("MainWindow", "100"))
        self.curs_euro.setText(_translate("MainWindow", "100"))
        self.rubli_label_1.setText(_translate("MainWindow", "Рубли"))
        self.dollars_label.setText(_translate("MainWindow", "Доллары"))
        self.rubli_label_2.setText(_translate("MainWindow", "Рубли"))
        self.euro_label.setText(_translate("MainWindow", "Евро"))
        self.temp_fills_like.setText(_translate("MainWindow", "<html><head/><body><p>Ощущается как:</p></body></html>"))
        self.visibility.setText(_translate("MainWindow", "Видимость:"))
        self.wind_speed.setText(_translate("MainWindow", "Скорость ветра:"))
        self.wind_deg.setText(_translate("MainWindow", "Направление:"))
        self.wind_gust.setText(_translate("MainWindow", "Порывы до:"))

    def course(self):
        #  получение курсов валют
        to_currency = 'RUB'

        from_currency_USD = 'USD'
        url_usd = f"https://api.exchangerate-api.com/v4/latest/{from_currency_USD}"
        from_currency_EUR = 'EUR'
        url_eur = f"https://api.exchangerate-api.com/v4/latest/{from_currency_EUR}"

        response_usd = requests.get(url_usd)
        data_usd = response_usd.json()

        response_eur = requests.get(url_eur)
        data_eur = response_eur.json()

        self.rate_usd = data_usd['rates'][to_currency]
        self.rate_eur = data_eur['rates'][to_currency]

        self.curs_dollara.setText(f'{self.rate_usd}')
        self.curs_euro.setText(f'{self.rate_eur}')
        
        #  активация подсчёта если нажата кнопка
        self.btn_dol.clicked.connect(lambda: self.currency_counting(self.rate_usd, self.rub_input_fo_dollar, self.output_dollar))
        self.btn_eur.clicked.connect(lambda: self.currency_counting(self.rate_eur, self.rub_input_fo_euro, self.output_euro))
        self.btn_city.clicked.connect(self.get_weather)

    def currency_counting(self, val, rub_for, output):
        #  подсчёт
        rub = rub_for.text().strip()
        if len(rub) > 0:
            try:
                result = eval(f'{rub}*{val}')
                output.setText(str(result))
            except:
                output.setText('Значение не может быть посчитано')
        
    def get_weather(self):
        #  получение погоды из .pkl файла
        if len(self.city.text()) == 0:
            try:
                with open('location.pkl', 'rb') as f:
                    self.city.setText(str(pickle.load(f)))
            except:
                pass

        #  получение информации о погоде в городе
        if len(self.city.text()) > 0:
            city_name = self.translator.translate(self.city.text()).text
            API = '9eeef01f90e326deb316a1333200354f'
            URL = f"https://api.openweathermap.org/data/2.5/weather?q={city_name.lower().capitalize()}&appid={API}&units=metric"
            try:
                res = requests.get(URL).json()
            except:
                self.city.setText('Введите существующий город или введите его название на EN')
            try:
                self.visibility.setText(f"Видимость: {res['visibility']}")
            except:
                self.visibility.setText('Видимость: Не найдено информации')
            try:
                self.temp_fills_like.setText(f"Ощущается как: {res['main']['feels_like']}")
            except:
                self.temp_fills_like.setText('Ощущается как: Не найдено информации')
            try:
                self.temp.setText(f"{res['main']['temp']}⁰\n"
                                  f"мин.: {res['main']['temp_min']}⁰ макс.: {res['main']['temp_max']}⁰")
            except:
                self.temp.setText('Мин. макс.: Не найдено информации')
            try:
                self.wind_speed.setText(f"Скорость ветра: {res['wind']['speed']} м/с")
            except:
                self.wind_speed.setText('Скорость ветра: Не найдено информации')
            try:
                self.wind_gust.setText(f"Порывы до: {res['wind']['gust']}")
            except:
                self.wind_gust.setText('Порывы до: Не найдено информации')
            try:
                match res['wind']['deg']:
                    case x if (340 <= x <= 359) or (0 <= x <= 20):
                        self.wind_deg.setText('Направление: С')
                    case x if 21 <= x <= 70:
                        self.wind_deg.setText('Направление: СВ')
                    case x if 71 <= x <= 111:
                        self.wind_deg.setText('Направление: В')
                    case x if 112 <= x <= 160:
                        self.wind_deg.setText('Направление: ЮВ')
                    case x if 161 <= x <= 201:
                        self.wind_deg.setText('Направление: Ю')
                    case x if 202 <= x <= 250:
                        self.wind_deg.setText('Направление: ЮЗ')
                    case x if 251 <= x <= 290:
                        self.wind_deg.setText('Направление: З')
                    case x if 291 <= x <= 339:
                        self.wind_deg.setText('Направление: СЗ')
            except:
                self.wind_gust.setText('Направление: Не найдено информации')
            try:
                match res['clouds']['all']:
                    case x if 0 <= x <= 10:
                        self.weather.setText('Ясно')
                        self.icon.setPixmap(QtGui.QPixmap("img/sun.png"))
                    case x if 11 <= x <= 39:
                        self.weather.setText('Преимущественно солнечно')
                        self.icon.setPixmap(QtGui.QPixmap("img/sunny.png"))
                    case x if 40 <= x <= 60:
                        self.weather.setText('Преимущественно облачно')
                        self.icon.setPixmap(QtGui.QPixmap("img/sunny.png"))
                    case x if 61 <= x <= 100:
                        self.weather.setText('Облачно')
                        self.icon.setPixmap(QtGui.QPixmap("img/sky.png"))
            except:
                self.weather.setText('Не найдено информации')
                self.icon.setPixmap(QtGui.QPixmap("img/error.png"))

            #  сохранение последнего введённого города в .pkl
            with open('location.pkl', 'wb') as f:
                pickle.dump(self.city.text(), f)
            

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
