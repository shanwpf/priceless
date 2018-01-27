# Code done with the help of Gareth Dwyer, based on
# https://www.codementor.io/garethdwyer/building-a-telegram-bot-using-python-part-1-goi5fncay
# Priceless - Team Scrub for NUS Hack & Roll 2018

import json, logging
import requests, urllib
import time, traceback
from modules.util import botinterface

# Logging Setup
logging.basicConfig(format='%(asctime)s-%(name)s:%(levelname)s - %(message)s',
                    level=logging.INFO, filename='bot.log')
logging.getLogger().addHandler(logging.StreamHandler())

# Bot Credentials
TOKEN = "522293065:AAG2bvhJR_iLTjt9PvYK9mklPNf6O_mm3Lw"
URL = "https://api.telegram.org/bot{}/".format(TOKEN)

def get_url(url):
    response = requests.get(url)
    content = response.content.decode("utf8")
    return content

def get_json_from_url(url):
    content = get_url(url)
    js = json.loads(content)
    return js

def get_updates(offset=None):
    url = URL + "getUpdates"
    if offset:
        url += "?offset={}".format(offset)
    url += "?time=100"
    print(url)    
    js = get_json_from_url(url)
    return js

def get_last_update_id(updates):
    update_ids = []
    for update in updates["result"]:
        update_ids.append(int(update["update_id"]))
    return max(update_ids)

def get_last_chat_id_and_text(updates):
    num_updates = len(updates["result"])
    last_update = num_updates - 1
    text = updates["result"][last_update]["message"]["text"]
    chat_id = updates["result"][last_update]["message"]["chat"]["id"]
    return (text, chat_id)

def send_message(text, chat_id):
    text = urllib.parse.quote_plus(text)
    url = URL + "sendMessage?parse_mode=Markdown&text={}&chat_id={}".format(text, chat_id)
    get_url(url)

def reply_all(updates):
    for update in updates["result"]:
        try:
            name = update["message"]["from"]["first_name"]
            text = update["message"]["text"]
            chat = update["message"]["chat"]["id"]
            update_id = update["update_id"]

            if text == "/help":
                results = "*Welcome!*\nTo begin, simply input the item you want to search, " \
                +"followed by the price you are comfortable with.\nFor example, if you want " \
                +"to find an _iPhone 6_ and you can only pay around _$100_, input \"*iPhone 6 100*\""

            else:
                # This is where we call Priceless's main API
                results = "Hi {}, these are the following price comparison results for {}".format(name, text)
                print(text)
                list = botinterface.search(text)
                print(list)
                # ...
            
            send_message(results, chat,)
            logging.info(("Name: {}, Text: {}, Chat: {}, Update_ID: {}, Results: {}").format(name, text, chat, update_id, results))
        except Exception as e:
            logging.warning('Error comparing prices. ' + traceback.format_exc())
            continue
    
def main():
    last_update_id = None
    while True:
        updates = get_updates(last_update_id)
        # print (last_update_id)
        if len(updates["result"]) > 0:
            last_update_id = get_last_update_id(updates) + 1
            reply_all(updates)
        time.sleep(0.5)

if __name__ == '__main__':
    main()