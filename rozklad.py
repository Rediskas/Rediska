import telebot

bot = telebot.TeleBot('1053474569:AAEH7lPrmQrL7D7-8yUTcEg589uN9pbUoPY')
keyboard1 = telebot.types.ReplyKeyboardMarkup(1)
keyboard1.row('Понеділок', 'Вівторок', 'Середа','Четвер',"П'ятниця")

@bot.message_handler(commands=['start'])
def start_message(message):
    if message.text == '/start':
        bot.send_message(message.chat.id, 'Привіт,клікни на кнопку щоб дізнатися розклад', reply_markup=keyboard1)

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'понеділок':
        bot.send_message(message.chat.id, '1.Алгебра\n2.Укр Мова\n3.Фізика\n4.Інформатика\n5.Англ.Мова\n6.Фіз.культура')
    
    elif message.text.lower() == 'вівторок':
        bot.send_message(message.chat.id, '1.Англ.мова\n2.Зарубіжна\n3.Геометрія\n4.Географія\n5.Укр.літ\n6.Фізика\n7.ЗВ/Медицина')
   
    elif message.text.lower() == 'середа':
       bot.send_message(message.chat.id,
'1.Хімія\n2.Інформатика\n3.Алгебра\n4.Біологія\n5.Історія\n6.Англ.мова')
   
    elif message.text.lower() == 'четвер':
      bot.send_message(message.chat.id,
'1.Фіз.культура\n2.Історія\n3.Геометрія\n4.Укр.мова\n5.Фізика\n6.Труд.Навч\n7.ЗВ/Медицина')   
    
    elif message.text.lower() == "п'ятниця":
       bot.send_message(message.chat.id,
'1.Астрономія\n2.Біологія\n3.Хімія\n4.Укр.літ\n5.Історія\n6.Фіз.культура')

bot.polling(none_stop=True)