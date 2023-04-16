import telebot
from dotenv import load_dotenv
import os

load_dotenv()

bot = telebot.TeleBot(os.getenv("BOT_TOKEN"))

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Selamat datang di bot telegram")

@bot.message_handler(commands=['help'])
def help_bot(message):
    bot.reply_to(message, "Silahkan ketik /start untuk memulai")

@bot.message_handler(commands=['kalkulator'])
def kalkulator(message):
    bot.reply_to(message, "Silahkan ketik angka pertama")

    def get_angka_pertama(message):
        try:
            global angka_pertama
            angka_pertama = float(message.text)
            bot.reply_to(message, "Silahkan ketik angka kedua")
            bot.register_next_step_handler(message, get_angka_kedua)
        except ValueError:
            bot.reply_to(message, "Mohon masukkan angka yang valid")
            bot.register_next_step_handler(message, get_angka_pertama)

    def get_angka_kedua(message):
        try:
            global angka_kedua
            angka_kedua = float(message.text)
            bot.reply_to(message, "Silahkan ketik operator (+, -, *, /)")
            bot.register_next_step_handler(message, get_operator)
        except ValueError:
            bot.reply_to(message, "Mohon masukkan angka yang valid")
            bot.register_next_step_handler(message, get_angka_kedua)

    def get_operator(message):
        operator = message.text
        if operator in ['+', '-', '*', '/']:
            if operator == '+':
                hasil = angka_pertama + angka_kedua
            elif operator == '-':
                hasil = angka_pertama - angka_kedua
            elif operator == '*':
                hasil = angka_pertama * angka_kedua
            else:
                hasil = angka_pertama / angka_kedua
            bot.reply_to(message, f"Hasil: {hasil}")
        else:
            bot.reply_to(message, "Mohon masukkan operator yang valid (+, -, *, /)")
            bot.register_next_step_handler(message, get_operator)

    bot.register_next_step_handler(message, get_angka_pertama)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    if message.text == 'Halo' or message.text == 'halo':
        bot.reply_to(message, 'Halo juga')
    elif message.text == 'Hai' or message.text == 'hai':
        bot.reply_to(message, 'Hai juga')
    else:
        bot.reply_to(message, message.text)

bot.polling()