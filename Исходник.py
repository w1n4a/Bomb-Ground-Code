import telebot
import random
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


bot = telebot.TeleBot('Ваш Токен')


inline_kb = InlineKeyboardMarkup()
inline_kb.add(InlineKeyboardButton('❓', callback_data='button1'))
inline_kb.add(InlineKeyboardButton('❓', callback_data='button2'))
inline_kb.add(InlineKeyboardButton('❓', callback_data='button3'))
inline_kb.add(InlineKeyboardButton('❓', callback_data='button4'))
inline_kb.add(InlineKeyboardButton('Исходный Код', url="https://github.com/w1n4a/Bomb-Ground-Code/blob/main/%D0%98%D1%81%D1%85%D0%BE%D0%B4%D0%BD%D0%B8%D0%BA.py"))

@bot.message_handler(commands=['start'])
def game(message):
    bot.send_message(
        message.chat.id,
        'Выбери клетку:',
        reply_markup=inline_kb
    )
    global boom
    boom = random.randint(1,2)
    global boom2
    boom2 = random.randint(3,4)

@bot.callback_query_handler(func=lambda call: True)
def handle_callback(call):
    if call.data == 'button1':
        plr = 1
    if call.data == 'button2':
        plr = 2
    if call.data == 'button3':
        plr = 3
    if call.data == 'button4':
        plr = 4
    
    if boom == plr or boom2 == plr:
        bot.send_message(call.message.chat.id, "Ты взорвался!\nСледующия ката - /start")
    else:
        bot.send_message(call.message.chat.id, "Ты выжил!\nСледующия ката - /start")
    

bot.polling()

#by w1n4a

