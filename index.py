import telebot 

bot = telebot.TeleBot('7143493574:AAG35cEPwLd1df3U4Cbb_9neW6b4OAUxAnE')


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Привет')
    
@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id, 'Это меню сталовой <b> АГПК </b>, закажи еду сидя на паре', parse_mode='html')

@bot.message_handler()
def info(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name} {message.from_user.last_name}')

bot.polling(none_stop=True)