import telebot
from telebot import types

token = '2124699720:AAFDNnnz-OPbVPTKXSiftxyYJ3O8zUO6yAQ'
bot = telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row('Хочу', 'Расписание', 'Создатель', '/help', '/news', '/photo')
    bot.send_message(message.chat.id, 'Привет! Хочешь узнать свежую информацию о МТУСИ?', reply_markup=keyboard)

@bot.message_handler(commands=['help'])
def help_message(message):
    bot.send_message(message.chat.id, 'Я умею перекидывать на сайт Университета МТУСИ, расписание, на страницу создатедя бота, на новости и показывать фото Универа ')

@bot.message_handler(commands=['news'])
def news_message(message):
    if message.text == '/news':
        bot.send_message(message.chat.id, 'https://web.telegram.org/z/#-1101170442')

@bot.message_handler(commands=['photo'])
def photo_message(message):
    if message.text == '/photo':
        bot.send_photo(message.chat.id, photo='https://lh3.googleusercontent.com/proxy/zs4imJxix6I2kdPSsB1Yx3cCj5tGxLar7BFtvzcsn7k7T2zVtnCOhCNtXbgNAhNpmWsKnxCGdNoB3Msc8BKHCtZXZQy0pu7cwqPm_6WGT8pIOHs',caption='University MTUSI')



@bot.message_handler(content_types=['text'])
def word(message):
    if message.text.lower() == "хочу":
        bot.send_message(message.chat.id, 'Тогда тебе сюда – https://mtuci.ru/')
    elif message.text.lower() == "расписание":
        bot.send_message(message.chat.id, '[Расписание](https://disk.yandex.ru/i/BxcUZY1OKjK0GQ)', parse_mode='Markdown')
    elif message.text.lower() == "создатель":
        bot.send_message(message.chat.id, '[Руслан Заликов:Вконтакте](https://vk.com/idruslanzalikov)', parse_mode='Markdown')
        bot.send_message(message.chat.id, '[Руслан Заликов:Инстаграм](https://www.instagram.com/rzalikov/?hl=ru)', parse_mode='Markdown')




bot.polling(non_stop=True)