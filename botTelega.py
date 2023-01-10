import telebot
from telebot.types import Message
from button import earbut_markup, admin_markup
from currency import loadCur, getCur
import os

bot = telebot.TeleBot(os.getenv('bottoken'))
ADMIN = [int(os.getenv('ADMIN'))]


@bot.message_handler(commands=['start'])
def start(msg: Message):
    send_mess = 'Воспользуйтесь клавиатурой'
    bot.send_message(msg.chat.id, send_mess, reply_markup=earbut_markup)


@bot.message_handler(content_types=['text', 'audio', 'document'])
def get_text_messages(msg: Message):
    if msg.text.lower() == "привет":
        bot.send_message(msg.chat.id, "привет, чем могу помочь?")
    elif msg.text == 'Доллар $':
        a = loadCur('USDKZT')
        bot.send_message(msg.chat.id, 'введите сумму которую перевести:')
        bot.register_next_step_handler(msg, translate, a)

    elif msg.text == 'Фунт Стерлингов £':
        a = loadCur('GBPKZT')
        bot.send_message(msg.chat.id, 'введите сумму которую перевести:')
        bot.register_next_step_handler(msg, translate, a)

    elif msg.text == 'Евро €':
        a = loadCur('EURKZT')
        bot.send_message(msg.chat.id, 'введите сумму которую перевести:')
        bot.register_next_step_handler(msg, translate, a)

    elif msg.text == 'Йены ¥':
        a = loadCur('JPYKZT')
        bot.send_message(msg.chat.id, 'введите сумму которую перевести:')
        bot.register_next_step_handler(msg, translate, a)

    elif msg.text == 'Update' and msg.chat.id in ADMIN:
        getCur()
        bot.send_message(msg.chat.id, 'Обновлено.')

    else:
        bot.send_message(msg.chat.id, msg.text)


def translate(msg: Message, i):
    markup = earbut_markup if msg.chat.id not in ADMIN else admin_markup
    try:
        cur = int(msg.text)
    except:
        bot.send_message(msg.chat.id, 'неправильно введено число.', reply_markup=markup)
    else:
        bot.send_message(msg.chat.id, '{0:,}'.format(int(cur * i)).replace(',', ' ') + '₸', reply_markup=markup)


if __name__ == "__main__":
    bot.infinity_polling()
