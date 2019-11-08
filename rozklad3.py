import telebot

bot = telebot.TeleBot('1068057744:AAHqcma-XjABK-y9twMiiVItwBK7oPfLCfg')
keyboard1 = telebot.types.ReplyKeyboardMarkup(1)
keyboard1.row('Понеділок', 'Вівторок', 'Середа','Четвер',"П'ятниця")

@bot.message_handler(commands=['start'])
def start_message(message):
    if message.text == '/start':
        bot.send_message(message.chat.id, 'Бота створив:\nInstagram:@denysdovg\nTelegram:@denysdovg', reply_markup=keyboard1)

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'понеділок':
        bot.send_message(message.chat.id, '1.Алгебра\n2.Геометрія\n3.Зарубіжна\n4.Історія\n5.Укр.літ\n6.Фіз.культура\n7.Гром.освіта')
    
    elif message.text.lower() == 'вівторок':
        bot.send_message(message.chat.id, '1.Біологія\n2.Історія\n3.Історія\n4.Хімія\n5.Географія\n6.Фізика')
   
    elif message.text.lower() == 'середа':
       bot.send_message(message.chat.id,
'1.Алгебра\n2.Англ.мова\n3.Англ.мова\n4.Укр.мова\n5.Медицина/ОЗВ\n6.Біологія')
   
    elif message.text.lower() == 'четвер':
      bot.send_message(message.chat.id,
'1.Укр.літ\n2.Хр.етика\n3.Хімія\n4.Гром.освіта\n5.Фізика\n6.Труд.навч\n7.Труд.навч')   
    
    elif message.text.lower() == "п'ятниця":
       bot.send_message(message.chat.id,
'1.Фізика\n2.Англ.мова\n3.Укр.мова\n4.Інформатика\n5.Геометрія')

bot.polling(none_stop=True)