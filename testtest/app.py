import  telebot
import user as u
from config import TOKEN
from test import Test


bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def strt(message: telebot.types.Message):
    id = message.chat.id
    if id not in u.id_lst:
        u.id_lst.append(id)
        u.create_user(id, message.chat.first_name)
    print(u.usr_lst)
    name = message.chat.first_name
    bot.send_message(message.chat.id, f"Приветствуем вас {name}!\n"
                                      "Хотите узнать ваще тотемное животное?\nВведите /test для начала теста"
                                      "\n Для помощи введите /help\n Для перезапуска теста введите /restart"
                                      "\n Обратная связь killedraccoon@gmail.com"
                                      "\n Поддержка killedraccoon@gmail.com"
                                      "\n Дополнительная информация /info")

@bot.message_handler(commands=['help'])
def help(message: telebot.types.Message):
    bot.send_message(message.chat.id, f'/start - запуск и перезапуск бота\n'
                                      f'/test - начало теста\n /restart - перезаупск теста'
                                      f'\n /info - Дополнительная информация ')

@bot.message_handler(commands=['restart'])
def rastrt(message: telebot.types.Message):
    us = u.getUser(message.chat.id)
    bot.send_message(message.chat.id, 'Перезапуск')
    us.q_count = 1
    us.intest = False
    test_start(message)

@bot.message_handler(commands=['info'])
def info(message: telebot.types.Message):
    bot.send_message(message.chat.id,'В зоопарке действует программа "Возьми животное под опеку"\n'
                                     'Подробности по ссылке: \n'
                                     'https://moscowzoo.ru/my-zoo/become-a-guardian/')

@bot.message_handler(commands=['test'])
def test_start(message: telebot.types.Message):
    try:
        us = u.getUser(message.chat.id)
        print(us.intest)
        if not us.intest:
            us.intest = True
            print(us.q_count)
            text = Test.qst_block(us.q_count)
            bot.send_message(message.chat.id, f"{text}\n")
            us.q_count += 1
        else:
            test(message)
    except ValueError or IndexError as ex:
        with open('log.txt', 'w') as f:
            f.write(str(ex)+' Пользователь не создан')
        strt(message)



@bot.message_handler(content_types=['text',])
def test(message: telebot.types.Message):
    try:
        us = u.getUser(message.chat.id)
        text, win = Test.test_block(us, message)
        bot.send_message(message.chat.id, text)
        if win != None:
            with open(win.img,'rb') as img:
                bot.send_photo(message.chat.id, img)
                bot.send_message(message.chat.id, win.descr)
            with open('users.txt', 'w', encoding='utf8') as f:
                f.write(f'{us.name} тотемное животное {win.name}\n')
            info(message)
            win = None
        print('пашет')

    except ValueError or IndexError as ex:
        with open('log.txt', 'w') as f:
            f.write(str(ex))
        strt(message)


bot.polling()