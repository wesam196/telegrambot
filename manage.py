import requests
from telegram import *
import telebot
from datetime import date


class BotHandler():
    def __init__(self, token):
        self.token = token
        self.api_url = "https://api.telegram.org/bot{}/".format(token)

    #url = "https://api.telegram.org/bot<token>/"

    def get_updates(self, offset=0, timeout=30):
        method = 'getUpdates'
        params = {'timeout': timeout, 'offset': offset}
        resp = requests.get(self.api_url + method, params)
        result_json = resp.json()["result"]
        return result_json

    def send_message(self, chat_id, text):
        params = {'chat_id': chat_id, 'text': text, 'parse_mode': 'HTML'}
        method = 'sendMessage'
        resp = requests.post(self.api_url + method, params)
        return resp

    def get_first_update(self):
        get_result = self.get_updates()
        Update
        if len(get_result) > 0:
            last_update = get_result[0]
        else:
            last_update = None

        return last_update


token = '1281609833:AAFMVFZcn4YcbsKcK9Jv7yJCKlnDpoMhQkA' #Token of your bot
magnito_bot = BotHandler("1281609833:AAFMVFZcn4YcbsKcK9Jv7yJCKlnDpoMhQkA") #Your bot's name

bot=telebot.TeleBot("1281609833:AAFMVFZcn4YcbsKcK9Jv7yJCKlnDpoMhQkA")















def main():
    d0 = date(2021, 5, 2)
    d1 = date.today()
    delta = d1 - d0
    new_offset = 0
    print('hi, now launching...')

    while True:
        all_updates=magnito_bot.get_updates(new_offset)

        if len(all_updates) > 0:
            for current_update in all_updates:
                print(current_update)
                first_update_id = current_update['update_id']
                if 'text' not in current_update['message']:
                    first_chat_text='New member'
                else:
                    first_chat_text = current_update['message']['text']
                first_chat_id = current_update['message']['chat']['id']
                if 'first_name' in current_update['message']:
                    first_chat_name = current_update['message']['chat']['first_name']
                elif 'new_chat_member' in current_update['message']:
                    first_chat_name = current_update['message']['new_chat_member']['username']
                elif 'from' in current_update['message']:
                    first_chat_name = current_update['message']['from']['first_name']
                else:
                    first_chat_name = "unknown"




               
                   
                if first_chat_text == '/start':
                    #bot.send_message(first_chat_id,"مرحباً بك في المساعد")
                    magnito_bot.send_message(first_chat_id,"مرحباً")
                    new_offset = first_update_id + 1

                elif first_chat_text=="موعد العلاج":
                    for i in str(delta).split():
                        if i.isdigit():
                            k=int(i)+1

                            if (k%2!=0):
                                magnito_bot.send_message(first_chat_id,"اليوم موعد العلاج")
                            else:
                                magnito_bot.send_message(first_chat_id,"غداً موعد العلاج")
                    new_offset = first_update_id + 1
                else:
                    #magnito_bot.send_message(first_chat_id," عدد الكلمات: "+str(len(first_chat_text.split()))+"\nعدد الأحرف: " +str(len(first_chat_text)) )
                    None
                    new_offset = first_update_id + 1


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()