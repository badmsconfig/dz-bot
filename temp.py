import telebot
import requests

# Замените YOUR_API_KEY на ваш API ключ OpenWeatherMap
API_KEY = '2806931948434976a456a95e7ce2499b'
# Город, для которого нужно получить погоду (Паттая)
CITY = 'Pattaya'
# Единицы измерения температуры (имперская - Fahrenheit или метрическая - Celsius)
UNITS = 'metric'

# Прокси-адрес
PROXY = {'http://65.21.67.151:20570:lgeKT3sVEj4C:uMb7GTTsVL'}

# Создаем объект бота
bot = telebot.TeleBot("6426802551:AAGBYJWzzAiPp5Tuv3s3_xKpncMSPEV9jvM")

# Функция для обработки команды /start
@bot.message_handler(commands=['start'])
def start(message):
    # Формируем URL для запроса к OpenWeatherMap API
    url = f'http://api.openweathermap.org/data/2.5/weather?q={CITY}&units={UNITS}&appid={API_KEY}'

    # Создаем объект сессии с прокси
    session = requests.Session()
    session.proxies = PROXY

    # Отправляем запрос и получаем данные о погоде
    response = session.get(url)
    weather_data = response.json()

    # Извлекаем температуру из полученных данных
    temperature = weather_data['main']['temp']

    # Отправляем сообщение с температурой в Щелково
    bot.send_message(message.chat.id, f'Текущая температура в Паттае: {temperature}°C')

@bot.message_handler(commands=['help'])
def help_message(message):
    help_text = "Бот для просмотра температуры\n\n"
    help_text += "/start - Получить температуру\n"
    help_text += "/help - Показать справку"
    bot.send_message(message.chat.id, help_text)

# Запускаем бота
bot.polling()