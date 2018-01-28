# Code done with the help of Gareth Dwyer, based on
# https://www.codementor.io/garethdwyer/building-a-telegram-bot-using-python-part-1-goi5fncay
# Priceless - Team Scrub for NUS Hack & Roll 2018

import json, logging
import requests, urllib
import time, traceback
import priceless

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
    url = URL + "sendMessage?parse_mode=HTML&text={}&chat_id={}".format(text, chat_id)
    get_url(url)

def reply_all(updates):
    for update in updates["result"]:
        try:
            userid = update["message"]["from"]["id"]
            username = update["message"]["from"]["username"]
            text = update["message"]["text"]
            chat = update["message"]["chat"]["id"]
            update_id = update["update_id"]

            text_words = text.split(" ")

            if text_words[0] == "/help":
                results = "*Welcome!*\nTo begin, simply input /compare and the item you want to search, " \
                +"followed by the price you are comfortable with.\nFor example, if you're " \
                +"looking for an <i>iPhone 6</i> and you're willing to pay <i>$500</i>, type \"<b>/find iPhone 6 500</b>\""

            elif text_words[0] == "/find":
                try:
                    text = text[6:]
                    # This is where we call Priceless's main API
                    itemlist = priceless.search(text)
                    #print(itemlist)
                    if (len(itemlist) == 0):
                        results = "Sorry <a href=\"tg://user?id={}\">{}</a>, there are no price comparison results for <b>'{}'</b>:\n".format(userid, username, text)
                    else:
                        results = "Hi <a href=\"tg://user?id={}\">{}</a>, these are the following price comparison results for <b>'{}'</b>:\n".format(userid, username, text)
                    counter = 1
                    for item in itemlist:
                        results += "<b>" + str(counter) + ". "
                        results += item["product_name"] + "</b>\n"
                        results += "Price: " + str(item["price"]) + "\n"
                        results += "URL: " + item["url"] + "\n"
                        item.pop("product_name")
                        item.pop("price")
                        item.pop("url")
                        for k in item:
                            results += k + ": " + item[k] + "\n"
                        counter += 1
                except ValueError as error:
                    results = "Sorry, <a href=\"tg://user?id={}\">{}</a>, you have entered an invalid price.".format(userid, username) \
                    + "\n\n<b>Example</b>\nIf you're looking for an <i>iPhone 6</i> and you are willing to pay <i>$500</i>, " \
                    + "type \"<b>/find iPhone 6 500</b>\""
            if len(results) > 4095:
                results = "Sorry <a href=\"tg://user?id={}\">{}</a>, the price comparison results for <b>'{}'</b> is too long to be sent.\n".format(userid, username, text)
            send_message(results, chat)
            logging.info(("UserID: {}, Username: {}, Text: {}, Chat: {}, Update_ID: {}, Results: {}").format(userid, username, text, chat, update_id, results))
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