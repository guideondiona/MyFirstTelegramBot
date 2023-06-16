from telebot.types import Message
from bot.bot import bot
from bot.keyboards import earbut_markup
from misc.currency import loadCur


@bot.message_handler(commands=["start"])
def start_message_handler(msg: Message):
    send_mess = "Воспользуйтесь клавиатурой"
    bot.send_message(msg.chat.id, send_mess, reply_markup=earbut_markup)


@bot.message_handler()
def currency_message_handler(msg: Message):
    match msg.text:
        case "Доллар $":
            currency = loadCur("USDKZT")
        case "Фунт Стерлингов £":
            currency = loadCur("GBPKZT")
        case "Евро €":
            currency = loadCur("EURKZT")
        case "Йены ¥":
            currency = loadCur("JPYKZT")
        case "Рубли ₽":
            currency = loadCur("RUBKZT")
        case _:
            return
    bot.send_message(msg.chat.id, "Введите сумму которую перевести:")
    bot.register_next_step_handler(msg, translate, currency)


def translate(msg: Message, i):
    try:
        cur = float(msg.text.replace(",", "."))
        assert cur > 0
        assert cur < 10**30
    except:
        bot.send_message(
            msg.chat.id, "Неправильно введено число.", reply_markup=earbut_markup
        )
    else:
        bot.send_message(
            msg.chat.id,
            "{0:,}".format(int(cur * i)).replace(",", " ") + "₸",
            reply_markup=earbut_markup,
        )
