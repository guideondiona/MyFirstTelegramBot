from telebot import TeleBot
from config import config

bot = TeleBot(token=config.bot_token.get_secret_value())
