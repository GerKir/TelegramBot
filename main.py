import telebot
import constants
bot = telebot.TeleBot(constants.token)

print("bot.get_me:")
print(bot.get_me())

def log(message):
    print("\n-------")
    from datetime import datetime
    print(datetime.now())
    print("Сообщение от:\n{0} {1}. (id = {2}) \nТекст:\n{3}".format(message.from_user.first_name,
                                                                    message.from_user.last_name,
                                                                    str(message.from_user.id),
                                                                    message.text))
#    print(answer)

user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
user_markup.row("Выбрать мастера", "Выбрать время", "Выбрать стрижку")
user_markup.row("Проверить запись", "Закрыть меню")

@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, "Меню", reply_markup=user_markup)
    log(message)

@bot.message_handler(content_types=['text'])
def menu(message):
    log(message)
# Меню выбора мастера
    if message.text == "Выбрать мастера":
        master_markup = telebot.types.ReplyKeyboardMarkup(True, True)
        master_markup.row("Сергей", "Фёдор", "Олег")
        bot.send_message(message.chat.id, "Выберете мастера", reply_markup=master_markup)
# Меню выбора времени
    elif message.text == "Выбрать время":
        time_markup = telebot.types.ReplyKeyboardMarkup(True)
        time_markup.row("11:00", "14:00", "17:30")
        bot.send_message(message.chat.id, "Выберете время", reply_markup=time_markup)
# Меню выбора срижки
    elif message.text == "Выбрать стрижку":
        hair_markup = telebot.types.ReplyKeyboardMarkup(True)
        hair_markup.row("Стрижка головы", "Стрижка бороды", "Стрижка усов")
        bot.send_message(message.chat.id, "Выберете стрижку", reply_markup=hair_markup)
# Выводит проверку записи
    elif message.text == "Проверить запись":
        bot.send_message(message.chat.id, constants.Bot_hair + ". Ваш мастер: " + constants.Bot_master
                         + ". Время записи: " + constants.Bot_time)
# Выбор мастера
    elif message.text == "Сергей":
        constants.Bot_master = message.text
        bot.send_message(message.chat.id, "Ваш мастер: " + constants.Bot_master, reply_markup=user_markup)
    elif message.text == "Фёдор":
        constants.Bot_master = message.text
        bot.send_message(message.chat.id, "Ваш мастер: " + constants.Bot_master, reply_markup=user_markup)
    elif message.text == "Олег":
        constants.Bot_master = message.text
        bot.send_message(message.chat.id, "Ваш мастер: " + constants.Bot_master, reply_markup=user_markup)
# Выбор времени
    elif message.text == "11:00":
        constants.Bot_time = message.text
        bot.send_message(message.chat.id, "Вы записались на " + constants.Bot_time, reply_markup=user_markup)
    elif message.text == "14:00":
        constants.Bot_time = message.text
        bot.send_message(message.chat.id, "Вы записались на " + constants.Bot_time, reply_markup=user_markup)
    elif message.text == "17:30":
        constants.Bot_time = message.text
        bot.send_message(message.chat.id, "Вы записались на " + constants.Bot_time, reply_markup=user_markup)
# Выбор стрижки
    elif message.text == "Стрижка головы":
        constants.Bot_hair = message.text
        bot.send_message(message.chat.id, "Вы записались на: " + constants.Bot_hair, reply_markup=user_markup)
    elif message.text == "Стрижка бороды":
        constants.Bot_hair = message.text
        bot.send_message(message.chat.id, "Вы записались на: " + constants.Bot_hair, reply_markup=user_markup)
    elif message.text == "Стрижка усов":
        constants.Bot_hair = message.text
        bot.send_message(message.chat.id, "Вы записались на: " + constants.Bot_hair, reply_markup=user_markup)
# Закрыть меню
    elif message.text == "Закрыть меню":
        bot.send_message(message.chat.id, "Чтобы открыть меню - напиши /start")
    else:
        bot.send_message(message.chat.id, "Извини, я пока что плохо говорю по-человечьи, но скоро научусь! \nА пока что можешь записаться на стрижку с помощью команды /start")



bot.polling(none_stop=True, interval=0)