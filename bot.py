import telebot
from dotenv import load_dotenv
import os

load_dotenv()

bot = telebot.TeleBot(os.getenv("BOT_TOKEN"))

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Selamat datang di bot telegram buatan Fauzan Gifari. Silahkan ketik /help untuk melihat daftar perintah yang tersedia.")
    bot.register_next_step_handler(message, back)

    @bot.message_handler(commands=['help'])
    def help_bot(message):
        bot.reply_to(message, '''
        Ada beberapa perintah yang tersedia di bot ini, yaitu:
        \n => /kalkulator untuk menggunakan kalkulator sederhana dengan operator (+, -, *, /).
        \n => /quotes untuk mendapatkan quotes dari bot ini.
        \n => /help untuk melihat daftar perintah yang tersedia.
        \n => /start untuk memulai bot ini.
        \n => /about untuk melihat informasi tentang pembuat bot ini.''')

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

    @bot.message_handler(commands=['quotes'])
    def quotes1(message):
        bot.reply_to(message, "Biarlah semesta bekerja, kita rebahan aja")
        bot.register_next_step_handler(message, quotes2)

    def quotes2(message):
        quotes = message.text
        if quotes == 'lagi' or quotes == 'Lagi':
            bot.reply_to(message, "Tetap jalani hidup, walau jalannya lagi rusak")
            bot.register_next_step_handler(message, quotes3)
        else:
            bot.reply_to(message, "Yahaha wahyuuu pal pale pal palee")

    def quotes3(message):
        quotes = message.text
        if quotes == 'lagi' or quotes == 'Lagi':
            bot.reply_to(message, "Hiduplah seperti tai ayam, walaupun dibawah tetapi tidak ada berani menginjaknya")
            bot.register_next_step_handler(message, quotes4)
        else:
            bot.reply_to(message, "Yahaha wahyuuu pal pale pal palee")

    def quotes4(message):
        quotes = message.text
        if quotes == 'lagi' or quotes == 'Lagi':
            bot.reply_to(message, "Jangan pernah menyerah, tapi tau diri lahh")
            bot.register_next_step_handler(message, quotes5)
        else:
            bot.reply_to(message, "Yahaha wahyuuu pal pale pal palee")

    def quotes5(message):
        quotes = message.text
        if quotes == 'lagi' or quotes == 'Lagi':
            bot.reply_to(message, "Habis dah quotes ku, nanti ku buat lagi")
        else:
            bot.reply_to(message, "Yahaha wahyuuu pal pale pal palee")

    @bot.message_handler(commands=['about'])
    def about(message):
        bot.reply_to(message, "Bot ini dibuat oleh Fauzan Gifari, kamu bisa mengunjungi instagram ku di https://www.instagram.com/fauzangfri")


    @bot.message_handler(func=lambda message: True)
    def echo_all(message):
        if message.text == 'Halo' or message.text == 'halo':
            bot.reply_to(message, 'Halo juga')
        elif message.text == 'Hai' or message.text == 'hai':
            bot.reply_to(message, 'Hai juga')
        elif message.text == 'Apa Kabar?' or message.text == 'apa kabar?':
            bot.reply_to(message, 'Baik, dan kamu?')
        else:
            bot.reply_to(message, "Yahaha wahyuuu pal pale pal palee")

@bot.message_handler(func=lambda message: True)
def back(message):
    bot.reply_to(message, "Silahkan ketik /start untuk memulai bot ini.")


bot.polling()