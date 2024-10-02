import telebot
from telebot import types
bot = telebot.TeleBot('7101342882:AAFv0HCC7Js543lJE7JlPEHaO1tpxubnpmw')

age = 0;
@bot.message_handler(content_types=['text'])

def get_text_messages(message):
    #bot.send_message(message.from_user.id, "Напиши Hi")
    if message.text == "Hi" or message.text == "hi":
        # global name;
        # name = message.text;
        bot.send_message(message.from_user.id, "Ваа, Привет!")
        bot.send_message(message.from_user.id,'Сколько тебе лет?')
        bot.register_next_step_handler(message, get_age)
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши Hi")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")

def get_age(message):
    global age
    i=0
    # if int(message.text):
    #      age = int(message.text)  # проверяем, что возраст введен корректно
    # print(age)
    while age == 0: #проверяем что возраст изменился
        try:
             age = int(message.text) #проверяем, что возраст введен корректно
             print (age)
             break
        except Exception:
             bot.send_message(message.from_user.id, 'Цифрами, пожалуйст')
             i+=1
             if i==2:
                age = -1
    bot.send_message(message.from_user.id,str(age))
    bot.send_message(message.from_user.id, ' ого, а ты молод')
    keyboard = types.InlineKeyboardMarkup() #наша клавиатура
    key_yes = types.InlineKeyboardButton(text='Согласен', callback_data='yes') #кнопка «Да»
    keyboard.add(key_yes) #добавляем кнопку в клавиатуру
    key_no= types.InlineKeyboardButton(text='Нет', callback_data='no')
    keyboard.add(key_no)
    #question = 'Отвечай'
    question = 'Согласен?'
    bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "yes": #call.data это callback_data, которую мы указали при объявлении кнопки
        #код сохранения данных, или их обработки
        bot.send_message(call.message.chat.id, 'Молодец : )')
    elif call.data == "no":
         #переспрашиваем
         bot.send_message(call.message.chat.id, 'Запомню : )')

bot.polling(none_stop=True, interval=0)