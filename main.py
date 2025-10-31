import telebot

bot = telebot.TeleBot("8322895283:AAFDxby89-g5EB0w_9M40g25pG_Y...")  # ← өзүңдүн токениңди ушул жерге кой

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Салам! 🤖 Бот иштеп жатат!")

bot.infinity_polling()
