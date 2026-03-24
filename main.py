import telebot
from telebot import types
from apisetup import api
t_token = api
bot = telebot.TeleBot(t_token)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == '/start':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #create buttons
        btn1 = types.KeyboardButton('Магазини')
        btn4 = types.KeyboardButton('Знижки')
        btn2 = types.KeyboardButton('Про нас')
        btn3 = types.KeyboardButton(f'Зворотний зв{chr(39)}язок')
        btn5 = types.KeyboardButton('Підтримка')
        markup.add(btn1, btn4, btn2, btn3, btn5)
        bot.send_message(message.from_user.id, '👋 Привіт у iMagala Delivery! 🚀' +
                         '\nХочеш швидку доставку?\nМи вже в дорозі! '
                         'Обирай товари — ми доставимо їх просто до тебе додому.'+ '\n' +
                         'iMagala Delivery — замовив і вже чекаєш! 😎', reply_markup=markup)

    elif message.text == 'Магазини':
        bot.send_message(message.from_user.id, 'Тут список магазинів.',
        parse_mode="Markdown")
    elif message.text == 'Про нас':
        bot.send_message(message.from_user.id, "Розроблено для громади."
        "\nРозробники:\nЯкобець Д.Г,\nЯкобець Г.С,\nГостюк К.І",
        parse_mode='Markdown')
    elif message.text == f'Зворотний зв{chr(39)}язок':
        bot.send_message(message.from_user.id,
        "Наші контакти\n+380572825271\n+380675423167\n+380675423167", parse_mode='Markdown')
    elif message.text == 'Знижки': 
        bot.send_message(message.from_user.id,'Тут буде знижки', parse_mode='Markdown')
    elif message.text == 'Підтримка':
        bot.send_message(message.from_user.id,'Підтримка буде скоро')

bot.polling(non_stop=True, interval=0)