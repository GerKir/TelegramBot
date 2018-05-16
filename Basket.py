import telebot
import constants

bot = telebot.TeleBot(constants.token)

print("bot.get_me:")
print(bot.get_me())

def log(message,answer):
    print("\-------")
    from datetime import datetime
    print(datetime.now())
    print("Сообщение от:\n{0} {1}. (id = {2}) \nТекст:\n{3}\n-------".format(message.from_user.first_name,
                                                                   message.from_user.last_name,
                                                                   str(message.from_user.id),
                                                                   message.text))

@bot.message_handler(commands=['start'])
def handle_start(message):
    answer = "Здесь будет меню"
    log(message, answer)
    bot.send_message(message.chat.id, answer)

@bot.message_handler(content_types=['text'])
def handle_text(message):
    answer = "Я просто бот, и не понимаю что ты говоришь! \nПока что..."
    log(message, answer)
    taxi = message.text
    print("Первая буква:")
    print(taxi[0])
    if taxi == "Fuck you":
        bot.send_message(message.chat.id, "Не нужно быть таким грубым:(")
    else:
        bot.send_message(message.chat.id, answer)

bot.polling(none_stop=True, interval=0)