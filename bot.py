# -*- coding: utf-8 -*-

import re
import telebot
import urllib2
token = '323152778:AAEEm2guy91BDoM32qwgp3dAON0WTFm0fK8'

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
        bot.reply_to(message, u"Привет, как дела?")


@bot.message_handler(regexp="give me (.*)")
def handle_message(message):
    data = re.search("give me (.*)", message.text).group(1)
    x = urllib2.urlopen('http://hh.ru').read()
    res = re.search(".*href=\"(.*?\.jpg)\".*?>",x)
    if res is not None:
        img = "https://lurkmore.to"+res.group(1)
        bot.send_message(message.chat.id, img)
    else:
        bot.send_message(message.chat.id, u"Я не смог")

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    if message.text == u"кис":
        bot.send_message(message.chat.id, u"мяу")
    else:
        bot.send_message(message.chat.id, message.text)


bot.polling()
