#!/usr/bin/python
# -*- coding: utf-8 -*-


from maxbotapi import BotHandler
import json

config = 'config.json'
with open(config, 'r', encoding='utf-8') as c:
    conf = json.load(c)
    token = conf['access_token']

bot = BotHandler(token)

def main():
    while True:
        last_update = bot.get_updates()
        if last_update: #проверка на пустое событие, если пусто - возврат к началу цикла
            user_id = bot.get_user_id(last_update)
            mid = bot.get_message_id(last_update)
            admins = bot.get_chat_admins(bot.get_chat_id(last_update))
            list_admin = []
            if admins:
                admins = admins['members']
                for admin in admins:
                    list_admin.append(admin['user_id'])
            if user_id not in list_admin:
                bot.delete_message(mid)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()
