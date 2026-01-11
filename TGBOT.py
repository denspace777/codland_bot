import telebot
from bot_logic import gen_pass #, gen_rnd_smile

# Замени 'TOKEN' на токен твоего бота
# Этот токен ты получаешь от BotFather, чтобы бот мог работать
bot = telebot.TeleBot("7639056794:AAHrGV-Yh87bNoAsukyjpXtNCsjD6mX4m8g")

# Обработчик команды '/start' и '/hello'
@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    name = message.from_user.first_name
    bot.reply_to(message, f'Привет, {name}! Я бот {bot.get_me().first_name}!')

 # Обработчик команды '/heh'
@bot.message_handler(commands=['heh'])
def send_heh(message):
    count_heh = int(message.text.split()[1]) if len(message.text.split()) > 1 else 5
    bot.reply_to(message, "he" * count_heh)

@bot.message_handler(commands=['bye'])
def send_bye(message):
    bot.reply_to(message, "Пока! Удачи!")

@bot.message_handler(commands=['bebebe'])
def send_bebebe(message):
    bot.reply_to(message, ">:(")

@bot.message_handler(commands=['gen_pass'])
def send_pass(message):
    bot.reply_to(message,'Напишите длину пароля:')
    bot.register_next_step_handler(message, send_pass)
def send_pass(message):
    len_pass = int(message.text)
    if len_pass <= 4000:
        bot.reply_to(message, f"Вот ваш пароль: {gen_pass(len_pass)}")
    else:
        bot.reply_to(message, "Длина паролья слишком блоьшая!")

@bot.message_handler(commands=['secret_comand'])
def send_bebebe(message):
    bot.reply_to(message, "Поздравляю! Ты нашёл секретную команду! XD")



@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.polling()


